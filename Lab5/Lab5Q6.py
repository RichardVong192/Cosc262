def counting_sort(A, key):
    B = [] * len(A)
    P = key_positions(A, key)
    for a in A:
        B[P[key(a)]] = a
        P[key(a)] = p[key(a)] + 1
    return B

def key_positions(seq, key):
    k = max(key(a) for a in seq)
    c = []
    for i in range(k+1):
        c.append(i)
    for i in range(k+1):
        c[i] = 0
    for a in seq:
        c[key(a)] = c[key(a)] + 1
    summ = 0
    for i in range(k+1):
        c[i], summ = summ, summ + c[i]
    return c

def sorted_array(seq, key, positions):
    


#print(key_positions([0, 1, 2], lambda x: x))
#print(key_positions([2, 1, 0], lambda x: x))
#print(key_positions([1, 2, 3, 2], lambda x: x))
#print(key_positions([5], lambda x: x))
#print(key_positions(range(-3,3), lambda x: x**2))
#print(key_positions(range(1000), lambda x: 4))
#print(key_positions([1] + [0] * 100, lambda x: x))