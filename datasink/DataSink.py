'''
Created on Feb 20, 2012

@author: yelkalay
'''
from collections import Counter

class DataSink():
    '''
    The DataSink acts as a final data bag/buffer where filtered words are stored. The class uses
    the very powerful Counter collection data type in Python to keep track of words and their
    respective counts. A counter is implemented as an extended dictionary (key/value pairs) with words 
    as the keys and their frequency as the value. 
    See http://docs.python.org/library/collections.html#counter-objects for more information on Counters. 
    '''

    def __init__(self,inputPipe):
        '''
        Constructor
        '''
        self.buffer = inputPipe
        self.counter = None
        self.commonTermCount = 20
    
    def computeWordFrequency(self):
        self.counter = Counter(self.buffer)
        
    
    def printWordFrequency(self):
        ''' 
        Counter.most_common() returns a list of tuples. Each tuple contains two values (word,frequency). 
        '''
        for wordCountPair in self.counter.most_common(self.commonTermCount):
            print "Word:" + wordCountPair[0] + " Count:" + str(wordCountPair[1]) 