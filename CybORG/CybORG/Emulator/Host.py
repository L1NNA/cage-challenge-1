## The following code contains work of the United States Government and is not subject to domestic copyright protection under 17 USC § 105.
## Additionally, we waive copyright and related rights in the utilized code worldwide through the CC0 1.0 Universal public domain dedication.
import hashlib
from copy import deepcopy
from datetime import datetime

from ipaddress import IPv4Network, IPv4Address
from random import randrange
from typing import Optional, List

from CybORG.Shared.Enums import (
        SessionType, OperatingSystemPatch, OperatingSystemKernelVersion,
        OperatingSystemVersion, DecoyType,
        OperatingSystemDistribution, OperatingSystemType
        )

from CybORG.Emulator.Entity import Entity
from CybORG.Emulator.File import File
from CybORG.Emulator.Interface import Interface
from CybORG.Emulator.LocalGroup import LocalGroup
from CybORG.Emulator.MSFServerSession import MSFServerSession
from CybORG.Emulator.Process import Process
from CybORG.Emulator.Session import VelociraptorServer, RedAbstractSession, Session

from CybORG.Emulator.User import User


class Host(Entity):
    """Emulator a host.
    This class simulates the internals of a host, including files, processes and interfaces.
    The methods are used to change the state of the host.
    """

    def __init__(self):
        pass

    def get_state(self):
        observation = {"os_type": self.os_type, "os_distribution": self.distribution, "os_version": self.version,
                       "os_patches": self.patches, "os_kernel": self.kernel, "hostname": self.hostname,
                       "architecture": self.architecture}
        return observation

    def get_ephemeral_port(self):
        port = randrange(49152, 60000)
        if port in self.ephemeral_ports:
            port = randrange(49152, 60000)
        self.ephemeral_ports.append(port)
        return port

    def add_session(self):
        pass

    def add_process(self):
        pass

    def add_file(self):
        pass

    def add_user(self, username: str, password: str = None, password_hash_type: str = None):
        pass

    def get_user(self, username):
        pass

    def get_interface(self, name=None, cidr=None, ip_address=None, subnet_name=None):
        """A method to get an interface with a selected name, subnet, or IP Address"""
        pass

    def get_process(self, pid):
        pass

    def get_file(self):
        pass

    def disable_user(self, username):
        user = self.get_user(username)
        if user is not None:
            return user.disable_user()
        else:
            return False

    def remove_user_group(self, user, group):
        user = self.get_user(user)
        if user is not None:
            return True
        return False

    def start_service(self, service_name: str):
        """starts a stopped service, no effect if service already started"""
        pass

    def stop_service(self, service_name: str):
        """stops a started service, no effect if service already stopped"""
        pass

    def add_service(self, service_name: str, process: int, session=None):
        pass

    def create_backup(self):
        pass

    def restore(self):
        pass

    def __str__(self):
        pass