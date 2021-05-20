import random

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    if command == "q":
        break           # breaks you out of the loop
    elif command == "p":
        num = random.randint(0,5)
        #print(f"{num}")

        if num == 0:
            print("You will have a wonderful life")
        elif num == 1:
            print("You will be famous")
        elif num == 2:
            print("You will eat a cookie")
        elif num == 3:
            print("You will get a bird")
        elif num == 4:
            print("You are a dog")
        elif num == 5:
            print("Your life wil be special")
        else:
            print("What?")
    else:
        print("Invalid input")
        
print("Goodbye")
    