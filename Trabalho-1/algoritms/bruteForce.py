import itertools

def tsp_bruteforce(distances):
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
    return min_distance, optimal_path