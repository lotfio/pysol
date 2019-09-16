#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     Pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

class info:

    description = 'This command displays app information'

    def __init__(self, inp, out):
        self.inp = inp
        self.out = out

    def execute(self, sub = None, options = [], flags = []):

        # This method should execute our commands
        if(sub == 'hello'):
            return self.hello()

        return self.help()

    def hello(self):

        print("\n hello from Pysol")


    def help(self):

        hp  = "\n [ info command ] \n\n"
        hp += "  - This command helps you to get information about Pysol\n"

        return self.out.writeLn(hp)