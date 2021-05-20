import random

totalGames = 0
score = 0

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "p":
        totalGames += 1
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        product = num1 * num2
        
        userAnswer = int(input(f"{num1} * {num2} = "))
        
        if userAnswer == product:
            print("YAY!")
            score += 1
        else:
            print(f"Sorry, the answer is {product}")
    else:
        print("Invalid input")
        
print("Goodbye")
print(f"You won {score} games out of {totalGames}")