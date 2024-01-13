# Rock, Paper, Scissor by Python
import random

# Greetings
print("Welcome to this game!")
print("\nPlease select your option:")
print("1: Rock")
print("2: Paper")
print("3: Scissor")

# Main work
inventory = ["Rock", "Paper", "Scissor"]


while True:
    userChoice = input("\nEnter your choice (Rock/Paper/Scissor): ")

    # User Input Validation
    if userChoice in inventory:
        comChoice = random.choice(inventory)
        print("Computer Choice:", comChoice)

        # Determine the winner
        if userChoice == comChoice:
            print("It's a tie!")
        elif (userChoice == "Rock" and comChoice == "Scissor") or (userChoice == "Paper" and comChoice == "Rock") or (userChoice == "Scissor" and comChoice == "Paper"):
            print("You win!")
        else:
            print("Computer wins!")
        
    else:
        print("Invalid Input. Try again.")