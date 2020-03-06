import math
import argparse
import glob
import sys
import os
from pythonds.graphs import Graph
from contextlib import ExitStack

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='S2-APP5i Labo1:Exercice1.py')
    parser.add_argument('-f', required=True,
                        help='Fichier contenant la liste de mots')
    parser.add_argument('-m', required=True, help='Mot de départ')
    parser.add_argument('-d', required=True, help='Distance du mot de départ')
    parser.add_argument('-v', action='store_true', help='Mode verbose')
    args = parser.parse_args()

# Si mode verbose, refléter les valeurs des paramètres passés sur la ligne de commande
    if args.v:
        print("Mode verbose:")
        print("Fichier de mots utilisé: " + args.f)
        print("Mot de départ: " + args.m)
        print("Distance du mot de départ: " + args.d)


#
# Début du code
#

def lirecode():
    mot = args.m
    Graph = buildGraph(args.f)

    depart = Graph.getVertex(mot)

    if depart == None:
        print("Entree hors du dictionnaire")
        exit()
    buff = [depart]

    noeudsVisites = set()
    noeudsVisites.add(depart.id)

    for d in range(int(args.d)):
        print("Distance: ", d+1)
        connections = []
        
        for noeud in buff:
            connections += noeud.getConnections()
            
        for noeud in connections:
            if noeud.id not in noeudsVisites:
                print(noeud.id)
                noeudsVisites.add(noeud.id)
        buff = connections

with ExitStack() as Stack:
    files = [Stack.enter_context(open(args.f))]
lirecode()