num1 = 0
num2 = 1
next_number = num1
for i in range(1,31):
    print(next_number)
    num1, num2 = num2, next_number
    next_number = num1 + next_number
