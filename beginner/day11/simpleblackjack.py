import random


def new_deck():
    cards = []
    for i in range(2,11):
        for j in range(4):
            cards.append(i)
    
    for jack in range(4):
        cards.append("Jack")
    for jack in range(4):
        cards.append("Queen")
    for jack in range(4):
        cards.append("King")
    for jack in range(4):
        cards.append("Ace")
    
    return cards

def shuffle_deck(fresh_deck):
    random.shuffle(fresh_deck)
    return fresh_deck

def win(bet):
    print("congratutalions, you won!")
    return bet * 2

def bust(bet):
    print("better luck next time.")
    return 0

def push(bet):
    print("It's a tie!")
    return bet

def blackjack(bet):
    print("We have a blackjack!")
    return bet * 2.5

def deal(shuffled_deck):
    
    while True:
        if len(shuffled_deck) > 4:
            house.append(shuffled_deck[0])
            shuffled_deck.pop(0)
            player.append(shuffled_deck[0])
            shuffled_deck.pop(0)
            house.append(shuffled_deck[0])
            shuffled_deck.pop(0)
            player.append(shuffled_deck[0])
            shuffled_deck.pop(0)
            
            break
        else:
            deck = new_deck()
            shuffled = shuffle_deck(deck)
            shuffled_deck = shuffled

def clear_hand():
    player.clear()
    house .clear()

def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card in ["Jack", "Queen", "King"]:
            value += 10
        elif card == "Ace":
            value += 11
            aces += 1
        else:
            value += card

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

def main_game(funds, deck):
    global player
    global house

    try:
        bet = int(input("Place your bet. > "))
        if bet <= 0:
            print("Invalid bet.")
            return funds
        elif bet > funds:
            print("Your bet can't be more than your available funds.")
            return funds
    except ValueError:
        print("Only numeric values are accepted.")
        return funds

    funds -= bet

    player_hand_value = hand_value(player)
    house_hand_value = hand_value(house)

    print(f"Player's hand: {player} -> {player_hand_value}")
    print(f"Dealer's hand: [{house[0]}, '?']")

    # Check for initial blackjack
    player_blackjack = (player[0] in [10, "Jack", "Queen", "King"] and player[1] == "Ace") or \
                       (player[1] in [10, "Jack", "Queen", "King"] and player[0] == "Ace")

    house_blackjack = (house[0] in [10, "Jack", "Queen", "King"] and house[1] == "Ace") or \
                      (house[1] in [10, "Jack", "Queen", "King"] and house[0] == "Ace")

    if player_blackjack:
        print(f"Dealer's hand: {house} -> {house_hand_value}")
        if house_blackjack:
            funds += push(bet)
        else:
            funds += blackjack(bet)
        return funds

    # Player's turn
    while True:
        hit_or_stay = input("Hit or stay? h / s > ").lower()
        if hit_or_stay == "h":
            player.append(deck.pop(0))
            player_hand_value = hand_value(player)
            print(f"Player hits: {player} -> {player_hand_value}")
            if player_hand_value > 21:
                bust(bet)
                return funds
        elif hit_or_stay == "s":
            print(f"Player stays at {player_hand_value}")
            break
        else:
            print("Invalid input. Enter 'h' to hit or 's' to stay.")

    # Dealer's turn
    print(f"Dealer reveals hand: {house} -> {house_hand_value}")
    while house_hand_value < 17:
        card = deck.pop(0)
        house.append(card)
        house_hand_value = hand_value(house)
        print(f"Dealer draws: {card} -> Total: {house_hand_value}")

    # Final outcome
    if house_hand_value > 21:
        funds += win(bet)
    elif house_hand_value == player_hand_value:
        funds += push(bet)
    elif house_hand_value > player_hand_value:
        bust(bet)
    else:
        funds += win(bet)

    return funds


deck = shuffle_deck(new_deck())    
house = []
player = []
player_funds = 0


print("Welcome to blackjack!")

while True:
    print("1. Deposit money\n2. Start the game\n3. Quit")
    player_choice = input("> ")

    while player_choice not in ["1", "2", "3"]:
        print("You need to select option 1, 2 or 3")
        player_choice = input("> ")


    
    if player_choice == "3":
        exit()

    elif player_choice == "1":
        try:
            deposit = int(input("Select amount to deposit: $"))
            if deposit <= 0:
                print("You need to deposit more than that!")
                continue
            player_funds += deposit
            print(f"Player balance is {player_funds}$")
        except ValueError:
            print("You can only deposit numeric values!")
    
    elif player_choice == "2":
        if player_funds <= 0:
            print("You need to deposit more money to play.")
            continue
        else:
            while True:
                clear_hand()
                deal(deck)
                player_funds = main_game(player_funds,deck)
                print(f"Your balance: ${player_funds}")
                if player_funds <= 0:
                    print("You're out of funds!")
                    break
                play_again = input("Play again? (y/n) > ").lower()
                if play_again != "y":
                    print(f"You're leaving the game with ${player_funds}.")
                    break








    


        










