# Graph to be traversed
graph = {
    "A": ["D", "B"], "B": ["A", "D", "E", "F", "C"], "C": ["B", "E", "F"],
    "D": ["A", "B"], "E": ["B"], "F": ["B", "C"]
}

# Set to store visited nodes
visited = set()


def dfs(visited, graph, node):
    """

        :param visited: visited node set
        :param graph: dictionary containing key value, nodes and its neighbours
        :param node: point of start of traversal
        :return:
        """
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("The path from the start node C:")

dfs(visited, graph, 'C')


def Dijkstra(nodes, paths, source):
    """

    :param nodes: node list
    :param paths: dictionary containing key-value pairs of paths with their weights
    :param source: source node
    :return: path length from the source node to each of the vertices
    """

    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source] = 0

    neighbour = {v: {} for v in nodes}
    for (u, v), weight in paths.items():

        neighbour[u][v] = weight
        neighbour[v][u] = weight

    temp_nodes = [v for v in nodes]
    # Iterate while finding the smallest path length until there are no nodes left
    while len(temp_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temp_nodes}
        # Get the smallest path length
        u = min(upper_bounds, key=upper_bounds.get)

        temp_nodes.remove(u)

        for v, weight in neighbour[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + weight)
    return path_lengths


# Dictionary of paths within the graph with their corresponding weights
path = {("C", "B"): 5, ("C", "E"): 22, ("C", "F"): 30,
         ("F", "B"): 18, ("B", "E"): 20, ("B", "D"): 17,
         ("A", "D"): 10, ("A", "B"): 13}
# Nodes in the graph
node = ["C", "B", "A", "D", "E", "F"]

print("The shortest path from the source node 'D' to 'E':")

result = Dijkstra(node, path, "C")

for key, value in result.items():
    if key == "E":
        print("D ->", key, ":", value)

print("The shortest path from node D to nodes B, A, D, E: ")
for key, value in result.items():
    print("D ->", key, ":", value)

