from collections import deque
#5works for both undirected and directed


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


def bfs_tree(adapters_info, start):
    adapters_info = adjacency_list(adapters_info) #new
    n = len(adapters_info)
    state = ['U' for _ in range(int(n))]
    parent = [None for _ in range(int(n))]
    queue = deque()
    state[start] = 'D'
    queue.append(start)
    return bfs_loop(adapters_info, queue, state)
    
def bfs_loop(adapters_info, queue, state):
    while len(queue) != 0:
        u = queue.pop(0)
        for v in adapters_info[u]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                #parent[v[0]] = u
                queue.append(v[0])
        state[u] = 'P'
    return state

#def tree_path(parent,s,t):
    #if s == t:
        #return [s]
    #else:
        #if parent[t] == None:
            #return "CS Unplugged!"
        #else:
            #return tree_path(parent,s,parent[t])+[t]


#def adapter_chain(adapters_info, charger_plug, wall_socket): #parent, start, end
    #adj_list = adjacency_list(adapters_info)
    #parent_graph = bfs_tree(adapters_info, charger_plug)
    #return tree_path(parent_graph, charger_plug, wall_socket)

    
def connected_components(adj_list):
    n = len(adj_list)
    state = ['U' for _ in range(int(n))]
    queue = []
    components = []
    for i in range(n):
        if state[i] == 'U':
            previous_state = state[:]
            state[i] = 'D'
            queue.append(i)
            bfs_loop(adj_list, queue, state)
            component = []
            for i in range(len(previous_state)):
                if previous_state[i] != state[i]:
                    component.append(i)
            new_component = component
            components.append(new_component)
    return components

def arrangement(direct_friendship_info):
    adj_list = adjacency_list(direct_friendship_info)
    #graph = bfs_loop(direct_friendship_info, queue, state)
    return connected_components(adj_list)


direct_friendship_info = """\
U 2
0 1
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 2
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 0
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 1
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))