'''
BUBBLE SORT
COMPLEXITAT: O(n²)
'''

import sys
import os

sys.path.append(os.path.abspath('/home/mrt/ordenacioMusica/AlgoOrdMusica'))

from serie import llista;

def bubble_sort():
    n = len(llista)

    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if llista[j] > llista[j+1]:
                llista[j], llista[j+1] = llista[j+1], llista[j]
                swapped = True
        if not swapped:
            break

    return llista;