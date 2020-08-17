from collections import deque
#Only works for directed graphs

def adjacency_list(adapters_info_str):
    graphLines = adapters_info_str.splitlines() #each line in the string
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
    return result


def bfs_tree(adapters_info, start):
    adapters_info = adjacency_list(adapters_info) #new
    n = len(adapters_info)
    state = ['U' for _ in range(int(n))]
    parent = [None for _ in range(int(n))]
    queue = deque()
    state[start] = 'D'
    queue.append(start)
    return bfs_loop(adapters_info, queue, state, parent)
    
def bfs_loop(adapters_info, queue, state, parent):
    while len(queue) != 0:
        u = queue.popleft()
        for v in adapters_info[u]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parent[v[0]] = u
                queue.append(v[0])
        state[u] = 'P'
    return parent

def tree_path(parent,s,t):
    if s == t:
        return [s]
    else:
        if parent[t] == None:
            return "CS Unplugged!"
        else:
            return tree_path(parent,s,parent[t])+[t]


def adapter_chain(adapters_info, charger_plug, wall_socket): #parent, start, end
    adj_list = adjacency_list(adapters_info)
    parent_graph = bfs_tree(adapters_info, charger_plug)
    return tree_path(parent_graph, charger_plug, wall_socket)


adapters_info_str = """\
D 2
0 1
"""

charger_plug = 0
wall_socket = 1

print(adapter_chain(adapters_info_str, charger_plug, wall_socket))

adapters_info_str = """\
D 2
0 1
"""

print(adapter_chain(adapters_info_str, 1, 1))

adapters_info_str = """\
D 2
0 1
"""

print(adapter_chain(adapters_info_str, 1, 0))

adapters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

print(adapter_chain(adapters_info_str, 1, 2))

adapters_info_str = """\
D 1
"""

print(adapter_chain(adapters_info_str, 0, 0))