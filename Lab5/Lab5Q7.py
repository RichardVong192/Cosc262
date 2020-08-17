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
    seq_list = list(seq)
    b_array = [0 for _ in range(len(seq_list))]
    for a in seq_list:
        b_array[positions[key(a)]] = a
        positions[key(a)] = positions[key(a)] + 1
    return b_array
    


print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))