import math

# int for whole numbers float for decimals
age = int(input("Enter age: "))
decade = 10
future_age = age + decade
print(f"Future age is {future_age}")

# Piazza Party
print("Pizza Party")
num_guests = int(input("Num Guests: "))
slices_per_guest = 2.5
total_slices = math.ceil(num_guests * slices_per_guest)
total_pizzas = math.ceil(total_slices / 8)

print(f"You need {total_slices} slices.")
print(f"You need {total_pizzas} pizzas")

# Travelling
print("Travelling")
totalMiles = float(input("Total Miles: "))
pricePerMile = float(input("Price Per Mile: "))
totalCost = totalMiles * pricePerMile
print(f"Total Cost: ${round(totalCost,2)}")

