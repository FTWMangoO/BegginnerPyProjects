import random


def hint1(b):
    return "The guessing number is greater than 50" if (b > 50) else "The guessing number is lesser than 50"


def hint2(b):
    return "The guessing number is even" if (b % 2 == 0) else "The guessing number is odd"


def hint3(b):
    x = random.randrange(0,12)
    y = random.randrange(0,12)
    strin = f"Your number lies between {b-x}"
    strin +=f" and {b+y}" if (b - 5 > 0) else "0"
    return strin


def hintchoice():
    while True:
        try:
            tipscheck(hints)
            z = int(input())
            if z not in range(1, len(hints) + 1):
                raise ValueError
            hintselect(z)
            break
        except ValueError:
            print("Enter the correct choice")


def hintselect(r):
    print(hints[r-1])
    hints[r-1] = 0


def numcheck(a):
    while True:
        if -1 < a < 101:
            break
        raise ValueError


def tipscheck(lis):
    string = "Press "
    for i in range(0, 3):
        if lis[i] != 0:
            string += f"{i+1} "
    print(string)


print("Number Guessing Game")
print("You must select a number between 0 and 100")
print("You have 3 hints")
print("The game is over when you guess the number or press 0")

x = 0
random.seed()
rand = random.randrange(1, 101)
hints = [hint1(rand), hint2(rand), hint3(rand)]

while x != rand:
    try:
        x = int(input("Enter a number:"))
        if x == 0:
            break
        numcheck(x)
        if x == rand:
            break
        while True:
            risp = input("Need a hint?(s/n):")
            if risp == "n":
                break
            if risp == "s":
                hintchoice()
                break
            print("Enter a valid character")
    except ValueError:
        print("You must enter a valid number")

print(f"Game ended. The number was {rand}")