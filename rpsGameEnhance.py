import random

# Greetings MID
print("Welcome to this game!")
print("\nPlease select your option:")
print("1: Rock")
print("2: Paper")
print("3: Scissors")
inventory = ["Rock", "Paper", "Scissors"] 

while True:
    userChoice = input("\nEnter your choice (1/2/3): ")
    if userChoice in ["1", "2", "3"]:
        userChoice = int(userChoice) 
        userChoice -= 1  
        comChoice = random.randint(0, 2) 

        print("Computer Choice:", inventory[comChoice])

        if userChoice == comChoice:
            print("It's a tie!")
        elif (userChoice == 0 and comChoice == 2) or (userChoice == 1 and comChoice == 0) or (userChoice == 2 and comChoice == 1):
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid Input. Fuck You User #$&#@∆")
