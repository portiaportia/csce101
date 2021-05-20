
while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    if command == "q":
        break           # breaks you out of the loop
    elif command == "p":
        print("Random fortune")
    else:
        print("Invalid input")
        
print("Goodbye")
    