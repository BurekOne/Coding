name = input("Please tell me your name: ")
if name == 'Jerry':
    print("Next please!")
    exit()
if name != "Jerry":
    soupPortions = int(input("How many portions of soup? "))
    singlePortion = float(5.90)
    totalCost = singlePortion * soupPortions
    print(f"The total cost is {totalCost}")
    print("Next please!")