'''
Created on Feb 20, 2012

@author: Youssuf ElKalay
@version: 1.0
'''

class FilterStrategy(object):
    '''
    Abstract Filter class. Python doesn't have interfaces like 
    other modern OO programming languages like Java or C# because 'everything' is an object
    but we can mock an interface by throwing a not implemented exception and having other classes
    inherit from this mock interface. We'll use the strategy pattern here since we will want to have
    a variety of strategies for all filter methods abstracted below. 
    '''
    def getInput(self):
        raise NotImplementedError

    def filterInput(self):
        raise NotImplementedError
    
    def outputData(self):
        raise NotImplementedError
