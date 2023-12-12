"""Utility functions for working with UniFi."""
from django.conf import settings

from pyunifi.controller import Controller

PLUGIN_CFG = settings.PLUGINS_CONFIG["nautobot_ssot_unifi"]


def connect_controller():
    """Generate connection to UniFi controller API endpoint.

    Returns:
        Controller: Connection to UniFi Controller.
    """
    return Controller(
        host=PLUGIN_CFG["unifi_host"],
        username=PLUGIN_CFG["unifi_user"],
        password=PLUGIN_CFG["unifi_password"],
        port=PLUGIN_CFG["unifi_port"],
        ssl_verify=PLUGIN_CFG["verify"],
    )
