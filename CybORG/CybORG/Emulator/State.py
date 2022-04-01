## The following code contains work of the United States Government and is not subject to domestic copyright protection under 17 USC § 105.
## Additionally, we waive copyright and related rights in the utilized code worldwide through the CC0 1.0 Universal public domain dedication.
import copy
from datetime import datetime, timedelta
from ipaddress import IPv4Network, IPv4Address
from math import log2
from random import sample, choice

from CybORG.Shared import Scenario
from CybORG.Shared.Enums import SessionType
from CybORG.Shared.Observation import Observation
from CybORG.Emulator.Host import Host
from CybORG.Emulator.Process import Process
from CybORG.Emulator.Session import Session
from CybORG.Emulator.Subnet import Subnet


class State:
    """Emulates the Network State.
    This class contains all the data for the simulated network, including ips, subnets, hosts and sessions.
    The methods mostly modify the network state, but tend to delegate most of the work to the Host class.
    """
    def __init__(self):
        pass

    def get_true_state(self, info: dict) -> Observation:
        pass

    def reset(self):
        pass

    def _initialise_state(self, scenario: Scenario):
        pass

    def add_session(self):
        """Adds a session of a selected type to a dict as a selected user"""
        pass

    def add_file(self):
        pass

    def add_user(self):
        pass

    def remove_process(self, hostname: str, pid: int):
        pass

    def get_session_from_pid(self, hostname, pid):
        pass

    def reboot_host(self, hostname):
        pass

    def stop_service(self, hostname: str, service_name: str):
        # stops a service, its process, and associated sessions
        pass

    def start_service(self, hostname: str, service_name: str):
        pass

    def get_subnet_containing_ip_address(self, ip_address: IPv4Address) -> Subnet:
        pass