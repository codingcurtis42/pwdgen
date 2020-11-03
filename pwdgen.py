import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'


def howmanychars():
    try:
        charamount = input("How many characters would you like: ")
        isinstance(int(charamount), int)
        return charamount
    except:
        print('Please use numbers only')
        return howmanychars()


def howmanyruns():
    try:
        pwdamounts = input("How many passwords would you like: ")
        isinstance(int(pwdamounts), int)
        return pwdamounts
    except:
        print('Please use numbers only')
        return howmanyruns()

def randoed(charamount, pwdamounts):
    for i in range(int(pwdamounts)):
        gendpwd = []
        for j in range(int(charamount)):
            k = random.choice(chars)
            gendpwd.append(k)
        print(''.join(gendpwd))


if __name__ == "__main__":
    charamount = howmanychars()
    pwdamounts = howmanyruns()
    randoed(charamount, pwdamounts)
