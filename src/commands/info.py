#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     Pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal
from src.core.Command import Command as baseCommand

class info(baseCommand):
    #command description
    description = 'This command displays app information'

    # execute method
    # this method is where your sub commands and flags should be
    # executed
    def execute(self, sub = None, options = [], flags = []):

        # This method should execute our commands
        if(sub == 'hello'):
            return self.hello()

        return self.help()

    # test hello method
    def hello(self):

        print("\n hello from Pysol")


    # help method
    # this method will display this comand help
    def help(self):

        hp  = "\n [ info command ] \n\n"
        hp += "  - This command helps you to get information about Pysol\n"

        return self.out.writeLn(hp)