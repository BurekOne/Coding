hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
week_day = input("Day of the week: ")
sunday = (hourly_wage * hours_worked)

if week_day == 'Sunday':
    print(f"Daily wages: {sunday * 2} euros")

else:
    print(f"Daily wages: {sunday} euros")