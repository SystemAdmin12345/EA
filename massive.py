import random

a1 = 0
a2 = 0
a3 = 0
nextlevel = 100


def rng():
    global a1
    global a2
    global a3
    a1 = random.randint(5, 10)
    a2 = random.randint(5, 10)
    a3 = a1 + a2


def activate():
    global nextlevel
    level = 0
    sec = 1
    nextlevel = 100*sec
    print(f"Level: {level}/{nextlevel}")
    rng()
    ans = input(f"What is {a1}+{a2}? ")
    integeranswer = int(ans)
    if integeranswer == a3:
        print("Success")
        level += 1
    else:
        print("Fail")
    nextlevel = sec * 100
    if level >= nextlevel:
        sec += 1
        nextlevel = sec * 100


    activate()


activate()
