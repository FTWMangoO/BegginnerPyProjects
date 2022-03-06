import random

random.seed()
words = ["apple", "mother", "garden", "dog", "hook", "pig", "book", "cigarette", "painting", "baloon", "house", "kitchen"]
hanged = ["o","|", "\\", "/","\\","/"]



def lettersCheck(ch,le):
    if(not ch.isalpha() or ch.isupper()):
        print("Scrivi una lettera minuscola")
        return True
    if ch not in le:
        le.append(ch)
        print(le)
        return False
    if ch in le:
        print("Lettera già utilizzata")
        print(le)
        return True

def drawHanged(c,hang,change):
    for i in range(0,c):
        change[i]=hang[i]
    print(f""" 
            ----------
            |         |  
            |         {change[0]}
            |        {change[3]}{change[1]}{change[2]}  
            |        {change[5]} {change[4]}
    
            """)

def checkChar(a,rword,gword):
    c=0
    j=0
    for i in rword:
        if(a == i):
            gword[j]=a
            c=1
        j+=1
    return c

def choosing(c,a):
    while c:
        while True:
         ch = input("Play Again?(y/n)")
         if(ch == "y"):
             return True
         if(ch == "n"):
             return False
         print("Error: Choose y/n")

def createWord(gw):
    rw = words[random.randrange(0, len(words) - 1)]
    for i in rw:
        gw += "_"
    return rw

def main():
    print("Hangman Game")
    x = True
    y = True
    H = True

    choice = True

    while x:
        changeHang = [" ", " ", " ", " ", " ", " ", " "]
        count = 0
        letters = list()
        guessW = list()
        randW = list(createWord(guessW).strip())

        while H:
            print("".join(guessW))
            while y:
                char = input("Enter a character:")
                y = lettersCheck(char,letters)
            y = True
            if(checkChar(char,randW,guessW) == 0):
                print("The character isn't in the word")
                count+=1
                drawHanged(count,hanged,changeHang)
            if(guessW == randW):
                print("You won, the word was '{}'".format("".join(randW)))
                break
            if(count == (len(hanged))):
                print("You've lost, the word was '{}'".format("".join(randW)))
                break

        x = choosing(choice,x)

if __name__ == "__main__":
    main()









