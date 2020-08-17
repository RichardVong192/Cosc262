from collections import deque

def adjacency_list(graph_str):
    
    graphLines = graph_str.splitlines() #each line in the string
    header = graphLines[0].split(" ") # splits the header of graph into its elements
    numVertices = header[1] #the first line of the graphLines
    result = [[] for _ in range(int(numVertices))] #creates a list with in a list for the numVertices
    graphData = graphLines[1:]  #from element 1 onwards (not including vertex)
    
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


def bfs_tree(adj_list, start):
    n = len(adj_list)
    state = ['U' for _ in range(int(n))]
    parent = [None for _ in range(int(n))]
    queue = deque()
    state[start] = 'D'
    queue.append(start)
    return bfs_loop(adj_list, queue, state, parent)
    
def bfs_loop(adj_list, queue, state, parent):
    while len(queue) != 0:
        u = queue.popleft()
        for v in adj_list[u]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parent[v[0]] = u
                queue.append(v[0])
        state[u] = 'P'
    return parent
        
    