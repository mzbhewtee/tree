# Using a Python dictionary to act as an adjacency list
graph = {
    "A": ["D", "B"], "B": ["A", "D", "E", "F", "C"], "C": ["B", "E", "F"],
    "D": ["A", "B"], "E": ["B", "C"], "F": ["B", "C"]
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    """

    :param visited: visited node set
    :param graph: dictionary containing key value, nodes and its neighbours
    :param node: point of start of traversal
    :return:
    """
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'C')