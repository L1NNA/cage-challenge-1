# Copyright DST Group. Licensed under the MIT license.
from CybORG.Emulator.Entity import Entity
import enum


class ServiceState(enum.Enum):
    """An enum for representing the different states of services. """
    UNKNOWN = enum.auto()
    OPEN = enum.auto()
    CLOSED = enum.auto()
    FILTERED = enum.auto() #used when unable to determine whether port is closed or filtered

    @classmethod
    def parse_string(cls, service_string):
        if service_string.lower() == "open":
            return cls.OPEN
        elif service_string.lower() == "closed":
            return cls.CLOSED
        elif service_string.lower() == "filtered":
            return cls.FILTERED
        else:
            return cls.UNKNOWN

    def __str__(self):
        return self.name


class ServiceVersion(enum.Enum):
    """An enum for representing the different versions of services. """
    UNKNOWN = enum.auto()
    OpenSSH7_6p1 = enum.auto()

    @classmethod
    def parse_string(cls, service_string):
        pass

    def __str__(self):
        return self.name


class StartupType(enum.Enum):
    """An enum for representing the different startup types of services. """

    @classmethod
    def parse_string(cls, service_string):
        pass

    def __str__(self):
        return self.name


class Service(Entity):
    def __init__():
        pass

    def get_state(self):
        pass