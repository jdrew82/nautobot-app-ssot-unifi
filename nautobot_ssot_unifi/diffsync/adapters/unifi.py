"""Nautobot SSoT Unifi Adapter for Unifi SSoT plugin."""

from diffsync import DiffSync
from nautobot_ssot_unifi.diffsync.models.unifi import (
    UniFiLocationModel,
    UniFiManufacturerModel,
    UniFiRoleModel,
    UniFiDeviceModel,
    UniFiDeviceTypeModel,
    UniFiInterfaceModel,
)
class UniFiAdapter(DiffSync):
    """DiffSync adapter for UniFi."""

    location = UniFiLocationModel
    manufacturer = UniFiManufacturerModel
    devicetype = UniFiDeviceTypeModel
    role = UniFiRoleModel
    device = UniFiDeviceModel
    interface = UniFiInterfaceModel

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

        """Load Sites from UniFi as Locations."""
        """Load Manufacturer from UniFi as Manufacturer"""
        """Load Devices from UniFi as Devices."""
    def load(self):
        """Load data from UniFi into DiffSync models."""
