import math
import argparse
import glob
import sys
import os
from pathlib import Path
from random import randint
from random import choice

def ouvrirFichier(stringEntree):
    Dict = {}
    i = 0

    with open(stringEntree,'r') as f:
        for line in f:
            for word in line.split():
                Dict[i] = word
                i = i + 1
    f.close()
    return Dict

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def printDict(Dict):
    print("Dictionnaire : ") 
    print(Dict) 

    fp = open('test.txt')
    data = fp.read()
    words = data.split()
    fp.close()

    unwanted_chars = "!)(,.;:?-_"
    wordfreq = {}
    for raw_word in words:
        word = raw_word.strip(unwanted_chars)
        if word not in wordfreq:
            wordfreq[word] = 0 
        wordfreq[word] += 1

    print("Frequence par mots : ")
    print(wordfreq)
    print(sortFreqDict(wordfreq))
    
