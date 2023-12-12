"""Nautobot Adapter for Unifi SSoT plugin."""

from nautobot_ssot.contrib import NautobotAdapter
from nautobot_ssot_unifi.diffsync.models.base import (
    LocationModel,
    ManufacturerModel,
    DeviceTypeModel,
    RoleModel,
    DeviceModel,
    InterfaceModel,
)


class UniFiNautobotAdapter(NautobotAdapter):
    """DiffSync adapter for Nautobot."""

    location = LocationModel
    manufacturer = ManufacturerModel
    devicetype = DeviceTypeModel
    role = RoleModel
    device = DeviceModel
    interface = InterfaceModel

    top_level = ["location", "manufacturer", "device", "interface"]
