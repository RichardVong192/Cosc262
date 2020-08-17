#Green campus

def adjacency_list(graph_str):
    graphLines = graph_str.splitlines()
    header = graphLines[0].split(" ")
    numVertices = header[1]
    result = [[] for _ in range(int(numVertices))]
    graphData = graphLines[1:]
    for i in graphData:
        info = i.split(" ")
        vertex = int(info[0])
        connectedVertex = int(info[1])
        if len(info) == 3:
            weight = int(info[2])
        else:
            weight = None           
        if 'D' in graphLines[0]:    #for directed graphs
            result[vertex].append((connectedVertex, weight))
        else:                       #for undirected graphs
            result[vertex].append((connectedVertex, weight))
            result[connectedVertex].append((vertex, weight))
    return result

def next_vertex(in_tree, distance):
    minDist = float("inf")
    for i in range(len(in_tree)):
        if distance[i] < minDist and in_tree[i] == False:
            minDist = distance[i]
            nextVertex = i
    return nextVertex

def prim(adj_list):
    n = len(adj_list)
    in_tree = [False for _ in range(int(n))]
    distance = [float("inf") for _ in range(int(n))]
    parent = [None for _ in range(int(n))]
    distance[0] = 0
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] is False and weight < distance[v]:          
                distance[v] = weight
                parent[v] = u
    result = []
    for i in range(1,len(distance)):
        result.append((min(parent[i],i),max(parent[i],i)))
    return result


def which_walkways(campus_map):
    adj_list = adjacency_list(campus_map)
    return prim(adj_list)

campus_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_walkways(campus_map)))

campus_map = """\
U 1 W
"""

print(sorted(which_walkways(campus_map)))