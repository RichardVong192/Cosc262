def coins_reqd(value, coinage):
    '''thus'''
    alist = []
    aDict = dict{}
    
    if not coinage or value <= 0:
        return alist
    else:  
        alist = min((coins_reqd(value - c, coinage) + [c] for c in coinage if value >= c), key=len)
        
    return alist

#print(coins_reqd(19,[1, 5, 7, 11]))
print(coins_reqd(32, [1, 10, 25]))