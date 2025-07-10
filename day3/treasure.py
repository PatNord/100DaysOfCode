#Basic and short if, elif and else practice project.

print("""
                _
               (_)
                |
           ()---|---()
                |
                |
         __     |     __
        |\     /^\     /|
          '..-'   '-..'
            `-._ _.-`
                `
""")
event_counter = 0

print("Welcome to the boat!")
player_choice = input(" Do you want to go up or down? ").lower().strip()

if player_choice != "up" and player_choice != "down": 
    print("You walked overboard. Game over.")
else: 
    if player_choice == "up":
        print("You went up the stairs on the maindeck.")
        event_counter = 1
    else:
        print("You went to the lower decks and found some rum. You are drunk and game is over")

if event_counter == 1:
    print("You walk to the ships wheel.")
    player_choice = input("Do you want to turn it? Yes or No? ").lower().strip()
    if player_choice == "yes":
        print("you crashed the ship. Game over.")
    else:
        print("You continue onwards. Soon you see land in the distance.")
        event_counter = 2

if event_counter == 2:
    print("You are close to the shore. Do you want to land?")
    player_choice = input("Yes or No? ")
    if player_choice == "yes":
        print("You land your skiff to the shore. There is something in the sand.")
        event_counter = 3 
    else:
        print("Drunkard on your lower decks lights up the black powder canister and blows up the ship. Game over.")


if event_counter == 3:
    player_choice = input("What you want to do with the object in the sand? Dig, leave or ignore? ").strip().lower()
    if player_choice == "leave" or player_choice == "ignore":
        print("Natives capture and make dinner out of you. Game over.")
    elif player_choice == "dig":
        print("You found box of rum in the sand. You and your crew won the game!")