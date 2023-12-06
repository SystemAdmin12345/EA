multi = ["one", "two", "three", "five"]
length = len(multi)


def load(item1):
    for i in range(length):
        if item1 == multi[i]:
            return 0
    return 1

if load(input("Enter something: ")) == 0:
    print("Listed ")
else:
    print("Unlisted ")
