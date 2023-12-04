import numpy as np
import sys

def minKey(key):
    minVal = sys.maxsize
    minIndex = -1
    
    for v in range(len(key)):
        if key[v] < minVal:
            minVal = key[v]
            minIndex = v
    return minIndex

def minTree(graph):
    numVertices, _ = graph.shape
    parent = [-1] * numVertices
    key = [sys.maxsize] * numVertices
    
    key[0] = 0
    
    for _ in range(numVertices - 1):
        u = minKey(key)
        key[u] = sys.maxsize
        
        for v in range(numVertices):
            if graph[u][v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]
    
    minSpanningTree = [[0] * numVertices for _ in range(numVertices)]
    
    for i in range(1, numVertices):
        minSpanningTree[parent[i]][i] = graph[i][parent[i]]
        minSpanningTree[i][parent[i]] = graph[i][parent[i]]
                
    return minSpanningTree
    
""" def findOddDegree(graph):
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
    
    return totalCost """
    
def eulerian(graph):
    circuit = []
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            while graph[i][j] > 0:
                circuit.append(i)
                graph[i][j] -= 1
                graph[j][i] -= 1
                i = j
                j = circuit[-1]
    return circuit

def findOddVertices(mst):
    oddVertices = []
    for i in range(len(mst)):
        if(sum(mst[i]) % 2 != 0):
            oddVertices.append(i)
    return oddVertices

def minWeightMatch(oddVertices, graph):
    edges = []
    numVertices, _ = graph.shape
    
    for i in range(len(oddVertices)):
        for j in range(i + 1, len(oddVertices)):
            edges.append((oddVertices[i], oddVertices[j], graph[oddVertices[i]][oddVertices[j]]))


    edges.sort(key=lambda x: x[2])
    
    minWeight = [0] * numVertices
    visited = set()
    
    for edge in edges:
        u, v, weight = edge
        if u not in visited and v not in visited:
            minWeight[u] = v
            minWeight[v] = u
            visited.add(u)
            visited.add(v)
            
    return minWeight

def improveTour(tour, minWeight):
    for i in range(len(tour) - 1):
        if minWeight[tour[i]] == tour[i + 1]:
            return tour[:i + 1] + list(reversed(tour[i + 1:]))
    return tour

def calcCost(graph, tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += graph[tour[i]][tour[i + 1]] 
    return cost

def christofides(graph):
    mst = minTree(graph)
    oddVertices = findOddVertices(mst)
    
    eulerianGraph = [[0] * len(mst) for _ in range(len(mst))]
    
    for i in range(len(mst)):
        for j in range(len(mst[i])):
            eulerianGraph[i][j] = mst[i][j]
            
    minWeight = minWeightMatch(oddVertices, graph)
    
    for i in range(len(minWeight)):
        j = minWeight[i]
        eulerianGraph[i][j] += 1
        eulerianGraph[j][i] += 1
        
    eulerianTour = eulerian(eulerianGraph)
    
    improved = improveTour(eulerianTour, minWeight)
    
    totalCost = calcCost(graph, improved)
    
    return totalCost
    
