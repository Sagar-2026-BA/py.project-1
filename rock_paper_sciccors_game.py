"""
#ROCK PAPER SCICCORS GAME
r-Rock
p-Paper
s-Sciccors

"""
import random
computer = random.choice(['r','s','p'])
you=str(input("enter your choice..(r/s/p):"))
print(f"computer chose:{computer}")
if(computer==you):
    print("draw")


else:
    if(computer=='r' and you=='s'):
        print("you lose")


    elif(computer=='s' and you=='r'):
        print("you win")



    elif(computer=='p' and you=='r'):
        print("you lose")



    elif(computer=='r' and you=='p'):
        print("you win")



    elif(computer=='p' and you=='s'):
        print("you win")


    elif(computer=='s' and you=='p'):
        print("you lose")

    if(you=='r' or you=='s' or you=='p'):
        print("valid choice")

