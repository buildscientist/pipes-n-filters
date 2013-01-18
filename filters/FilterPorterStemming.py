'''
Created on Feb 23, 2012

@author: yelkalay
'''

from filters import FilterStrategy
from stemming import Porters

class FilterPorterStemming(FilterStrategy.FilterStrategy):
    '''
    A basic filter class that utilizes Vivake Gupta's Python implementation of 
    Porter's stemming algorithm. 
    '''


    def __init__(self,inputPipe,outputPipe):
        '''
        Constructor
        '''
        self.input = None
        self.inputPipe = inputPipe
        self.outputPipe = outputPipe
        
    def getInput(self):
        self.input = self.inputPipe.pop()

    def filterInput(self):
        '''This filter operates as follows: 
        1. Get the input (a word) being filtered
        2. Apply Porter's Stemming algorithm to it
        3. Push the data onto the output pipe '''
        self.getInput()
        stemmer = Porters.PorterStemmer()
        output = stemmer.stem(self.input, 0, len(self.input) - 1)
        self.input = output
        self.outputData()
    
    def outputData(self):
        self.outputPipe.append(self.input)

        