print("Welcome to the tip calculator!")
amount = float(input("What was the total of the bill? $"))
tip = int(input("How much tip would you like to give? %"))
people = int(input('How many people to split the bill? '))

calculatedTip = (tip / 100) * amount / people

print(f"Each person should pay: {round(calculatedTip, 2)}$ ")




