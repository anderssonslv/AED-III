import itertools
from time import time

def tsp_bruteforce(distances):
    execTime = time()
    print("Rodando bruteForce...")
    num_cities = len(distances)
    cities = list(range(num_cities))
    min_distance = float('inf')
    optimal_path = None

    for path in itertools.permutations(cities):
        distance = 0
        for i in range(num_cities - 1):
            distance += distances[path[i]][path[i+1]]
        distance += distances[path[-1]][path[0]]  # Volta para a cidade inicial

        if distance < min_distance:
            min_distance = distance
            optimal_path = path
    print(f"Concluido!\nCusto:{min_distance}\nCaminho:{optimal_path}")
    execTime -= time()
    print("Tempo = ",execTime)
    return min_distance, optimal_path

import numpy as np 

def getMatrixFromFile(file):
    with open(file) as matrixFile:
        matrix = np.loadtxt(matrixFile)
    return matrix

tsp_bruteforce(getMatrixFromFile("tsp3_1194.txt"))
