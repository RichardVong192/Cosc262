def adjacency_list(graph_str):
    graphLines = graph_str.splitlines()
    header = graphLines[0].split(" ")
    numVertices = header[1]
    result = [[] for _ in range(int(numVertices))]
    graphData = graphLines[1:]
    for i in graphData:
        info = i.split(" ")
        u = int(info[0])
        connectedu = int(info[1])
        if len(info) == 3:
            weight = int(info[2])
        else:
            weight = None           
        if 'D' in graphLines[0]:    #for directed graphs
            result[u].append((connectedu, weight))
        else:                       #for undirected graphs
            result[u].append((connectedu, weight))
            result[connectedu].append((u, weight))
    return result

def next_vertex(in_tree, distance):
    minDist = float("inf")
    nextVertex = None
    for i in range(len(in_tree)):
        if distance[i] < minDist and in_tree[i] == False:
            minDist = distance[i]
            nextVertex = i
    return nextVertex

def dijkstra(adj_list, s):
    n = len(adj_list)
    in_tree = [False for _ in range(int(n))]
    distance = [float("inf") for _ in range(int(n))]
    parent = [None for _ in range(n)]
    distance[s] = 0
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        if u is None:
            return parent, distance
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance

def maximum_energy(city_map, depot_position):
    adj_list = adjacency_list(city_map)
    parent, distance = dijkstra(adj_list, depot_position)
    energy = -1
    for i in range(len(distance)):
        if distance[i] != float('inf') and distance[i] > energy:
            energy = distance[i]
    return energy * 2
