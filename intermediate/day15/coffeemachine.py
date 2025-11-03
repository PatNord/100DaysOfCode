#prompt user what they would like to drink (coffee/latte/capuccino)
#turn off the machine by writing off to prompt
#print report of coffee machines resource values
#check resource sufficients (is there enough stuff to make the chosen beverage)
#process coins (count them, give change)
#make the coffee 


water = 1000 #ml
milk = 1000 #ml
coffee = 1000 #g


def fill_the_machine():
    global water, milk, coffee

    water = 1000 #ml
    milk = 1000 #ml
    coffee = 1000 #g

    

def report(money):
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nFunds: {money}")

def insert_funds():
    inserted_coins = 0
    while True:
        print("insert coins:\n1. 1¢\n2. 5¢\n3. 10¢\n4. 25¢\n5. 50¢\n6. 1$\n7. OK")
        coin = input("> ").strip().lower()
        if coin not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Use only given choices!")
            continue
        elif coin == "1":
            inserted_coins += 0.01
            print("**********************************")
            print(f"Current balance: {inserted_coins:.2f}")
            print("**********************************")
        elif coin == "2":
            inserted_coins += 0.05
            print("**********************************")
            print(f"Current balance: {inserted_coins:.2f}")
            print("**********************************")
        elif coin == "3":
            inserted_coins += 0.1
            print("**********************************")
            print(f"Current balance: {inserted_coins:.2f}")
            print("**********************************")
        elif coin == "4":
            inserted_coins += 0.25
            print("**********************************")
            print(f"Current balance: {inserted_coins:.2f}")
            print("**********************************")
        elif coin == "5":
            inserted_coins += 0.5
            print("**********************************")
            print(f"Current balance: {inserted_coins:.2f}")
            print("**********************************")
        elif coin == "6":
            inserted_coins += 1
            print("**********************************")
            print(f"Current balance: {inserted_coins:.2f}")
            print("**********************************")
        elif coin == "7":
            print("**********************************")
            print(f"Current balance: {inserted_coins:.2f}")
            print("**********************************")
            return inserted_coins

def check_funds(price, money):
    product_name, product_price = price
    if float(product_price) > float(money):
        return False
    else:
        return True
    
def check_ingredients(product):
    global water, milk, coffee

    recipes = {
        "Coffee": {"water": 100, "milk": 0, "coffee": 20},
        "Latte": {"water": 50, "milk": 150, "coffee": 20},
        "Capuccino": {"water": 50, "milk": 100, "coffee": 20}
    }

    recipe = recipes[product]

    if water < recipe["water"]:
        print("Error! not enough water!")
        return False
    elif milk < recipe["milk"]:
        print("Error! not enough milk!")
        return False
    elif coffee < recipe["coffee"]:
        print("Error! not enough coffee!")
        return False
    else:
        return True
    
def make_coffee(product):
    global water, milk, coffee

    recipes = {
        "Coffee": {"water": 100, "milk": 0, "coffee": 20},
        "Latte": {"water": 50, "milk": 150, "coffee": 20},
        "Capuccino": {"water": 50, "milk": 100, "coffee": 20}
    }

    recipe = recipes[product]

    water -= recipe["water"]
    milk -= recipe["milk"]
    coffee -= recipe["coffee"]
    print(f"Making {product}...")


def select_coffee():
     while True:
        print(f"products:\n1. Coffee 2$\n2. Latte 2.50$\n3. Capuccino 3.25$")
        choice = input("> ").strip().lower()
        if choice not in ["1", "2", "3", "off", "report", "refill"]:
                print("Use only given options!")
        elif choice == "1":
            return "Coffee", 2.00
        elif choice == "2":
            return "Latte", 2.50
        elif choice == "3":
            return "Capuccino", 3.25
        elif choice == "off":
            return "off", 0
        elif choice == "report":
            return "report", 0
        elif choice == "refill":
            return "refill", 0



def main():
    funds = 0
    print("Insert coins to start.")
    money = insert_funds()
    
    while True:
        selection = select_coffee()

        if selection[0] == "off":
            print("Goodbye!")
            break
        elif selection[0] == "report":
            report(money)
            continue
        elif selection[0] == "refill":
            fill_the_machine()
            print("Machine full!")
            continue
        else:
            if not check_funds(selection, money):
                print("Not enough funds!")
                while True:
                    want_to_continue = input("1. insert more money 2. exit").strip()
                    if want_to_continue not in ["1", "2"]:
                        continue
                    elif want_to_continue == "1":
                        money += insert_funds()
                        break
                    else:
                        print(f"{money}$ returned!")
                        exit()
            if not check_ingredients(selection[0]):
                print("Not enough ingredients! Machine needs to be refilled to continue!")
                continue
            else:
                make_coffee(selection[0])
                money -= selection[1]
                if money == 0:
                    print("Enjoy your coffee!")
                else:
                    print(f"Change {money:.2f}$. Enjoy your coffee!")
                break

main()