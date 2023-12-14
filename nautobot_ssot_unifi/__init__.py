"""Plugin declaration for nautobot_ssot_unifi."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

__version__ = metadata.version(__name__)

from nautobot.core.signals import nautobot_database_ready
from nautobot.extras.plugins import NautobotAppConfig
from nautobot_ssot_unifi.signals import nautobot_database_ready_callback


class NautobotSsotUniFiConfig(NautobotAppConfig):
    """Plugin configuration for the nautobot_ssot_unifi plugin."""

    name = "nautobot_ssot_unifi"
    verbose_name = "Nautobot SSoT UniFi"
    version = __version__
    author = "Justin Drew"
    description = "Nautobot SSoT App for UniFi."
    base_url = "ssot-unifi"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}

    def ready(self):
        """Trigger callback when database is ready."""
        super().ready()

        nautobot_database_ready.connect(nautobot_database_ready_callback, sender=self)


config = NautobotSsotUniFiConfig  # pylint:disable=invalid-name
