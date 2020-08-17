def almost_all(numbers):
    summ = sum(numbers)
    return [summ - x for x in numbers] 