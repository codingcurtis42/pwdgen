import random
fizz = []
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

charamount = input("How many characters would you like: ")

pwdamounts = input("How many passwords would you like: ")


for i in range(int(pwdamounts)):
    genpwd = []

    for j in range(int(charamount)):

        k = random.choice(chars)
        genpwd.append(k)
    fizz.append(genpwd)
