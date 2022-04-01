## The following code contains work of the United States Government and is not subject to domestic copyright protection under 17 USC § 105.
## Additionally, we waive copyright and related rights in the utilized code worldwide through the CC0 1.0 Universal public domain dedication.
import copy
from ipaddress import IPv4Address
from typing import List, Optional

from CybORG.Shared.Enums import (ProcessType, ProcessVersion,
        TransportProtocol, DecoyType)
from CybORG.Emulator.Entity import Entity
from CybORG.Emulator.User import User

# Creates a process within the simulation
# __init__(): Constructor for Process object, creates attributes for object.
class Process(Entity):
    def __init__(self, process_name: str, pid: int, parent_pid: int, username: str, program_name: str = None,
                 path: str = None, open_ports: list = None, process_type: str = None, process_version: str = None,
                 decoy_type: DecoyType = DecoyType.NONE, properties: List[str] = None):
        """
        :param process_name: name of process
        :param pid: id of process
        :param parent_pid: id of parent of process
        :param program_name: program the process is running
        :param username: the user runnning the process
        :param path: the path of the program the process is running
        :param open_ports: listening ports of structure [{Port: int, Address: str, Application Protocol: str}, ...]
        :param process_type: the type of process
        :param process_version: the version of the process
        :param decoy_type: which red actions are prevented despite appearing vulnerable
        :param properties: properties of the process to specify configuration details such as RFI presence
        """
        pass

    def get_state(self):
        pass

    def __str__(self):
        return f'{self.name}: {self.pid} <- {self.ppid}'