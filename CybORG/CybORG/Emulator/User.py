# Copyright DST Group. Licensed under the MIT license.
import copy
import random
import string

from CybORG.Shared.Enums import PasswordHashType
from CybORG.Emulator.Entity import Entity
from CybORG.Emulator.LocalGroup import LocalGroup


class User(Entity):
    def __init__(self):
        pass

    def get_state(self):
        pass

    def add_group(self, group: LocalGroup):
        if self.groups is None:
            self.groups = [group]
        else:
            self.groups.append(group)

    def disable_user(self):
        self.disabled = True
        return True

    def __str__(self):
        return f'{self.username}'