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

def dfs_backtrack(adj_list, state, source, destination, result, tempResult=[]):
    state[source] = "destination"
    tempResult.append(source)
    if is_solution(source, destination):
        add_to_solution(result, tempResult)
    else:
        for child in children(adj_list, source, state):
            dfs_backtrack(adj_list, state, child, destination, result, tempResult)
    tempResult.pop()
    state[source] = "U"

def is_solution(source, destination):
    if source == destination:
        return True
    return False

def add_to_solution(result, tempResult):
    return result.append(tempResult[:])

def children(adj_list, source, state):
    childList = []
    for child, _ in adj_list[source]:
        if state[child] == "U":
            childList.append(child)
    return childList

def all_paths(graph_string, source, destination):
    adj_list = adjacency_list(graph_string)
    state = ["U" for _ in range(len(adj_list))]
    result = []
    dfs_backtrack(adj_list, state, source, destination, result)
    return result



# triangle graph
graph_str = """\
U 3
0 1
1 2
2 0
"""

print(sorted(all_paths(graph_str, 0, 2)))
print(all_paths(graph_str, 1, 1))

graph_str = """\
U 5
0 2
1 2
3 2
4 2
1 4
"""

print(sorted(all_paths(graph_str, 0, 1)))

from pprint import pprint

# graph in fig 5.15 of textbook
# vertices 0 to 6 correspond to A to G
graph_str = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

pprint(sorted(all_paths(graph_str, 6, 3)))

from pprint import pprint

# graph in fig 5.15 of textbook
# vertices 0 to 6 correspond to A to G
graph_str = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

pprint(sorted(all_paths(graph_str, 6, 3)))

from pprint import pprint

graph_str = """\
D 4
0 1
1 2
0 3
3 2
"""

pprint(sorted(all_paths(graph_str, 0, 2)))
pprint(sorted(all_paths(graph_str, 2, 0)))
pprint(sorted(all_paths(graph_str, 1, 2)))
pprint(sorted(all_paths(graph_str, 3, 2)))