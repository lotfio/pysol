#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     Pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

from src.core.Command import Command

class info(Command):

    def execute(self, sub = None, options = [], flags = []):

        # This method should execute our commands
        if(sub == 'hello'):
            self.hello()

        return self.output.writeLn(" Command help msg here ")

    def hello(self):

        print("hello from Pysol")