"""Nautobot Adapter for UniFi SSoT plugin."""

from diffsync import DiffSync
from diffsync.exceptions import ObjectNotFound
from pyunifi.controller import Controller
from nautobot_ssot_unifi.constants import DEVICETYPE_MAP
from nautobot_ssot_unifi.diffsync.models.unifi import (
    UniFiLocationModel,
    UniFiManufacturerModel,
    UniFiRoleModel,
    UniFiDeviceModel,
    UniFiDeviceTypeModel,
    UniFiInterfaceModel,
)
from nautobot_ssot_unifi.utils.unifi import get_sites


class UniFiAdapter(DiffSync):
    """DiffSync adapter for UniFi."""

    location = UniFiLocationModel
    manufacturer = UniFiManufacturerModel
    devicetype = UniFiDeviceTypeModel
    role = UniFiRoleModel
    device = UniFiDeviceModel
    interface = UniFiInterfaceModel

    top_level = ["location", "manufacturer", "device", "interface"]

    def __init__(self, *args, job=None, sync=None, client: Controller, **kwargs):
        """Initialize UniFi Controller.

        Args:
            job (object, optional): UniFi Job. Defaults to None.
            sync (object, optional): UniFi DiffSync. Defaults to None.
            client (Controller): UniFi API client connection object.
        """
        super().__init__(*args, **kwargs)
        self.job = job
        self.sync = sync
        self.conn = client

        self.site_map = {}

    def load_sites(self):
        """Load Sites from UniFi as Locations."""
        locations = get_sites(conn=self.conn)
        for site in locations:
            self.site_map[site["_id"]] = site["desc"]
            new_site = self.location(
                name=site["desc"],
                content_types="device",
                location_type__name="Site",
            )
            self.add(new_site)

    def load_manufacturer(self):
        """Load Manufacturer from UniFi as Manufacturer."""
        ubi_vendor = self.manufacturer(
            name="Ubiquiti",
        )
        self.add(ubi_vendor)

    def load_devicetype(self, model: str, manu_name: str = "Ubiquiti"):
        """Load Device models from UniFi as DeviceType."""
        try:
            self.get(self.devicetype, {"model": model, "manufacturer__name": manu_name})
        except ObjectNotFound:
            new_dt = self.devicetype(
                model=model,
                manufacturer__name=manu_name,
            )
            self.add(new_dt)

    def load_unifi_devices(self):
        """Load Devices from UniFi as Devices."""
        aps = self.conn.get_aps()
        for ap in aps:
            model = DEVICETYPE_MAP[ap["model"]] if DEVICETYPE_MAP.get(ap["model"]) else ap["model"]
            location = self.site_map[ap["site_id"]] if ap.get("site_id") else "Unknown"
            self.load_devicetype(model)
            try:
                self.get(self.device, ap["name"])
            except ObjectNotFound:
                new_dev = self.device(
                    name=ap["name"],
                    location__name=location,
                    serial=ap["serial"],
                    role__name="Unknown",
                    devicetype__model=model,
                    devicetype__manufacturer__name="Ubiquiti",
                )
                self.add(new_dev)
            try:
                self.get(self.role, "Unknown")
            except ObjectNotFound:
                new_role = self.role(
                    name="Unknown",
                    content_types="device",
                )
                self.add(new_role)

    def load_clients(self):
        """Load client devices from UniFi as Devices."""
        clients = self.conn.get_clients()
        for client in clients:
            if client.get("hostname") and client["hostname"] != "\x03":
                site = self.site_map[client["site_id"]] if client.get("site_id") else "Unknown"
                try:
                    _ = self.get(self.device, client["hostname"])
                    self.job.logger.warning(f"Duplicate client found: {client['hostname']}.")
                except ObjectNotFound:
                    new_dev = self.device(
                        name=client["hostname"],
                        location__name=site,
                        serial=None,
                        role__name="Client",
                        devicetype__model="Unknown Device",
                        devicetype__manufacturer__name=client["oui"] if client.get("oui") else "Unknown",
                    )
                    self.add(new_dev)
                try:
                    self.get(self.role, "Client")
                except ObjectNotFound:
                    new_role = self.role(
                        name="Client",
                        content_types="device",
                    )
                    self.add(new_role)

    def load(self):
        """Load data from UniFi into DiffSync models."""
        self.load_sites()
        self.load_manufacturer()
        self.load_unifi_devices()
        self.load_clients()
