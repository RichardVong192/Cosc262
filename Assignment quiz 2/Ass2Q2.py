def longest_common_substring(s1, s2):
    """Bruh"""
    
    #Initilise rows and cols
    n_rows = len(s1) 
    n_cols = len(s2)
    
    #Making the table (row * col) to store dp values
    grid = [["" for x in range(n_cols + 1)] for x in range(n_rows + 1)]

    #Calculates the values that should go into rows
    for i in range(n_rows + 1): 
        for j in range(n_cols + 1): 
            if i == 0 or j == 0: 
                grid[i][j] = 0
            elif s1[i-1] == s2[j-1]: 
                grid[i][j] = grid[i-1][j-1]+1
            else: 
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
    for i in grid:
        print(i)
    return backtracking_grid(s1, s2, grid)
    

def backtracking_grid(s1, s2, grid):
    """Retrieving the actual seqence (Optimisation algrithms - Slide 96)"""
    i = len(s1)
    j = len(s2)
    result = ""

    #the first row and col are just filled with 0's
    while(i != 0 and j != 0):
        #start at last positon in the matrix, if they are equal...
        if s1[i-1] == s2[j-1]:
            #move to position [i-1,j-1]
            i -= 1
            j -= 1 
            #add s1[i] to begining of result
            result += s1[i]            
        #If s1[i] != s2[j]
        else:
            #Move to whichever of [i-1, j] or [i, j-1] contains the maximum value.
            if grid[i-1][j] < grid[i][j-1]:
                j -= 1
            else:
                i -= 1
                
    #Reverse the result because you are appending it to the end.
    result = result[::-1]
    return result
        
    
#s1 = "Look at me, I can fly!"
#s2 = "Look at that, it's a fly"
#print(longest_common_substring(s1, s2))
##16

#s1 = "abcdefghijklmnopqrstuvwxyz"
#s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
#print(longest_common_substring(s1, s2))
##0

#s1 = "balderdash!"
#s2 = "balderdash!"
#print(longest_common_substring(s1, s2))
##11

s1 = "glorious"
s2 = "algorithms"
print(longest_common_substring(s1, s2))
#should be 5

#s1 = 1500 * 'x'
#s2 = 1500 * 'y'
#print(longest_common_substring(s1, s2))

#s1 = "Solidandkeen\nSolidandkeen\nSolidandkeen\n"
#s2 = "Whoisn'tsick\nWhoisn'tsick\nWhoisn'tsick"
#lcs = longest_common_substring(s1, s2)
#print(lcs)
#print(repr(lcs))