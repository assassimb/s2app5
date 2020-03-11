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
from collections import defaultdict



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

    words = unwanted_chars(data)
     
    return words



def unwanted_chars(string):
    PONC = ["!", '"', "'", ")", "(", ",", ".", ";", ":", "?", "-", "_","—", "«", "»", "[", "]"]
    RetourListe = []
    NewListe = string.split()
    for word in NewListe:
        for signe in PONC:
            word = word.replace(signe, " ")
        word = word.replace("\n", " ")
        word = word.replace("-", " ")
        word = word.lstrip()
        word = word.rstrip()
        
        if " " in word:
            wordsplit = word.split()
            if len(wordsplit[0]) > 2:
                RetourListe.append(wordsplit[0].lower())
            if len(wordsplit[1]) > 2:
                RetourListe.append(wordsplit[1].lower())
                
        if len(word) > 2 and " " not in word:
            RetourListe.append(word.lower())

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
    
    listeMotsOrdonnes = []
    listeMotsParFreq = []
    dictionnaireBigramme = {}
    dictionnaireFreqBigramme = {}
    
    listeMotsOrdonnes.append(dictionnaire[0])
    for i in range(len(dictionnaire)- 1):
        listeMotsOrdonnes.append(dictionnaire[i+1])
        dictionnaireBigramme[i] = listeMotsOrdonnes[i] + " " + listeMotsOrdonnes[i+1]
    
    for i in range(len(dictionnaireBigramme)):
        if dictionnaireBigramme[i] not in dictionnaireFreqBigramme:
            dictionnaireFreqBigramme[dictionnaireBigramme[i]] = 0
        dictionnaireFreqBigramme[dictionnaireBigramme[i]] += 1
    
    listeMotsParFreq = sortFreqDict(dictionnaireFreqBigramme)
    
    return listeMotsParFreq


    
def comparaisonTexteUnigramme(listemots, path):
    texteInconnu = []
    frequence = 0.0
    dictionnaire ={}
    
    for i in range(len(listemots)):
        if listemots[i][1] not in dictionnaire:
            dictionnaire[listemots[i][1]] = listemots[i][0]
    
    texteInconnu = lireFichier(path)
    
    nbMotsDict = 0
    for i in range(len(listemots)):
        nbMotsDict += listemots[i][0]
    nbMotsInconnu = len(texteInconnu)
        
    listeDeMotsUnitaire = []
    listeDeFreqDictionnaire = []
    
    for i in range(len(texteInconnu)):
        if texteInconnu[i] in dictionnaire:
            listeDeMotsUnitaire.append(texteInconnu[i])
            listeDeFreqDictionnaire.append(dictionnaire[texteInconnu[i]] / nbMotsDict * 100)
        else:
            listeDeMotsUnitaire.append(texteInconnu[i])
            listeDeFreqDictionnaire.append(0)
    

    listeFREQ = [(listeDeFreqDictionnaire[i], listeDeMotsUnitaire[i], 1 / nbMotsInconnu * 100) for i in range(len(listeDeFreqDictionnaire))]
    listeFREQ.sort()
    listeFREQ.reverse()
    
    for i in range(len(listeFREQ)):
        frequence = frequence + (float(listeFREQ[i][0] - listeFREQ[i][2])**2)
    frequence **= 0.5    
    
    return frequence



def comparaisonTexteBigramme(listemots, path):
    texteInconnu = []
    frequence = 0.0
    dictionnaire ={}
    
    for i in range(len(listemots)):
        if listemots[i][1] not in dictionnaire:
            dictionnaire[listemots[i][1]] = listemots[i][0]
    
    texteInconnu = lireFichier(path)
    
    nbMotsDict = 0
    for i in range(len(listemots)):
        nbMotsDict += listemots[i][0]

        
    listeDeMotsBinaire = []
    listeDeFreqDictionnaire = []
    
    for i in range(len(texteInconnu) - 1):
        if (texteInconnu[i] + " " + texteInconnu[i + 1]) in dictionnaire:
            listeDeMotsBinaire.append(str(texteInconnu[i] + " " + texteInconnu[i+1]))
            listeDeFreqDictionnaire.append(dictionnaire[texteInconnu[i] + " " + texteInconnu[i+1]] / nbMotsDict * 100)
        else:
            listeDeMotsBinaire.append(str(texteInconnu[i] + " " + texteInconnu[i+1]))
            listeDeFreqDictionnaire.append(0)

    nbMotsInconnu = len(listeDeMotsBinaire)
    
    listeFREQ = [(listeDeFreqDictionnaire[i], listeDeMotsBinaire[i], 1 / nbMotsInconnu * 100) for i in range(len(listeDeFreqDictionnaire))]
    listeFREQ.sort()
    listeFREQ.reverse()
    
    for i in range(len(listeFREQ)):
        frequence = frequence + (float(listeFREQ[i][0] - listeFREQ[i][2])**2)
    frequence **= 0.5    
    
    return frequence
    
    
            
        
        

        
        