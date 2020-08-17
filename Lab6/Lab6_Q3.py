"""Write a function change_greedy(amount, coinage) that takes an integer amount 
of money in some units (call them "cents" if you like) plus a list of integer coin 
values (in an arbitrary order) and returns the breakdown of that amount into coins
as obtained by the greedy algorithm described in the lecture notes. The return 
value is a list of (coin_count, coin_value) tuples sorted in descending order of
coin_value, including only cases where coin_count is greater than zero.

If an exact breakdown is not achieved using the greedy algorithm, 
the function should return None."""

def change_greedy(amount, coinage):
    result = []
    coinage.sort()
    coinage.reverse()
    while amount > 0:
        if (amount % coinage[-1]) != 0:
            return None            
        if amount >= coinage[0]:
            num = amount // coinage[0]
            amount -= (num * coinage[0])
            result.append((num, coinage[0]))
        coinage = coinage[1:]   
    return result

print(change_greedy(82, [1, 10, 25, 5]))
print(change_greedy(80, [1, 10, 25]))
print(change_greedy(82, [10, 25, 5]))