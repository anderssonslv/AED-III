import sys

def tsp_branch_and_bound(graph):
    print("Rodando branchAndBound...")
    def tsp_recursive(curr_pos, mask, cost):
        nonlocal n, graph, final_path, min_cost

        if mask == (1 << n) - 1:
            if graph[curr_pos][0] != 0:
                curr_cost = cost + graph[curr_pos][0]
                if curr_cost < min_cost:
                    min_cost = curr_cost
                    final_path = path[:]
                    final_path.append(0)
            return

        for city in range(n):
            if (mask & (1 << city)) == 0 and graph[curr_pos][city] != 0:
                path.append(city)
                tsp_recursive(city, mask | (1 << city), cost + graph[curr_pos][city])
                path.pop()

    n = len(graph)
    path = [0]
    final_path = []
    min_cost = sys.maxsize

    tsp_recursive(0, 1, 0)
    print(f"Concluido!\nCusto:{min_cost}\nCaminho:{final_path}")
    return min_cost, final_path