

def Floyd_Warshall(nodes, edges):
    """

    :param nodes: nodes set
    :param edges: edges set
    :return: shortest path
    """

    distance = {(i, j): float('inf') if i != j else 0 for i in nodes for j in nodes}

    for (i, j), weight in edges.items():
        distance[(i, j)] = weight

    # Check for the smallest weight of edges between all available paths in the nodes
    for k in nodes:
        for i in nodes:
            for j in nodes:
                distance[(i, j)] = min(distance[(i, j)], distance[(i, k)] + distance[(k, j)])

    # Checks for negative-cycle in the graph
    if any(distance[(i, i)] < 0 for i in nodes):
        print("Negative Cycle")

    return distance

vertices = ["u", "v", "w", "z", "y", "x"]

# edges weight
weight = {("u", "v"): 2, ("u", "w"): 5, ("u", "x"): 1,
     ("v", "u"): 2, ("v", "w"): 3, ("v", "x"): 2,
     ("w", "u"): 5, ("w", "x"): 3, ("w", "y"): 1, ("w", "z"): 5, ("w", "v"): 3,
     ("x", "u"): 1, ("x", "y"): 1, ("x", "v"): 2, ("x", "w"): 3,
     ("y", "z"): 1, ("y", "w"): 1, ("y", "x"): 1,
     ("z", "w"): 5, ("z", "y"): 1
     }


shortest_path = Floyd_Warshall(vertices, weight)
for key in shortest_path:
    print(key, ':', shortest_path[key])
