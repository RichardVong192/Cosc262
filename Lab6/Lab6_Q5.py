"""Write a function fractional_knapsack(capacity, items) that returns the 
maximum achievable value ("benefit") obtainable with a knapsack of the given
capacity and a given list of items, each represented by a 
tuple (name, value, weight). In this problem you are allowed to take
fractions of an item."""

def fractional_knapsack(capacity, items):
    weight = []
    benefit = []
    value = []
    result = 0
    items.sort(reverse = True, key=lambda x: x[1]/x[2]) #sort items in decensing order of benefit
    for item in items:
        value.append(item[1])
        weight.append(item[2])
        benefit.append(item[1]/item[2])
    fractions = [0]*len(value)
    for i in range(len(value)):
        if weight[i] <= capacity:
            fractions[i] = 1
            result += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            result += value[i]*capacity/weight[i]
            break
    return result

# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))