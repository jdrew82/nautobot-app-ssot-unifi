"""DiffSync models for Nautobot SSoT UniFi."""

from nautobot_ssot_unifi.diffsync.models.base import (
    LocationModel,
    ManufacturerModel,
    RoleModel,
    DeviceTypeModel,
    DeviceModel,
    InterfaceModel,
)


class UniFiLocationModel(LocationModel):
    """UniFi implementation of Location DiffSync model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Location in UniFi from UniFiLocationModel object."""
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Location in UniFi from UniFiLocationModel object."""
        return super().update(attrs)

    def delete(self):
        """Delete Location in UniFi from UniFiLocationModel object."""
        return self


class UniFiManufacturerModel(ManufacturerModel):
    """UniFi implementation of Manufacturer DiffSync model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Manufacturer in UniFi from UniFiManufacturerModel object."""
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Manufacturer in UniFi from UniFiManufacturerModel object."""
        return super().update(attrs)

    def delete(self):
        """Delete Manufacturer in UniFi from UniFiManufacturerModel object."""
        return self


class UniFiDeviceTypeModel(DeviceTypeModel):
    """UniFi implementation of Manufacturer DiffSync model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create DeviceType in UniFi from UniFiDeviceTypeModel object."""
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update DeviceType in UniFi from UniFiDeviceTypeModel object."""
        return super().update(attrs)

    def delete(self):
        """Delete DeviceType in UniFi from UniFiDeviceTypeModel object."""
        return self


class UniFiRoleModel(RoleModel):
    """UniFi implementation of Manufacturer DiffSync model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Role in UniFi from UniFiRoleModel object."""
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Role in UniFi from UniFiRoleModel object."""
        return super().update(attrs)

    def delete(self):
        """Delete Role in UniFi from UniFiRoleModel object."""
        return self


class UniFiDeviceModel(DeviceModel):
    """UniFi implementation of Interface DiffSync model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Device in UniFi from UniFiDevice object."""
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Device in UniFi from UniFiDevice object."""
        return super().update(attrs)

    def delete(self):
        """Delete Device in UniFi from UniFiDevice object."""
        return self


class UniFiInterfaceModel(InterfaceModel):
    """UniFi implementation of Device DiffSync model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Interface in UniFi from UniFiInterfaceModel object."""
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Interface in UniFi from UniFiInterfaceModel object."""
        return super().update(attrs)

    def delete(self):
        """Delete Interface in UniFi from UniFiInterfaceModel object."""
        return self
