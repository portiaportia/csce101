weekDay = input("Enter day of week: ").strip().lower()
lunchCost = 5

if weekDay == "monday" or weekDay == "mon":
    print("Mos Monday")
    lunchCost * .9
elif weekDay == "tuesday":
    print("Taco Tuesday")
    lunchCost * .8
else:
    print("We don't have any deals")
    
print(f"Your lunch costs ${lunchCost}")
print("Goodbye")