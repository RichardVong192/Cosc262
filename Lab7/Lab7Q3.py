"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
from math import inf as INFINITY

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid

def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    result = [[None] * n_cols for _ in range(n_rows)]

    #iterates throughs the rows and columns and calculates the weights and each square
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if i == 0: #Condition: First row
                       #First row weights are the same value as input graph
                result[i][j] = grid[i][j]
            
            elif j == 0: #Condition: Left side columns
                         #Calculate the min of the square above and its right neighbour
                cheapest_entry = min(result[i-1][j], result[i-1][j+1])
                result[i][j] = grid[i][j] + cheapest_entry
                
            elif j == n_cols-1: #Condition: Right-side columns
                                #Calculate the min of the square above and its left neighbour
                cheapest_entry = min(result[i-1][j-1] , result[i-1][j])
                result[i][j] = grid[i][j] + cheapest_entry
                
            else:   #Otherwise
                cheapest_entry = min(result[i-1][j-1] , result[i-1][j], result[i-1][j+1] )
                result[i][j]= grid[i][j] + cheapest_entry

    best = min(result[n_rows-1])
    return best
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

print(file_cost('test1'))

print(file_cost('test2'))

print(file_cost('test3'))