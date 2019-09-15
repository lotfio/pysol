'''
*| This file is part of cony
*|
*| @package     Pysol python cli application
*| @author      <lotfio lakehal>
*| @license     MIT
*| @version     0.1.0
*| @copyright   2019 lotfio lakehal
'''

import sys

class Output:
    '''
    * input class
    '''

    def __init__(self):
        '''
        init
        '''
        pass

    def writeLn(self, line = ''):
        return sys.stdout.write(line)