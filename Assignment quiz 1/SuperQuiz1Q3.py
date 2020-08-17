#top sort spreadsheets

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


def dfs_loop(adj_list, u, state, parent, stack):
    for v in adj_list[u]:
        if state[v[0]] == 'U':
            state[v[0]] = 'D'
            parent[v[0]] = u
            dfs_loop(adj_list, v[0], state, parent, stack)
        if state[v[0]] == 'D':
            return None           
    state[u] = 'P'
    stack.append(u)

def top_sort(adj_list):
    n = len(adj_list)                  #first initialise variables
    state = ['U' for _ in range(n)]
    parent = [None for _ in range(n)]
    stack = []
    for vertex in range(len(adj_list)):
        if state[int(vertex)] == 'D': #After it discovers all vertex, and non are left, 
                                      #it means no cell depends on another, therefore returns None.
            return None               
        if state[vertex] == 'U':      #if state is undiscovered, do a bfs_loop to discover it
            dfs_loop(adj_list, vertex, state, parent, stack)
    return stack
                 
def computation_order(dependencies):
    adj_list = adjacency_list(dependencies)
    result = top_sort(adj_list)
    return result
    

dependencies = """\
D 2
0 1
"""

print(computation_order(dependencies))

dependencies = """\
D 3
1 2
0 2
"""

print(computation_order(dependencies) in [[2, 1, 0], [2, 0, 1]])

dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = computation_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))
    
dependencies = """\
D 5
2 3
3 2
"""

print(computation_order(dependencies))