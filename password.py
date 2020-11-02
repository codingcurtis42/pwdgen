import random


def howmany():
    amount = int(input("How many characters would you like: "))
    return amount


def randoed(amount):
    rand = random.randint(1, amount)
    print(rand)


lower vs upper


if __name__ == "__main__":
    amount = howmany()
    randoed(amount)
