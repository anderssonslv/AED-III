import numpy as np
import sys 
from time import time
import matplotlib.pyplot as plt
import networkx as nx

def minTree(graph):
    numVertices, _ = graph.shape
    visited = [False] * numVertices
    minSpanningTree = np.zeros_like(graph)
    
    visited[0] = True
    
    for _ in range(numVertices - 1):
        minEdge = [sys.maxsize, None, None]
        
        for i in range(numVertices):
            if visited[i]:
                for j in range(numVertices):
                    if not visited[j] and graph[i][j] < minEdge[0] and graph[i][j] != 0:
                        minEdge = [graph[i][j], i, j]
        _, u, v = minEdge
        visited[v] = True
        minSpanningTree[u][v] = minEdge[0]
        minSpanningTree[v][u] = minEdge[0]
    
    return minSpanningTree
    
def findOddDegree(graph):
    degrees = np.sum(graph, axis=1)
    oddVertices = np.where(degrees % 2 != 0)[0]
    return oddVertices

def findMatch(graph, oddVertices):
    minWeight = np.zeros_like(graph)
    
    for i in range(len(oddVertices)):
        for j in range(i + 1, len(oddVertices)):
            minWeight[oddVertices[i]][oddVertices[j]] = graph[oddVertices[i]][oddVertices[j]]
            minWeight[oddVertices[j]][oddVertices[i]] = graph[oddVertices[j]][oddVertices[i]]
    
    return minWeight

def findEulerian(graph):
    stack = [0]
    circuit = []
    
    while stack:
        current = stack[-1]
        neighbors = np.where(graph[current] > 0)[0]
        
        if neighbors.any():
            nextVertice = neighbors[0]
            stack.append(nextVertice)
            graph[current][nextVertice] -= 1
            graph[nextVertice][current] -= 1
        else:
            circuit.append(stack.pop())
            
    return circuit[::-1]

def calcCost(graph, tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += graph[tour[i]][tour[i + 1]]
    return cost

def christofides(graph):
    mst = minTree(graph)
    oddVertices = findOddDegree(mst)
    minWeightMatch = findMatch(graph, oddVertices)
    mergeGraph = mst + minWeightMatch
    eulerianCircuit = findEulerian(mergeGraph)
    
    tour = []
    visited = set()
    
    for vertice in eulerianCircuit:
        if vertice not in visited:
            tour.append(vertice)
            visited.add(vertice)
            
    tour.append(tour[0])
    totalCost = calcCost(graph, tour)
    
    return totalCost


