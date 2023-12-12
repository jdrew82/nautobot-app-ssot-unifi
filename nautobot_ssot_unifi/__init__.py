"""Plugin declaration for nautobot_ssot_unifi."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import NautobotAppConfig


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


config = NautobotSsotUniFiConfig  # pylint:disable=invalid-name
