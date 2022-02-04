Written By: Michael Kalpouzos, 20116078

The Scenario's information about how agents, subnets and hosts should work in specified scenarios 
are kept in yaml files. These files are loaded and parsed through for their information and the data
of the scenario are kept and stored. 

How will we specify a scenario for the emulation environment?
We would create a new yaml file or change the information inside the already existant yaml scenario 
file to specify whatever needs or changes that the scenario requires.

Scenario1.yaml & Scenario1b.yaml -
Located in the Scenarios Folder holds the information of the agents, hosts and subnets.
It contains what subnets the agents are allowed to use, its available actions, its agent
type, the type of reward calculator type, its starting sessions, wrappers, hostname, name, 
number of children sessions, the type and the username. These are two different scenarios
that can be used.

Scenario.py -
Located in the Shared Folder and acts as a dataclass that can access scenario
information from the yaml files. It acts as a wrapper class holding information
on the scenario's session, agents, and other needed scenario information.

ScenarioParser.py -
Located in the Shared Folder and is used to parse through and set variable to attributes
of the scenario. This file begins by loading and recorded the information from the specified 
yaml file. This file checks to make sure the inputs/data are correct. It finds available actions
and images, the name of the scenario, the subnets, the hosts, the flags, red's actions and the
open-source intellegence. After retrieving all this information, it is returned to the program.

scenario_parser.py -
This file is very similar to the ScenarioParser.py file. The file loads the contents of the yaml
file and parses through the yaml file retieving the host names, subnet names and agent names.
The python file then parses through every host, subnet and agent. The main function
in the file parses through both Scenario1.yaml and Scenario1b.yaml files.

DataGatherer.py - 
This file gathers the needed data and checks to make sure the data collected is correct and would
work.
