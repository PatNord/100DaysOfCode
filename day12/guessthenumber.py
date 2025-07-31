import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print('Choose difficulty. Type "easy" or "hard".')

secret_number = random.randrange(1,101)
print(f"Secret number is {secret_number}")

while True:
    mode = input("> ").strip().lower()

    if mode not in ["easy", "hard"]:
        print("Invalid choice!")
        continue

    if mode == "easy":
        lives = 10
        break
    else:
        lives = 5
        break

    
print("guess the number:")
while lives > 0:
    try:
        player_choice = int(input("> "))
    except ValueError:
        print("Use only numeric values!")
        continue
    if lives == 1 and player_choice != secret_number:
        print("You lost!")
        break
    if player_choice == secret_number:
        print("You guessed right!")
        break
    elif player_choice > secret_number:
        print("Too high!")
        lives -= 1
        print(f"{lives} left.")
    elif player_choice < secret_number:
        print("Too low!")
        lives -= 1
        print(f"{lives} left.")
    
        


        

    


