"""Test UniFi adapter."""

import json
from unittest.mock import MagicMock, patch

from nautobot.extras.models import JobResult
from nautobot.core.testing import TransactionTestCase
from nautobot_ssot_unifi.diffsync.adapters.unifi import UniFiAdapter
from nautobot_ssot_unifi.jobs import UniFiDataSource


def load_json(path):
    """Load a json file."""
    with open(path, encoding="utf-8") as file:
        return json.loads(file.read())


SITE_FIXTURE = load_json("./nautobot_ssot_unifi/tests/fixtures/get_sites.json")
AP_FIXTURE = load_json("./nautobot_ssot_unifi/tests/fixtures/get_aps.json")


class TestUniFiAdapterTestCase(TransactionTestCase):
    """Test NautobotSsotUniFiAdapter class."""

    job_class = UniFiDataSource
    databases = ("default", "job_logs")

    def setUp(self):
        """Initialize test case."""
        self.unifi_client = MagicMock()
        self.unifi_client.get_aps.return_value = AP_FIXTURE

        self.job = self.job_class()
        self.job.job_result = JobResult.objects.create(
            name=self.job.class_path, task_name="fake task", worker="default"
        )
        self.unifi = UniFiAdapter(job=self.job, sync=None, client=self.unifi_client)

    @patch("nautobot_ssot_unifi.diffsync.adapters.unifi.get_sites")
    def test_load_sites(self, mock_get_sites):
        """Test Nautobot SSoT UniFi load_sites() function."""
        mock_get_sites.return_value = SITE_FIXTURE
        self.unifi.load_sites()
        self.assertEqual(
            {"Site"},
            {site.get_unique_id() for site in self.unifi.get_all("locationtype")},
        )
        self.assertEqual(
            {"Test__Site"},
            {site.get_unique_id() for site in self.unifi.get_all("location")},
        )

    def test_load_manufacturer(self):
        """Test Nautobot SSoT UniFi load_manufacturer() function."""
        self.unifi.load_manufacturer()
        self.assertEqual({"Ubiquiti"}, {manu.get_unique_id() for manu in self.unifi.get_all("manufacturer")})

    def test_load_devicetype(self):
        """Test Nautobot SSoT UniFi load_devicetype() function."""
        self.unifi.load_devicetype(model="Test")
        self.assertEqual({"Test__Ubiquiti"}, {dt.get_unique_id() for dt in self.unifi.get_all("devicetype")})

    def test_load_unifi_devices(self):
        """Test Nautobot SSoT UniFi load_unifi_devices() function."""
        self.unifi.site_map["63b0a5b8539cd042ecba85b5"] = "Test"
        self.unifi.load_unifi_devices()
        self.assertEqual(
            {dev["name"] for dev in AP_FIXTURE}, {dev.get_unique_id() for dev in self.unifi.get_all("device")}
        )
