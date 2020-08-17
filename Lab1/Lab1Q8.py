def recursive_divide(x, y):
    if x == 0: 
        return (0)
    elif x == y:
        return (1)
    elif x - y == 0:
        return (0)
    elif x < y:
        return (0)
    else:
        return ( 1 + recursive_divide(x - y, y))