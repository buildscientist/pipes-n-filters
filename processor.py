'''
SE480 Assignment 3
@author: Youssuf ElKalay
@version: 1.0
'''
import argparse
import profile
from filters import FilterAlphaCharacters
from filters import FilterPorterStemming
from filters import FilterStopWords
from pipes import Pipe
from datasink import DataSink

'''Main/Driver that executes everything in the application. Provides an argument parser for the
command line interface. 
 '''

def main():
    'Setup the argument parser'
    parser = argparse.ArgumentParser("description='processor.py'")
    parser.add_argument('--data-source',dest='datasource',type=argparse.FileType('r'),help='The data source to process')
    args = parser.parse_args()
    
    if (args.datasource is None):
        parser.print_usage()
        exit(1)
    
    'Load the stop words into a buffer and populate a stopwords list'    
    fs = open('resources/stopwords.txt','r')
    buffer = fs.readlines()
    stopWordsList = []
    for word in buffer:
        'Remove the trailing newline character and add it to a stop words list'
        '*sigh* I miss perl chomp()'
        word = word.rstrip('\n')
        stopWordsList.append(word)
    fs.close()
     
    'Create a list of words from data source'
    datasourceLines = args.datasource.readlines()
    wordList = []
    for line in datasourceLines:
        for word in line.split(" "):
            wordList.append(word.rstrip('\n'))
     
    'Setup my pipes'
    datasourcePipe = Pipe.Pipe()
    datasourcePipe.buffer = wordList
    alphaCharacterPipe = Pipe.Pipe()
    stopwordPipe = Pipe.Pipe()
    datasinkPipe= Pipe.Pipe()
    
    'Setup my filters'    
    alphaCharFilter = FilterAlphaCharacters.FilterAlphaChars(datasourcePipe.buffer,alphaCharacterPipe.buffer)
    stopWordFilter = FilterStopWords.FilterStopWords(alphaCharacterPipe.buffer,stopwordPipe.buffer,stopWordsList)
    stemmingFilter = FilterPorterStemming.FilterPorterStemming(stopwordPipe.buffer,datasinkPipe.buffer)

    'Setup my datasink'
    datasink = DataSink.DataSink(datasinkPipe.buffer)
    
    
    'Run the wordlist through the filters'
    for process in range(len(datasourcePipe.buffer)):
        alphaCharFilter.filterInput()
        
    for processTwo in range(len(alphaCharacterPipe.buffer)):
        stopWordFilter.filterInput()
    
    for processThree in range(len(stopwordPipe.buffer)):
        stemmingFilter.filterInput()

    'Have the DataSink do its word frequency count'
    datasink.computeWordFrequency()
    datasink.printWordFrequency()
    


    
    
    
if __name__ == '__main__':
    main()