import random

print("Welcome to the Dice Rolling Game!")
game = input ("Roll the dice(y/n): ")
if game == "y":
    number = random.randint(1,6)
    print("The random number generated is:",number)

elif game == "n":
    print("Thanks for playing")

else:
    print("Invalid choice")



