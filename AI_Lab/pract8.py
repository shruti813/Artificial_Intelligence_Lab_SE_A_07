import heapq

# 1. Define the Graph
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# 2. Define Heuristic Values
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

# 3. A* Algorithm Implementation
def a_star(graph, heuristics, start, goal):
    # Priority queue for the open list (min-heap)
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))  # (f, g, current_node, path)

    # Closed list to keep track of visited nodes
    closed_list = set()

    while open_list:
        f, g, current_node, path = heapq.heappop(open_list)

        # Skip if already visited
        if current_node in closed_list:
            continue

        # If goal is reached
        if current_node == goal:
            return path, g

        # Mark node as visited
        closed_list.add(current_node)

        # Expand neighbors
        for neighbor, cost in graph[current_node].items():
            if neighbor not in closed_list:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')  # If goal is not reachable

# 4. Run the Algorithm
start_node = 'S'
goal_node = 'G'
path, total_cost = a_star(graph, heuristics, start_node, goal_node)

# 5. Print the Output
print("===== A* Algorithm Result =====")
if path:
    print("Path found:", " -> ".join(path))
    print("Total cost:", total_cost)
else:
    print("No path found from", start_node, "to", goal_node)

