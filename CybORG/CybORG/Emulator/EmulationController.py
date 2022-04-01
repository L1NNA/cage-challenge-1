# Copyright DST Group. Licensed under the MIT license.
import copy
import inspect
from ipaddress import IPv4Network
from math import log2
from random import sample, choice
import yaml

from CybORG import CybORG
from CybORG.Shared.Actions import FindFlag, ShellSleep, SambaUsermapScript, UpgradeToMeterpreter, MSFEternalBlue, GetShell, \
    PingSweep
from CybORG.Shared.Actions.Action import Action
from CybORG.Shared.Enums import FileType, TrinaryEnum
from CybORG.Shared.EnvironmentController import EnvironmentController
from CybORG.Shared.Observation import Observation
from CybORG.Shared.Results import Results
from CybORG.Emulator.State import State


class EmulationController(EnvironmentController):
    """The class that controls the Emulation environment.
    Inherits from Environment Controller then implements emulation-specific functionality.
    Most methods are either disabled or delegate their functionality to the State attribute.
    The main thing this class currently does is parse the scenario file.
    """
    def __init__():
        pass

    def reset(self, agent=None):
        self.state.reset()
        self.hostname_ip_map = {h: ip for ip, h in self.state.ip_addresses.items()}
        self.subnet_cidr_map = self.state.subnet_name_to_cidr
        return super(EmulationController, self).reset(agent)

    def pause(self):
        pass

    def execute_action(self, action: Action) -> Observation:
        return action.sim_execute(self.state)

    def restore(self, file: str):
        pass

    def save(self, file: str):
        pass

    def get_true_state(self, info: dict) -> Observation:
        output = self.state.get_true_state(info)
        return output

    def shutdown(self, **kwargs):
        pass

    def _parse_scenario(self, scenario_filepath: str, scenario_mod: dict = None):
        pass

    def _create_environment(self):
        self.state = State(self.scenario)
        self.hostname_ip_map = {h: ip for ip, h in self.state.ip_addresses.items()}
        self.subnet_cidr_map = self.state.subnet_name_to_cidr

    def run_schtasks(self):
        for host in self.hosts:
            host.run_scheduled_tasks(self.step)

    def get_last_observation(self, agent):
        return self.observation[agent]