# Copyright DST Group. Licensed under the MIT license.
from datetime import datetime

from CybORG.Shared.Enums import FileType, FileVersion
from CybORG.Emulator.Entity import Entity
from CybORG.Emulator.LocalGroup import LocalGroup
from CybORG.Emulator.User import User
import enum

# The File class creates an object file, the file path, different permissions(users, groups, default), time created, time modified and 
# indicates when it was last accessed and what version type is the file.
# 1. __init__(): creates object, file. Assigns paramters to attributes for given object
# 2. get_state(self): returns the dictionary obs

class File(Entity):
    def __init__():
       pass 

    def get_state(self):
        pass

    def check_executable(self): # Checks if the file is executable by a given user - assumes the user and file are on the same dict
        pass

    def check_readable(self): # Checks if the file is readable by a given user
        pass