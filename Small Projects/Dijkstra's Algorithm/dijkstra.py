from heapq import heapify, heappop, heappush


class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph  # A dictionary for the adjacency list

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:  # Check if the node is already added
            self.graph[node1] = {}  # If not, create the node
        # Else, add a connection to its neighbor
        self.graph[node1][node2] = weight

    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0

        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()

        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(
                pq
            )  # Get the node with the min distance

            if current_node in visited:
                continue  # Skip already visited nodes
            visited.add(current_node)  # Else, add the node to visited set

            for neighbor, weight in self.graph[current_node].items():
                # Calculate the distance from current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))

            predecessors = {node: None for node in self.graph}

            for node, distance in distances.items():
                for neighbor, weight in self.graph[node].items():
                    if distances[neighbor] == distance + weight:
                        predecessors[neighbor] = node

        return distances, predecessors

    def shortest_path(self, source: str, target: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()

        return path


graph = {
    "A": {"B": 7, "C": 5, "E": 10, "G": 10.5},
    "B": {"A": 7, "C": 3, "D": 6, "J": 9.5},
    "C": {"A": 5, "B": 3, "D": 4, "E": 7},
    "D": {"B": 6, "C": 4, "E": 7, "F": 4, "J": 4},
    "E": {"A": 10, "C": 7, "D": 7, "F": 5},
    "F": {"D": 4, "E": 5, "G": 6, "H": 4, "I": 6, "J": 4},
    "G": {"A": 10.5, "F": 6, "I": 6},
    "H": {"F": 4, "I": 4, "J": 4},
    "I": {"F": 6, "G": 6, "H": 4, "J": 8.5},
    "J": {"B": 9.5, "D": 4, "F": 4, "H": 4, "I": 8.5}
}

G = Graph(graph)
distances = G.shortest_distances("I")

print("The shortest distance from node A to node I is: "
      f"{distances[0]["A"]} points.")
print("The shortest path from node A to node I is: "
      f"{G.shortest_path("A", "I")[0]} --> {G.shortest_path("A", "I")[1]} --> "
      f"{G.shortest_path("A", "I")[2]}.")
