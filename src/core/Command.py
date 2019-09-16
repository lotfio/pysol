#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     Pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

import glob, os
from src.cfg.app import root
from src.core.helpers import load_module

class Command:

    # @var available commands
    avail_commands = {}

    def no_sub_command(self):
        return print("\n no sub command !")



    def available_commands(self):

        print("\nAvailable commands :\n")
        os.chdir(root + "/commands/")

        for file in glob.glob("*.py"):

            f = file.split(".")[0]
            m = load_module("src.commands."+f)
            c = getattr(m, f)
            self.avail_commands[f] = c.description

        ## tallest command
        t = len(max(self.avail_commands, key=len))

        for com in self.avail_commands:

           print( " "+com + ((t - len(com) + 18) * ' ') + self.avail_commands[com])

