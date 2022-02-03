# Copyright DST Group. Licensed under the MIT license.
from CybORG.Simulator.Session import Session
from CybORG.Simulator.Process import Process

# Starts a Metasploit Server session
# What is a Metasploit server?
# -> It is a tool used to probe systematic vulnerabilities on networks and servers.
# __init__(): Constructor for MSF Server session
# dead_child(self, child_id: int): checks with parent class, if matches with route, eliminates the child process
class MSFServerSession(Session):

    def __init__(self, ident: str, host: str, user: str, agent: str,
                 process: Process, timeout: int = 0, session_type: str = 'msf server', name=None):
        """
        :param ident: Identity verification
        :param host: host name
        :param user: user name
        :param agent: agent name
        :param process: process id
        :param timeout: timeout value at 0 (means there is no timeout)
        :param session_type: the type of session
        :param name: name of session
        """
        super().__init__(ident, host, user, agent,
                 process, timeout, session_type, name=name)
        self.routes = {}  # routes have the structure sessionid: subnet

    def dead_child(self, child_id: int):
        super().dead_child(child_id)
        if child_id in self.routes:
            self.routes.pop(child_id)
