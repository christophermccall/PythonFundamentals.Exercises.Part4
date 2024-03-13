def Fibonacci(n):
    # First Fibonacci number is 0
    if n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


for i in range(1, 31):
    print(Fibonacci(i))
'''
think java version
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


for i in range(1, 31):
    print(Fibonacci(i))
'''