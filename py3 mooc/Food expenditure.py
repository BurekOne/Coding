cafeteria = int((input("How many times a week do you eat at the student cafeteria? ")))
lunchPrice = float((input("The price of a typical student lunch? ")))
weeklyGroceries = float((input("How much money do you spend on groceries in a week? ")))
weekly = cafeteria * lunchPrice + weeklyGroceries
print("Average food expenditure:")
print(f"Daily: {weekly / 7} euros")
print(f"Weekly: {weekly} euros")


# weekly = ((cafeteria * lunchPrice) + weeklyGroceries)
# daily = weekly / 7