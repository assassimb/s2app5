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

def lireFichier(stringEntree, enleverPONC, PONC):
    
    f = open(stringEntree, 'r', encoding="utf8")
    data = f.read()
    words = data.split()
    f.close()
    
    if enleverPONC is True:
        for raw_word in words:
            word = raw_word.strip(PONC)
        
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
    
