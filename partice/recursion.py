#recurions in python 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(5 * factorial(4)) # calculate the factorial of 5

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10)) # calculate the 10th Fibonacci number
