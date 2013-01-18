'''
Created on Feb 20, 2012

@author: yelkalay
'''

class Pipe():
    '''
    Generic pipe class. Since Python is a loosely typed language we can basically setup a buffer
    without a specific type before runtime. We'll setup a buffer for the data source and sink. 
    Transfer methods (getters/setters) aren't necessary because Python 
    doesn't have any concept of access modifiers. Some argue that this breaks the encapsulation 
    portion of OO theory but I'll leave that to the purists/theorists. 
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.buffer = []
        