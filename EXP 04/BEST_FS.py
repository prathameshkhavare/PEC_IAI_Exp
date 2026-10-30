import heapq

def best_first_search(graph, heuristic, start, goal):
    open_list = []
    closed = set()
    parent = {}

    # Add start node to OPEN list
    heapq.heappush(open_list, (heuristic[start], start))
    parent[start] = None

    while open_list:
        # Select node with smallest heuristic value
        h, current = heapq.heappop(open_list)

        if current in closed:
            continue

        closed.add(current)

        # Check goal
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Path:", " -> ".join(path))
            print("Goal reached!")
            return path

        # Expand current node
        for neighbor in graph[current]:
            if neighbor not in closed:
                if neighbor not in parent:
                    parent[neighbor] = current

                heapq.heappush(
                    open_list,
                    (heuristic[neighbor], neighbor)
                )

    print("Goal not reached!")
    return None


# Graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['T'],
    'F': ['R'],
    'G': ['N'],
    'H': ['O', 'P'],
    'I': ['Q'],
    'J': ['R'],
    'P': ['I'],
    'Q': [],
    'N': [],
    'O': [],
    'T': [],
    'R': [],
}

# Heuristic values
heuristic = {
    'A': 0,
    'B': 4,
    'C': 4,
    'D': 6,
    'E': 5,
    'F': 5,
    'G': 4,
    'H': 3,
    'I': 4,
    'J': 4,
    'N': 0,
    'O': 2,
    'P': 3,
    'Q': 0,
    'R': 4,
    'T': 5
}

# Start and Goal
start = 'A'
goal = 'P'

best_first_search(graph, heuristic, start, goal)