'''
Created on Feb 20, 2012

@author: yelkalay
'''
from filters import FilterStrategy
from pipes import Pipe

class FilterStopWords(FilterStrategy.FilterStrategy):
    '''
    A basic filter class that removes all stop words from a data stream. 
    '''

    def __init__(self,inputPipe,outputPipe,stopwordList):
        '''
        Constructor
        '''
        
        self.input = None
        self.inputPipe = inputPipe
        self.outputPipe = outputPipe
        self.stopwordList = stopwordList
    
    def getInput(self):
        self.input = self.inputPipe.pop()
    
    def filterInput(self):
        '''This filter operates as follows: 
        1. Get the input (a word) being filtered
        2. Compare it against a list of stopwords from the inputpipe
        3. Push the data onto the output pipe 
        '''
        self.getInput()
        if (self.input.lower() not in self.stopwordList and self.input.upper() not in self.stopwordList):
            self.outputData()
            
    
    def outputData(self):
        self.outputPipe.append(self.input)
    