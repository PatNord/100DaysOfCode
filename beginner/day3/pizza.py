#Practice file for if, elif and else statements. 
amount = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower().strip()
if size in ["s","m","l"]:
    if size == "s":
        amount += 15
    elif size == "m":
        amount += 20
    else: 
        amount += 25


pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower().strip()
if pepperoni == "y":
    amount += 5


extra_cheese = input("Do you want extra cheese? Y or N: ").lower().strip()

if extra_cheese == "y":
    amount += 3

print(f"Your total will be {amount}$")