def almost_all(numbers):
    summ = sum(numbers)
    return [summ - x for x in numbers]

almost_all(list(range(10**5)))
print("OK")