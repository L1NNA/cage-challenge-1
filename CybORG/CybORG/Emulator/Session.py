## The following code contains work of the United States Government and is not subject to domestic copyright protection under 17 USC § 105.
## Additionally, we waive copyright and related rights in the utilized code worldwide through the CC0 1.0 Universal public domain dedication.
from ipaddress import IPv4Address

from CybORG.Shared.Enums import SessionType, OperatingSystemType
from CybORG.Emulator.Entity import Entity


class Session(Entity):

    def __init__(self):
        pass

    def get_state(self):
        pass

    def set_orphan(self):
        pass

    def dead_child(self, child_id: int):
        self.children.pop(child_id)


class RedAbstractSession(Session):
    # a session that remembers previously seen information that can be used by actions
    def __init__(self):
        pass

    def addport(self):
        pass

    def addos(self, hostname: str, os: OperatingSystemType):
        self.operating_system[hostname] = os

class GreenAbstractSession(Session):
    # Currently a clone of RedAbstractSession
    # a session that remembers previously seen information that can be used by actions
    def __init__(self):
        pass

    def addport(self):
        pass

    def addos(self, hostname: str, os: OperatingSystemType):
        self.operating_system[hostname] = os

class VelociraptorServer(Session):
    # a session that remembers previously seen information that can be used by actions
    def __init__(self):
        pass

    def add_sus_pids(self):
        pass