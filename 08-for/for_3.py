# get a number from the user and calculate the factorial
# e.g. 5! = 5 * 4 * 3 * 2 * 1 = 120

num = int(input("Enter a number: "))
product = 1

for i in range(1,num + 1):
    product *= i
    
print(f"{num}! = {product}")