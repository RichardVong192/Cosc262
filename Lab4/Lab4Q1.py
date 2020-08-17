def dfs_backtrack(s, solutions, tempList = []):
    if is_solution(tempList, s):
        add_to_solutions(tempList, solutions)
    else:
        for child in children(tempList, s):
            dfs_backtrack( s, solutions, tempList = tempList + [child])


def is_solution(tempList, s):
    return len(tempList) == len(s)


def children(tempList, s):
    result = []
    for item in s:
        if item not in tempList:
            result.append(item)
            print(result)
    return result
    
def add_to_solutions(tempList, solutions):
    solutions.append(tuple(tempList))


def permutations(s):
    solutions = []
    dfs_backtrack(s, solutions)	
    return solutions



print(sorted(permutations({1,2,3})))

print(sorted(permutations({'a'})))

perms = permutations(set())
print(len(perms) == 0 or list(perms) == [()])