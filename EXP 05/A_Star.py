# Assignment No. 5
# Implementation of A* Search

def a_star(graph, start, goal, heuristic):
    open_list = [start]
    closed_list = set()

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:

        current = min(
            open_list,
            key=lambda node: g_cost[node] + heuristic[node]
        )

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", g_cost[goal])
            return True

        open_list.remove(current)
        closed_list.add(current)

        for neighbour, cost in graph[current]:

            if neighbour in closed_list:
                continue

            new_g = g_cost[current] + cost

            # Add new node or update if lower-cost path is found
            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                parent[neighbour] = current

                if neighbour not in open_list:
                    open_list.append(neighbour)

        open_list.sort(
            key=lambda node: g_cost[node] + heuristic[node]
        )

    print("No solution exists.")
    return False

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3)],
    'C': [('E', 2)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 2,
    'E': 3,
    'G': 0
}

start = 'A'
goal = 'G'

a_star(graph, start, goal, heuristic)