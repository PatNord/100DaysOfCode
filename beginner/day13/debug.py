# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            continue
        elif number % 3 == 0:
            print("Fizz")
            continue
        elif number % 5 == 0:
            print("Buzz")
            continue
        else:
            print(number)


fizz_buzz(20)