import random

def game():
    ans = random.randint(1,101)
    while(True):
        number = int(input("Guess the number"))
        if(number>ans):
            print("Too high")
        elif(number<ans):
            print("Too low")
        else:
            print("YOU WON")
            break

game()
