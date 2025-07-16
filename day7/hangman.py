import random
import words



lives = 6
secret_word = list(random.choice(words.word_list))
dashed_word = []
guessed_letters = []

for i in range(len(secret_word)):
    dashed_word += "_"
print(f'Secret word is: {" ".join(dashed_word)}')


while lives > 0:
    player_input = input("Guess a letter: ").strip().lower()

    if player_input in guessed_letters:
        print("You guessed that already!")
        print()
        continue
    

    if len(player_input) > 1:
        print("Use only one character at a time!")
        continue
    elif not player_input.isalpha():
        print("Use only letters!")
        continue
    
    if player_input in secret_word:
        for i in range(len(secret_word)):
            if player_input == secret_word[i]:
                dashed_word[i] = player_input
        print(" ".join(dashed_word))
        guessed_letters += player_input
    
    else:
        lives -= 1
        print()
        print(f"player lives: {lives}.")
        guessed_letters += player_input
        print(f'guessed letters: {" ".join(guessed_letters)}')
        print()

    if dashed_word == secret_word:
        print("You won!")
        break
    elif lives == 0:
        print(f'secret word was: {"".join(secret_word)}')
        print("You lost!")

    





