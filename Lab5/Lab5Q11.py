def radix_sort(numbers, d):
    n = 10
    for _ in range(d):
        numbers = counting_sort(numbers, lambda x: x%n)
        n *= 10
    return numbers

def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)

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

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))