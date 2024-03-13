def factorials():
    x = input("please enter a number:")
    sum = 1
    for i in range(int(x), 1, -1):
        sum *= i
    print(sum)


factorials()