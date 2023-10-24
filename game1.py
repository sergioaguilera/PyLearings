import random

computer=random.randint(1,3)

user=input("Let's play (1)rock, (2)papper, (3)sissors, Choose a number between them: ")
value="nothing"
if user == "1":
    print("You choose rock")
    value="rock"
elif user == "2":
    print("You choose papper")
    value="papper"
elif user == "3":
    print("You choose sissors") 
    value="sissors" 
else:
    print("Your number isn't valid please restart the game ")

if int(user) > int(computer):
    print(f"you win, the computer choose {computer}")
elif int(user) == int(computer):
    print(f"it's a tie both select {value}")
else:
    print("you lose")


print(f"just for debbuging, the computer selects {computer}")