# calculate the mean between 10 random numbers
import random

sum = 0

for i in range(10):
    num = random.randint(1, 100)
    sum += num
    print(f"{num}, ", end = "")
print()

average = sum / 10
print(f"Average: {average}")