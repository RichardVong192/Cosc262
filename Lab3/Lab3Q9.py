def next_vertex(in_tree, distance):
    """ that takes two arrays, in_tree and distance, 
    and returns the vertex that should be added to the tree next."""
    
    minDist = distance[0]
    for i in range(len(in_tree)):
        if distance[i] < minDist and in_tree[i] == False:
            minDist = distance[i]
            nextVertex = i
    return nextVertex
        
in_tree = [False, False, False]
distance = [float('inf'), 0, float('inf')]
print(next_vertex(in_tree, distance))