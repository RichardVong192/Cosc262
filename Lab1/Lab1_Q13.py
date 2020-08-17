def sort_of(numbers):
    alist = []
    if numbers == []:
        return alist
    else:
        alist.append(numbers[-1])
        i = len(numbers) - 1
        for h in range(len(numbers)-1):
            if alist[-1] <= numbers[i-h-1]:
                alist.append(alist[-1])
            else:
                alist.append(numbers[i-h-1])
        return alist[::-1]
        