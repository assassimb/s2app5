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

def printDict(stringEntree, dictionnaire, wordfreq):
    
    i = 0
    j = 0

    f = open(stringEntree,'r', encoding="utf8")
    for line in f:
        for word in line.split():
            dictionnaire[i] = word
            i = i + 1
    f.close()

    totalfreq = len(dictionnaire)

    print("Dictionnaire : ")    
    print(len(dictionnaire)) 

    f = open(stringEntree, 'r', encoding="utf8")
    data = f.read()
    words = data.split()
    f.close()

    unwanted_chars = "!)(,.;:?-_"
    
    for raw_word in words:
        word = raw_word.strip(unwanted_chars)
        if word not in wordfreq:
            wordfreq[word] = 0 
        wordfreq[word] += 1         # wordfreq[word] ++ (le mot donne la position) wordfreq['yo'] nous donne la frequence 6
    
    # pourcfreq = []

    # for j in wordfreq:
    #     pourcfreq = ((wordfreq['yo'] * 100 ) / totalfreq)       # trouver une facon de passer au prochain mot dans le dictionnaire
    #     #j = j + 1
    
    # print(pourcfreq)
    print("Frequence par mots : ")
    print(len(sortFreqDict(wordfreq)))
    return sortFreqDict(wordfreq)