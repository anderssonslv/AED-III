import itertools
from time import time
import numpy as np

def held_karp(dists):
    n = len(dists)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)

    return opt, list(reversed(path))

def getMatrixFromFile(file):
    with open(file) as matrixFile:
        matrix = np.loadtxt(matrixFile)
    return matrix

def formatTime(time):
    mins = int(time // 60)
    sec = int(time % 60)
    return f'{mins}m {sec}s'

print("Rodando Held Karp")
print("\n==============TSP_2===============\n")
execTime = time()
cost, path = held_karp(getMatrixFromFile("tsp2_1248.txt"))
execTime -= time()
print("Custo = ",cost)
print("Caminho = ",path)
print("Tempo = ",abs(execTime),"\n > ",formatTime(abs(execTime)))

print("\n==============TSP_1===============\n")
execTime = time()
cost, path = held_karp(getMatrixFromFile("tsp1_253.txt"))
execTime -= time()
print("Custo = ",cost)
print("Caminho = ",path)
print("Tempo = ",abs(execTime),"\n > ",formatTime(abs(execTime)))

print("\n==============TSP_3===============\n")
execTime = time()
cost, path = held_karp(getMatrixFromFile("tsp3_1194.txt"))
execTime -= time()
print("Custo = ",cost)
print("Caminho = ",path)
print("Tempo = ",abs(execTime),"\n > ",formatTime(abs(execTime)))

print("\n==============TSP_5===============\n")
execTime = time()
cost, path = held_karp(getMatrixFromFile("tsp5_27603.txt"))
execTime -= time()
print("Custo = ",cost)
print("Caminho = ",path)
print("Tempo = ",abs(execTime),"\n > ",formatTime(abs(execTime)))

print("\n==============TSP_4===============\n")
execTime = time()
cost, path = held_karp(getMatrixFromFile("tsp4_7013.txt"))
execTime -= time()
print("Custo = ",cost)
print("Caminho = ",path)
print("Tempo = ",abs(execTime),"\n > ",formatTime(abs(execTime)))

