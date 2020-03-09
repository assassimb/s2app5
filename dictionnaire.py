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

def lireFichier(stringEntree, enleverPONC):
    
    f = open(stringEntree, 'r', encoding = "utf8")
    #print(f)
    data = f.read()
    words = data.split()
    f.close()
    
    if enleverPONC is True:
        # for raw_word in words:
        #     words = raw_word.strip(PONC)
        words = unwanted_chars(words)
    
    #print(words)
    return words

def unwanted_chars(liste):
    PONC = ["!", '"', "'", ")", "(", ",", ".", ";", ":", "?", "-", "_","—", "«"]
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
    #print(RetourListe)
    return RetourListe 

def modeUnigramme(words):

    dictionnaire = dict()

    for word in words:
        if word not in words:
            words[word] = 0 
        words[word] += 1
        
    print("Frequence par mots : ")
    print(len(sortFreqDict(words)))
    for word in words.split():
        dictionnaire[i] = sortFreqDict(word)
        i = i + 1

    return dictionnaire

# def modeBigramme(dictionnaire):
#     graphMots = Graph()