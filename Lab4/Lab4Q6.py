def matrix_multiplication(x, y):
    result = [[0 for a in range(2)] for number in range(2)]
    
    #matrix multiplication using a nested loop
    #iterate through rows of X
    for i in range(len(x)):
        #iterate through columns of Y
        for j in range(len(y[0])):
            #iterate through rows of Y
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    return result

def process_fib(n):
    #6.4 fast exponentiation from lecture notes page29
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return [[1, 1], [1, 0]]
    else:
        p = process_fib(n//2)
        if n % 2 == 0: #if n is even
            return matrix_multiplication(p, p) 
        else:
            return matrix_multiplication([[1, 1], [1, 0]], matrix_multiplication(p, p))
        
def fib(n):
    return process_fib(n)[0][1] #indexing at row 0 column 1

print(fib(5))

print(fib(6))

print(fib(7))

print(fib(100))