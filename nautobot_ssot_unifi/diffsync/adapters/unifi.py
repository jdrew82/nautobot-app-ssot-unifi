"""Nautobot Adapter for UniFi SSoT plugin."""

from diffsync import DiffSync
from pyunifi.controller import Controller
from nautobot_ssot_unifi.constants import DEVICETYPE_MAP
from nautobot_ssot_unifi.diffsync.models.unifi import (
    UniFiLocationTypeModel,
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

    locationtype = UniFiLocationTypeModel
    location = UniFiLocationModel
    manufacturer = UniFiManufacturerModel
    devicetype = UniFiDeviceTypeModel
    role = UniFiRoleModel
    device = UniFiDeviceModel
    interface = UniFiInterfaceModel

    top_level = ["locationtype", "location", "manufacturer", "devicetype", "role", "device", "interface"]

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
        self.get_or_instantiate(
            self.locationtype, ids={"name": "Site", "content_types": [{"app_label": "dcim", "model": "device"}]}
        )
        locations = get_sites(conn=self.conn)
        for site in locations:
            self.site_map[site["_id"]] = site["desc"]
            self.get_or_instantiate(
                self.location,
                ids={"name": site["desc"], "location_type__name": "Site"},
                attrs={"status__name": "Active"},
            )

    def load_manufacturer(self, manu_name: str = "Ubiquiti"):
        """Load Manufacturer from UniFi as Manufacturer."""
        self.get_or_instantiate(self.manufacturer, ids={"name": manu_name})

    def load_devicetype(self, model: str, manu_name: str = "Ubiquiti"):
        """Load Device models from UniFi as DeviceType."""
        self.get_or_instantiate(self.devicetype, {"model": model, "manufacturer__name": manu_name})

    def load_unifi_devices(self):
        """Load Devices from UniFi as Devices."""
        aps = self.conn.get_aps()
        for ap in aps:
            model = DEVICETYPE_MAP[ap["model"]] if DEVICETYPE_MAP.get(ap["model"]) else ap["model"]
            location = self.site_map[ap["site_id"]] if ap.get("site_id") else "Unknown"
            self.load_manufacturer()
            self.load_devicetype(model)
            self.get_or_instantiate(
                self.device,
                ids={"name": ap["name"]},
                attrs={
                    "location__name": location,
                    "serial": ap["serial"],
                    "role__name": "Unknown",
                    "device_type__model": model,
                    "device_type__manufacturer__name": "Ubiquiti",
                    "status__name": "Active",
                },
            )
            self.get_or_instantiate(
                self.role, ids={"name": "Unknown"}, attrs={"content_types": [{"app_label": "dcim", "model": "device"}]}
            )

    def load_clients(self):
        """Load client devices from UniFi as Devices."""
        clients = self.conn.get_clients()
        for client in clients:
            if client.get("hostname") and client["hostname"] != "\x03":
                site = self.site_map[client["site_id"]] if client.get("site_id") else "Unknown"
                manu_name = client["oui"] if client.get("oui") else "Unknown"
                self.load_manufacturer(manu_name=manu_name)
                self.load_devicetype(model="Unknown Device", manu_name=manu_name)
                self.get_or_instantiate(
                    self.device,
                    ids={"name": client["hostname"]},
                    attrs={
                        "location__name": site,
                        "serial": "",
                        "role__name": "Client",
                        "device_type__model": "Unknown Device",
                        "device_type__manufacturer__name": manu_name,
                        "status__name": "Active",
                    },
                )
                self.get_or_instantiate(
                    self.role,
                    ids={"name": "Client"},
                    attrs={"content_types": [{"app_label": "dcim", "model": "device"}]},
                )

    def load(self):
        """Load data from UniFi into DiffSync models."""
        self.load_sites()
        self.load_unifi_devices()
        self.load_clients()
