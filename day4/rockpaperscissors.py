import random

rock = 1
paper = 2
scissors = 3
computer_choice = random.randint(1,3)

player_choice = input("Rock, paper, scissors? ").strip().lower()

if player_choice not in ["rock", "paper", "scissors"]:
    print("What the sigma?")
    exit()
else:
    if player_choice == "rock" and computer_choice == scissors:
        print("player chooses rock...")
        print("computer uses scissors...")
        print("You won!")
    elif player_choice == "rock" and computer_choice == paper:
        print("player chooses scissors...")
        print("computer uses paper...")
        print("You lost!")

    elif player_choice == "scissors" and computer_choice == paper:
        print("player chooses scissors...")
        print("computer uses rock...")
        print("You won!")
    elif player_choice == "scissors" and computer_choice == rock:
        print("player chooses scissors...")
        print("computer uses rock...")
        print("You lost!")
    
    elif player_choice == "paper" and computer_choice == rock:
        print("player chooses paper...")
        print("computer uses rock...")
        print("You won!")
    elif player_choice == "paper" and computer_choice == scissors:
        print("player chooses paper...")
        print("computer uses scissors...")
        print("You lost!")
    else:
        print("It's a tie!")
    