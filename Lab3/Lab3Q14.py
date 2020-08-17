def adjacency_matrix(graph_str):
    
    graphLines = graph_str.splitlines() #each line in the string
    header = graphLines[0].split(" ") # splits the header of graph into its elements
    numVertices = int(header[1]) #the first line of the graphLines
    result = [[float('inf')] * numVertices for _ in range(int(numVertices))] #creates a list * numb matrices times the number of num verticies
    graphData = graphLines[1:]  #from element 1 onwards (not including vertex)
    
    for i in range(numVertices):
        result[i][i] = 0
    for k in graphData:
        info = k.split(" ")
        vertex = int(info[0])
        connectedVertex = int(info[1])
        weight = int(info[2])
        result[vertex][connectedVertex] = weight
        if 'U' in graphLines[0]:
            result[connectedVertex][vertex] = weight
    return result