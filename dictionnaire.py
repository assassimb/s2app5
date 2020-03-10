import math
import argparse
import glob
import sys
import os
import pprint
from pathlib import Path
from random import randint
from random import choice
from pythonds import Graph

def sortFreqDict(freqdict):
    
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def lireFichier(path):
    
    f = open(path, 'r', encoding="utf8")
    data = f.read()
    words = data.split()
    f.close()

    data = unwanted_chars(data)
            
    return words

def unwanted_chars(string):
    PONC = ["!", '"', "'", ")", "(", ",", ".", ";", ":", "?", "-", "_","—", "«"]
    RetourListe = []
    NewListe = string.split()
    for word in NewListe:
        for signe in PONC:
            word = word.replace(signe, " ")
        word = word.replace("\n", " ")
        word = word.lstrip()
        word = word.rstrip()
    if len(word) > 2:
        RetourListe.append(word)
    return RetourListe 


def modeUnigramme(words):
    wordfreq = {}
    occurence = 0
    for word in words:
        if word not in wordfreq:
            wordfreq[word] = 0 
        wordfreq[word] += 1
        
    print("Frequence par mots : ")
    print(len(sortFreqDict(wordfreq)))
    return sortFreqDict(wordfreq)

def modeBigramme(dictionnaire):
    
    graphMots = Graph(connections, directed = True)    
    
    for i in range(len(dictionnaire) - 1):
        if graphMots.getVertex(dictionnaire[i]) is False:
            graphMots.addVertex(dictionnaire[i])
        graphMots.addEdge((dictionnaire[i]), (dictionnaire[i+1]))
        
    print(graphMots.numVertices)
    
    return graphMots
    
def comparaisonTexteUnigramme(dictionnaire, path):
    
    listeDeFreqUnitaire = []
    
    for key in dictionnaire:
        listeDeFreqUnitaire.append(float(key[0])/100, key[1])
        

        
        