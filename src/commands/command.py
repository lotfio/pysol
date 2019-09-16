#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     Pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

from src.core.Command import Command as baseCommand

class command(baseCommand):

    # comand description
    description = 'This command helps you to create, delete and update commands'

    # execute method
    # this method is where your sub commands and flags should be
    # executed
    def execute(self, sub = None, options = [], flags = []):

        # This method should execute our commands
        if(sub):
            if(sub == 'make'):
                return self.make()
            else:
                return self.no_sub_command(sub)
        else:
            pass
        return self.help()


    # this is hello test method
    def make(self):
        print("\n hello from Pysol")


    def help(self):

        hp  = "\n [ command ] \n\n"
        hp += "  - This command helps you to add commands to Pysol\n"

        return self.out.writeLn(hp)