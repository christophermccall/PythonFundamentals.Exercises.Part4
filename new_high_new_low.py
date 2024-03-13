from random import randrange


def get_input():
    num = input("enter a number: ")
    return int(num)


def rand_num():
    rand = randrange(1, 10)
    return rand


def high_or_low(random):
    onOff = True
    while onOff:
        user = get_input()
        print("Your number: "+str(user))
        if user > random:
            print("Too high")
        elif user < random:
            print("Too Low")
        elif user == random:
            print("Correct!")
            onOff = False


high_or_low(rand_num())
