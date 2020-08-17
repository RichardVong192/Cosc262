def all_paths(graph_string, source, destination):
    adj_list = adjacency_list(graph_string)
    path = []
    result = find_all_paths(adj_list, source, destination, path)
    return result

def find_all_paths(adj_list, source, destination, path):
    path = path + [source]
    if source == destination:
        return [path]
    result = []
    for vertex in adj_list[source]:
        if vertex not in path:
            newresult = find_all_paths(adj_list, vertex, destination, path)
            for newpath in newresult:
                result.append(newpath)
    return result
        
def adjacency_list(graph_str):
    graph_strings = graph_str.splitlines()
    graph_info = graph_strings[0].split(" ")
    number_of_vertices = graph_info[1]    
    vertices = [[] for _ in range(int(number_of_vertices))]
    edges_info = graph_strings[1:]
    for line in edges_info:
        edge = line.split(" ")
        current_vertex = int(edge[0])
        connecting_edge = int(edge[1])
        vertices[current_vertex].append(connecting_edge)        
        if 'U' in graph_strings[0]:
            vertices[connecting_edge].append(current_vertex) 
                                                                                 
    return vertices


from pprint import pprint

# triangle graph
graph_str = """\
U 3
0 1
1 2
2 0
"""

print(sorted(all_paths(graph_str, 0, 2)))
print(all_paths(graph_str, 1, 1))

# graph in fig 5.15 of text book
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
# triangle graph
graph_str = """\
U 3
0 1
"""

print(sorted(all_paths(graph_str, 0, 2)))