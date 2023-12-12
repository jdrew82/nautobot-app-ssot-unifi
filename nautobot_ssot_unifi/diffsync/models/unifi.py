"""DiffSync models for Nautobot SSoT UniFi."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Device in Unifi from UnifiDevice object."""
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Device in Unifi from UnifiDevice object."""
        return super().update(attrs)

    def delete(self):
        """Delete Device in Unifi from UnifiDevice object."""
        return self
