"""Jobs for UniFi SSoT integration."""

from nautobot.core.celery import register_jobs
from nautobot.extras.jobs import BooleanVar
from nautobot_ssot.jobs.base import DataSource, DataTarget
from nautobot_ssot_unifi.diffsync.adapters.nautobot import UniFiNautobotAdapter
from nautobot_ssot_unifi.diffsync.adapters.unifi import UniFiAdapter
from nautobot_ssot_unifi.utils.unifi import connect_controller


name = "UniFi SSoT"  # pylint: disable=invalid-name


class UniFiDataSource(DataSource):
    """UniFi SSoT Data Source."""

    debug = BooleanVar(description="Enable for more verbose debug logging", default=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta data for UniFi."""

        name = "UniFi to Nautobot"
        data_source = "UniFi"
        data_target = "Nautobot"
        description = "Sync information from UniFi to Nautobot"

    @classmethod
    def config_information(cls):
        """Dictionary describing the configuration of this DataSource."""
        return {}

    @classmethod
    def data_mappings(cls):
        """List describing the data mappings involved in this DataSource."""
        return ()

    def load_source_adapter(self):
        """Load data from UniFi into DiffSync models."""
        conn = connect_controller()
        self.source_adapter = UniFiAdapter(job=self, sync=self.sync, client=conn)
        self.source_adapter.load()

    def load_target_adapter(self):
        """Load data from Nautobot into DiffSync models."""
        self.target_adapter = UnifiNautobotAdapter(job=self, sync=self.sync)
        self.target_adapter.load()

    def run(  # pylint: disable=arguments-differ, too-many-arguments
        self, dryrun, memory_profiling, debug, *args, **kwargs
    ):
        """Perform data synchronization."""
        self.debug = debug
        self.dryrun = dryrun
        self.memory_profiling = memory_profiling
        super().run(dryrun=self.dryrun, memory_profiling=self.memory_profiling, *args, **kwargs)


class UniFiDataTarget(DataTarget):
    """UniFi SSoT Data Target."""

    debug = BooleanVar(description="Enable for more verbose debug logging", default=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta data for UniFi."""

        name = "Nautobot to UniFi"
        data_source = "Nautobot"
        data_target = "UniFi"
        description = "Sync information from Nautobot to UniFi"

    @classmethod
    def config_information(cls):
        """Dictionary describing the configuration of this DataTarget."""
        return {}

    @classmethod
    def data_mappings(cls):
        """List describing the data mappings involved in this DataSource."""
        return ()

    def load_source_adapter(self):
        """Load data from Nautobot into DiffSync models."""
        self.source_adapter = UniFiNautobotAdapter(job=self, sync=self.sync)
        self.source_adapter.load()

    def load_target_adapter(self):
        """Load data from UniFi into DiffSync models."""
        conn = connect_controller()
        self.target_adapter = UniFiAdapter(job=self, sync=self.sync, client=conn)
        self.target_adapter.load()

    def run(  # pylint: disable=arguments-differ, too-many-arguments
        self, dryrun, memory_profiling, debug, *args, **kwargs
    ):
        """Perform data synchronization."""
        self.debug = debug
        self.dryrun = dryrun
        self.memory_profiling = memory_profiling
        super().run(dryrun=self.dryrun, memory_profiling=self.memory_profiling, *args, **kwargs)


jobs = [UniFiDataSource, UniFiDataTarget]
register_jobs(*jobs)
