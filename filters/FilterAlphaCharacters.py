'''
Created on Feb 23, 2012

@author: yelkalay
'''
import string
from filters import FilterStrategy
from pipes import Pipe

class FilterAlphaChars(FilterStrategy.FilterStrategy):
    '''
    A basic filter class that removes non alpha characters and sends them to /dev/null. 
    Alpha characters are passed on to the alpha character queue
    '''


    def __init__(self,inputPipe,outputPipe):
        '''
        Constructor
        '''
        self.input = None
        self.outputPipe = outputPipe
        self.inputPipe = inputPipe
    
    def getInput(self):
        self.input = self.inputPipe.pop()

    def filterInput(self):
        '''This filter operates as follows: 
        1. Get the input (a word) being filtered
        2. Check to see if it only contains alphabetical characters
        3. If it does push the data onto the output pipe 
        '''
        self.getInput()
        if (self.input.isalpha()):
            self.outputData()
        else:
            self.input.strip(string.punctuation)
            self.outputData()


    def outputData(self):
        self.outputPipe.append(self.input)

