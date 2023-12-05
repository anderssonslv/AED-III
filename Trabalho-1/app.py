import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from time import time
from genetic import geneticAlgorithm

from algoritms.branchAndBound import tsp_branch_and_bound
from algoritms.bruteForce import tsp_bruteforce

def getMatrixFromFile(file):
    try:
        with open(file, "r") as info:
            matrix = np.loadtxt(info)
    except FileNotFoundError:
        print("Arquivo 'matriz.txt' não encontrado.")
    return matrix

def compairAlgorithm(file, runExact):
    matrix = getMatrixFromFile(file)
    target = re.search(r'_(\d+)\.', file)
    target = target.group(1)
    begin = time()
    totalCostAproximate = geneticAlgorithm(matrix)
    executeTimeAproximate = time() - begin
    
    totalCostExact = 0
    executeTimeExact = 0
    
    if runExact:
        begin = time()
        
        
    
    fileName = re.search(r'/(.*?)\.', file)
    fileName = fileName.group(1)
    return fileName, target,totalCostAproximate, formatTime(executeTimeAproximate), totalCostExact, formatTime(executeTimeExact)

def formatTime(time):
    
    mins = int(time // 60)
    sec = int(time % 60)
    
    return f'{mins}m {sec}s'  

matrixFiles = (('tsp_data/tsp1_253.txt', False),
               ('tsp_data/tsp2_1248.txt', True),
               ('tsp_data/tsp3_1194.txt', False),
               ('tsp_data/tsp4_7013.txt', False),
               ('tsp_data/tsp5_27603.txt', False))

results = []

for file, runExact in matrixFiles:
    results.append(compairAlgorithm(file, runExact))

resultsTable = pd.DataFrame(results, columns=['Arquivo', 'Custo Ótimo', 'Custo\nGenético', 'Tempo de execução\nGenético', 'Custo exato', 'Tempo de execução\nexato'])

fig, ax = plt.subplots(figsize=(10, 5))
#ax.axis('tight')
ax.axis('off')
imgTable = ax.table(cellText=resultsTable.values, colLabels=resultsTable.columns, cellLoc='center', loc='center', bbox=[-0.3, 0, 1.2, 1])
imgTable.auto_set_font_size(False)
imgTable.set_fontsize(10)
imgTable.scale(1, 2)

plt.savefig('algorithmsCompair.png', dpi=200, bbox_inches='tight')
plt.show()