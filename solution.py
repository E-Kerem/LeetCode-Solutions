def findSmallestSetOfVertices(n, edges):
    # Create a set to keep track of all vertices which have incoming edges
    has_incoming_edges = set()
    
    # Loop through each edge in the edges list
    for u, v in edges:
        has_incoming_edges.add(v)
    
    # The vertices that don't have incoming edges will be our answer
    result = []
    
    for vertex in range(n):
        if vertex not in has_incoming_edges:
            result.append(vertex)
    
    return result