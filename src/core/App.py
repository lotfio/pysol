'''
*| This file is part of cony
*|
*| @package     Pysol python cli application
*| @author      <lotfio lakehal>
*| @license     MIT
*| @version     0.1.0
*| @copyright   2019 lotfio lakehal
'''

from src.cfg.app import *

class App:

    def __init__(self, inp, output):
        ''' init '''

        self.input  = inp
        self.output = output

    def display_logo(self):
        '''
        + display app logo
        '''
        f = open(logo_file)
        self.output.writeLn(f.read())

    def display_basic_info(self):
        '''
        + display app basic info
        '''

        info = "\nwelcome to " + app_name + ' ' + app_version + ' by ' + app_author + '\n'

        self.output.writeLn(info)


    def run(self):
        '''
        + run application
        '''
        self.display_logo()
        self.display_basic_info()