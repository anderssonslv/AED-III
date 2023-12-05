import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from time import time
from algoritms.exact.branchAndBound import tsp_branch_and_bound
from algoritms.exact.bruteForce import tsp_bruteforce
from algoritms.prox.genetic import geneticAlgorithm

def getMatrixFromFile(file):
    with open(file) as matrixFile:
        matrix = np.loadtxt(matrixFile)
    return matrix

def formatTime(time):
    mins = int(time // 60)
    sec = int(time % 60)
    return f'{mins}m {sec}s'


def makeGraph(resultsTable):
    fig, ax = plt.subplots(figsize=(10, 5))
    #ax.axis('tight')
    ax.axis('off')
    imgTable = ax.table(cellText=resultsTable.values, colLabels=resultsTable.columns, cellLoc='center', loc='center', bbox=[-0.15, 0, 1.2, 1])
    imgTable.auto_set_font_size(False)
    imgTable.set_fontsize(10)
    imgTable.scale(1, 2)
    return fig

EXACT = False # Rodar exatos ou aproximativos

def compairAlgorithm(file, runTest):
    matrix = getMatrixFromFile(file)
    target = re.search(r'_(\d+)\.', file)
    target = target.group(1)

    totalCost = 0
    executeTime = time()

    if EXACT:
        if runTest:
            totalCost, pathExat = tsp_branch_and_bound(matrix)
    else: totalCost = geneticAlgorithm(matrix)
    executeTime = time() - executeTime
    
    fileName = re.search(r'/(.*?)\.', file)
    fileName = fileName.group(1)

    if EXACT: return fileName, target, totalCost, formatTime(executeTime)
    if not EXACT: return fileName, target, totalCost, formatTime(executeTime)

matrixFiles = (('tsp_data/tsp1_253.txt', True),
               ('tsp_data/tsp2_1248.txt', True),
               ('tsp_data/tsp3_1194.txt', False),
               ('tsp_data/tsp4_7013.txt', False),
               ('tsp_data/tsp5_27603.txt', False))


results = []
for file, runTest in matrixFiles:
    results.append(compairAlgorithm(file, runTest))

if EXACT:
    resultsTableExact = pd.DataFrame(results, columns=['Arquivo','Custo Ótimo','Custo exato', 'Tempo de execução\nexato'])
    resultsTable = resultsTableExact
    fig = makeGraph(resultsTable)
    plt.savefig('results/exactResults.png', dpi=200, bbox_inches='tight')
    plt.show()
else:
    resultsTableGenetic = pd.DataFrame(results, columns=['Arquivo', 'Custo Ótimo', 'Custo\nGenético', 'Tempo de execução\nGenético'])
    resultsTable = resultsTableGenetic
    makeGraph(resultsTable)
    plt.savefig('results/geneticResults.png', dpi=200, bbox_inches='tight')
    plt.show()
