points = int(input("How many points are on your card? "))
if points < 100:
    bonus = points * 0.1
    print("Your bonus is 10 %")
else:
    bonus = points * 0.15
    print("Your bonus is 15 %")
points += bonus
print("You now have", points, "points")