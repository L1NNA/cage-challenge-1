Outlines of python Classes and files for emulation

Agents:
They are implementation-agonstic so they can be ignored

EmulationController.py
File.py
Host.py
class Host - Simulates a host #Methods changes the state of the host

     def __init__(params): #Initializes the class and builds the iternals of the host, including files, processes and interfaces.
     
     def add_session():
     
     def add_process():

     def get_process():
     
     def get_interface():

     def start_service():

     def stop_service():

     def add_service():  #incomplete code, hence code within is removed

     def create_backup(self):

     def restore(self):   #unsure about these 2 methods, can easily be removed for implementation for emulation

Interface.py
Process.py
class Process 

     def __init__(self, process_name: str, pid: int, parent_pid: int, username: str, program_name: str = None,
                 path: str = None, open_ports: list = None, process_type: str = None, process_version: str = None,
                 decoy_type: DecoyType = DecoyType.NONE, properties: List[str] = None):

     def get_state(self):
         pass

     def _parse_scenario(self, scenario_filepath: str, scenario_mod: dict = None):
         pass

Service.py
Session.py
class RedAbstractSession
class GreenAbstractSession
class VelociraptorServer

State.py
class State

     def get_true_state(self, info: dict) -> Observation:
     
     def _initialise_state(self, scenario: Scenario):
     
     def remove_process(self, hostname: str, pid: int):

     def get_session_from_pid(self, hostname, pid):
     
     def reboot_host(self, hostname):

     def stop_service(self):

     def start_service(self):


User.py
class User

     def get_state(self):

Functions left alone:
LocalGroup.py
MSFServerSession.py
Subnet.py








  
 
