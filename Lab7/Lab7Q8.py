def coins_reqd(value, coinage):
    """The minimum number of coins to represent value"""
    num_coins = [0] * (value + 1)
    for amt in range(min(coinage), value + 1):
        num_coins[amt] = 1 + min(num_coins[amt - c] for c in coinage if  amt >=  c)
        print(num_coins[amt])    #shows the num[i]
    return num_coins[value]

coins_reqd(19,[1, 5, 7, 11])