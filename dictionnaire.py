import math
import argparse
import glob
import sys
import os
from pathlib import Path
from random import randint
from random import choice
from pythonds import Graph



def sortFreqDict(freqdict):
    
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def lireFichier(path, enleverPONC, PONC):
    
    f = open(path, 'r', encoding="utf8")
    data = f.read()
    words = data.split()
    f.close()
    
    if enleverPONC is True:
        for raw_word in words:
            words = raw_word.strip(PONC)
        
    return words

def modeUnigramme(words, dictionnaire, wordfreq):

    for word in words:
        if word not in wordfreq:
            wordfreq[word] = 0 
        wordfreq[word] += 1
        
    print("Frequence par mots : ")
    print(len(sortFreqDict(wordfreq)))
    return sortFreqDict(wordfreq)

def modeBigramme(dictionnaire):
    
    graphMots = Graph()    
    
    for i in range(len(dictionnaire) - 1):
        if graphMots.getVertex(dictionnaire[i]) is False:
            graphMots.addVertex(dictionnaire[i])
        graphMots.addEdge(str(dictionnaire[i]), str(dictionnaire[i+1]))
        
    print(graphMots.numVertices)
    return graphMots
    
    

        
        