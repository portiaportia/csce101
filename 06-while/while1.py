color = input("Guess my favorite color: ").strip().lower()

while color != "pink":
    print("wrong")
    color = input("Guess again: ").strip().lower()
    
print("Nice!")