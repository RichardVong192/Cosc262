def permutations(s):
    alist = list(s)
    left = 0
    right = len(s) - 1
    result = []
    result = permute(alist, left, right, result)
    return result

def permute(alist, left, right, result):
    if left == right:
        result.append(tuple(alist))
    else:
        for i in range(left, right+1):
            alist[left], alist[i] = alist[i], alist[left]
            permute(alist, left+1, right, result)
            alist[left], alist[i] = alist[i], alist[left]
    return result

#def permutations(s):
    #solutions = []
    #items = list(s)

#def backtrack_dfs(a, k, input, solutions):
    #if is_a_solution(a, k, input):
        #process_solution(a, k, input, solutions)
    #else:
        #for c in construct_candidates(a, k, input):
            #a[k] = c
            #backtrack_dfs(a, k+1, input, solutions)
#def permutations (s):
    #solutions = []
    #items = list(s)
    #boolean_vector = [None] * len(items)
    #k = 0
    #backtrack_dfs(boolean_vector, k, items, solutions)
    #return solutions

#def is_a_solution(a, k, input):
    #return k == len(input)

#def process_solution(boolean_vector, k, items, solutions):
    #solution = set()
    #for i, b in enumerate(boolean_vector):
        #if b:
            #solution.add(items[i])
    #solutions.append(solution)

#def construct_candidates(boolean_vector, k, items):
    #return [False, True]

print(sorted(permutations({1,2})))
print(sorted(permutations({'a'})))
perms = permutations(set())
print(len(perms) == 0 or list(perms) == [()])

