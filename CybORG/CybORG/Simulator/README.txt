Henry Tsui

---Host.py---

Host.py is an object that consists of attributes Entity, File, Interface, LocalGroup,  MSFServerSession, Process, Session and User

How it interacts is that Host.py is a class that simulates the internals of the "Host"
-> The constructor builds the host by calling on its child classes via add methods to create a new attribute within
the host.

Contains other functions such as disabling user, removes user from a group. Ability to start and stop a service.
*There is some error in the add_service(): functions

Able to create a backup of the current host and restore it if attacker is too established on host.

---SimulationController.py---

A parent class that controls the environment of the simulation.

*Inherits from environment controller.
*This class mainly parses the scenario file

Functionality allows the simulation controller to reset its environment
-> Also has pause, executions, restore, save, shutdown functions.

*Side note: Not entirely sure about get_true_state(self, info: dict) -> Observation:
 -> Getting the value of the current state of the targeted host?
 --> everything is visible in the state, per agent can't see the specific kind of information.
 --> In virtual environment, agent can't see it until they see it.

_parse_scenario(self, scenario_filepath: str, secnario_mod: dict = None):
takes input data and converts it to a data structure 

---State.py---

Simulates network state, contains data for simulated network, including ips, subnets, hosts

A class that contains attribute Host, Scenario, SessionType, Observation, Process, Session and Subnet

reset(): resets the state within the scenario and keeps a copy of the original time

_initialise_state(self, secnario: Scenario): 
contains...
mapping of subnet names to subnet cidrs
mapping of ip address to hostnames

mapping of hostnames to host objects
mapping of agent names to mapping of session id to session objects
mapping of subnet cidrs to subnet objects
mapping of agent name to number of sessions

Contains functionality...
that allows to add a session of a selected type to a dict as a selected user
adds file and adds user 
removes process from the state
getting session from the process id
rebooting to host

--User.py--
Constructs a User, given username, password and conditions if User is bruteforceable
Checks to see if the user is in a user group

How to implement actions?
There is a file called ActionSpace.py that defines parameters that only the agent is allowed to know

Within the Action folder, there are numerous sub-folders that allows actions to be implemented such as 
agent actions, abstract actions, concrete actions, global actions etc.