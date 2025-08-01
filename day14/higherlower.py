from data import data
import random

def main():
    main_compare = random.choice(data)
    score = 0
    used_data = []

    while True:
        compare_against = random.choice(data)

        if len(used_data) >= len(data) - 1:
            print("You finished the game!")
            print(f"final score {score}")
            break

        if compare_against['name'] in used_data or compare_against == main_compare:
            continue

        print(f"{main_compare['name']} has {main_compare['searches']} monthly searches.\n")
        print(f"{compare_against['name']} has higher or lower searches than {main_compare['name']}?")

        player_input = input("> ").lower().strip()
        if player_input not in ["higher", "lower"]:
            print('Type "higher" or "lower" to take your guess!')
            continue
        if player_input == "higher" and compare_against['searches'] > main_compare['searches']:
            score += 1
            used_data.append(main_compare['name'])
            main_compare = compare_against
            
        elif player_input == "lower" and compare_against['searches'] < main_compare['searches']:
            score += 1
            used_data.append(main_compare['name'])
            main_compare = compare_against
            
        else:
            print(f"{main_compare['name']} has {main_compare['searches']} and {compare_against['name']} has {compare_against['searches']}. Better luck next time!\n")
            print(f"final score: {score}")
            break

        

main()

