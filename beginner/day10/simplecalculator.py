def simple_calculator():
    current_answer = 0

    try:
        first_num = float(input("First number: "))
    except ValueError:
        print("Use only numeric values.")
        return

    print("Available operators:\n+\n-\n*\n/")

    operator = input("Select operator: ")
    if operator not in ["+", "-", "*", "/"]:
        print("Select only usable operators")
        return

    try:
        second_num = float(input("Second number: "))
    except ValueError:
        print("Use only numeric values.")
        return

    if operator == "+":
        current_answer = first_num + second_num
    elif operator == "-":
        current_answer = first_num - second_num
    elif operator == "*":
        current_answer = first_num * second_num
    elif operator == "/":
        if second_num == 0:
            print("Cannot divide by 0")
            return
        current_answer = first_num / second_num

    print(f"Current answer: {current_answer}")

    while True:
        choice = input("Continue calculating with current value? Y/N: ").lower().strip()
        if choice not in ["y", "n"]:
            print('Use only "y" as YES or "n" as NO')
            continue
        elif choice == "n":
            print(f"Final answer: {current_answer}")
            break

        print("Available operators:\n+\n-\n*\n/")
        operator = input("Select operator: ")
        if operator not in ["+", "-", "*", "/"]:
            print("Select only usable operators")
            continue

        try:
            second_num = float(input("Second number: "))
        except ValueError:
            print("Use only numeric values.")
            continue

        if operator == "+":
            current_answer += second_num
        elif operator == "-":
            current_answer -= second_num
        elif operator == "*":
            current_answer *= second_num
        elif operator == "/":
            if second_num == 0:
                print("Cannot divide by 0")
                continue
            current_answer /= second_num

        print(f"Current answer: {current_answer}")


# Run the calculator
simple_calculator()
