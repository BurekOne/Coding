number_one = int(input("Number 1: "))
number_two = int(input("Number 2: "))
number_operation = input("Operation: ")

if number_operation == 'add':
    print()
    print(f"{number_one} + {number_two} =", number_one + number_two)

if number_operation == 'multiply':
    print()
    print(f"{number_one} * {number_two} =", number_one * number_two)

if number_operation == 'subtract':
    print()
    print(f"{number_one} - {number_two} =", number_one - number_two)