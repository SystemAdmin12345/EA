import random

a1 = 0
a2 = 0
a3 = 0
level = 0
sec = 1
next = 100


def rng():
    global a1
    global a2
    global a3
    a1 = random.randint(0, 10)
    a2 = random.randint(0, 10)
    a3 = a1 + a2


def activate():
    global next
    global level
    global sec
    next = 100*sec
    print(f"Level: {level}/{next}")
    rng()
    try:
        ans = input(f"What is {a1}+{a2}? ")
        integer = int(ans)
        if integer == a3:
            print("Success")
            level += 1
        else:
            print("Fail")
        next = sec * 100
    except ValueError:
        print("Not an integer")
    if level >= next:
        sec += 1
        next = sec * 100

    activate()


activate()
