"""DiffSyncModel subclasses for Nautobot-to-UniFi data sync."""
from typing import Optional
from nautobot_ssot.contrib import NautobotModel
from nautobot.dcim.models import Device, DeviceType, Interface, Location, Manufacturer
from nautobot.extras.models import Role


class LocationModel(NautobotModel):
    """DiffSync model for UniFi locations."""

    _model = Location
    _modelname = "location"
    _identifiers = ("name", "location_type__name")
    _attributes = ("content_types",)
    _children = {}

    name: str
    location_type__name: str
    content_types: str


class ManufacturerModel(NautobotModel):
    """DiffSync model for UniFi client vendors."""

    _model = Manufacturer
    _modelname = "manufacturer"
    _identifiers = ("name",)
    _attributes = ()
    _children = {}

    name: str


class DeviceTypeModel(NautobotModel):
    """DiffSync model for UniFi device hardware."""

    _model = DeviceType
    _modelname = "devicetype"
    _identifiers = ("model", "manufacturer__name")
    _attributes = ()
    _children = {}

    model: str
    manufacturer__name: str


class RoleModel(NautobotModel):
    """DiffSync model for UniFi device roles."""

    _model = Role
    _modelname = "role"
    _identifiers = ("name",)
    _attributes = ("content_types",)
    _children = {}

    name: str
    content_types: str


class DeviceModel(NautobotModel):
    """DiffSync model for UniFi devices."""

    _model = Device
    _modelname = "device"
    _identifiers = ("name",)
    _attributes = (
        "location__name",
        "serial",
        "role__name",
        "devicetype__model",
        "devicetype__manufacturer__name",
    )
    _children = {}

    name: str
    location__name: str
    serial: Optional[str]
    role__name: Optional[str]
    devicetype__model: Optional[str]
    devicetype__manufacturer__name: Optional[str]


class InterfaceModel(NautobotModel):
    """DiffSync model for UniFi device interfaces."""

    _model = Interface
    _modelname = "interface"
    _identifiers = ("name",)
    _attributes = ("type", "mgmt_only")
    _children = {}

    name: str
    type: str
    mgmt_only: bool
