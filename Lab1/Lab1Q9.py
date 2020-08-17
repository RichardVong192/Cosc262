def cycle_length(n):
    if n % 2 == 0: #n is even
        n = n / 2
        return 1 + cycle_length(n)
    elif n == 1:
        return 1   
    elif n % 2 == 1:    #n is odd
        n = 3 * n + 1
        return 1 + cycle_length(n)