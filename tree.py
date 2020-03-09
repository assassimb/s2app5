import math
import argparse
import glob
import sys
import os
from pathlib import Path
from random import randint
from random import choice

stringEntree = "D:/coding/CODES/APP5/s2app5/TextesPourEtudiants"

#print(os.listdir("D:/coding/CODES/APP5/s2app5/TextesPourEtudiants"))

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
    print(Dict)

# def ouvrirFichier(stringEntree):
#     Dict = {}
#     i = 0

#     with open(stringEntree,'r') as f:
#         for line in f:
#             for word in line.split():
#                 Dict[i] = word
#                 i = i + 1
#     f.close()