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
    for fil in os.listdir(stringEntree):
        f = open(stringEntree + fil, 'r', encoding = "utf8")
        for line in stringEntree:
            for word in line.split():
                Dict[i] = word
                i = i + 1
    f.close()
    #print(Dict)
    return Dict

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def unwanted_chars(liste):
    PONC = ["!", '"', "'", ")", "(", ",", ".", ";", ":", "?", "-", "_","—"]
    RetourListe = []
    NewListe = liste.split()
    for word in NewListe:
        for signe in PONC:
            word = word.replace(signe, " ")
        word = word.replace("\n", " ")
        word = word.lstrip()
        word = word.rstrip()
    if len(word) > 2:
        RetourListe.append(word)
    print(RetourListe)
    return RetourListe 

def printDict(stringEntree, dictionnaire, wordfreq):
    
    i = 0
    j = 0

    # f = open(stringEntree,'r', encoding="utf8")
    # for line in f:
    #     for word in line.split():
    #         dictionnaire[i] = word
    #         i = i + 1
    # f.close()

    dictionnaire = ouvrirFichier(stringEntree)

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

def Comparer(self, path, mode):

    temp = []
    f = open(path, 'r', encoding = ("utf8"))
    for lines in f:
        temp = self.unwanted_chars(lines)
        #if mode == 2:
        
