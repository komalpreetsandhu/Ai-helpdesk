print("Welcome to IT Support System")

issue = input("Enter your problem: ")

if "password" in issue:
    print("Try resetting your password.")
elif "printer" in issue:
    print("Restart the printer.")
else:
    print("Issue not found. Creating ticket...")
    
    with open("tickets.txt", "a") as file:
        file.write(issue + "\n")