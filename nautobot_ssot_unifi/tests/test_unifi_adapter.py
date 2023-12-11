"""Test Unifi adapter."""

import json
from unittest.mock import MagicMock

from nautobot.extras.models import JobResult
from nautobot.core.testing import TransactionTestCase
from nautobot_ssot_unifi.diffsync.adapters.unifi import UnifiAdapter
from nautobot_ssot_unifi.jobs import UnifiDataSource


def load_json(path):
    """Load a json file."""
    with open(path, encoding="utf-8") as file:
        return json.loads(file.read())


DEVICE_FIXTURE = load_json("./nautobot_ssot_unifi/tests/fixtures/get_devices.json")


class TestUnifiAdapterTestCase(TransactionTestCase):
    """Test NautobotSsotUnifiAdapter class."""

    job_class = UnifiDataSource
    databases = ("default", "job_logs")

    def setUp(self):
        """Initialize test case."""
        self.unifi_client = MagicMock()
        self.unifi_client.get_devices.return_value = DEVICE_FIXTURE

        self.job = self.job_class()
        self.job.job_result = JobResult.objects.create(
            name=self.job.class_path, task_name="fake task", worker="default"
        )
        self.unifi = UnifiAdapter(job=self.job, sync=None, client=self.unifi_client)

    def test_data_loading(self):
        """Test Nautobot SSoT Unifi load() function."""
        # self.unifi.load()
        # self.assertEqual(
        #     {dev["name"] for dev in DEVICE_FIXTURE},
        #     {dev.get_unique_id() for dev in self.unifi.get_all("device")},
        # )
