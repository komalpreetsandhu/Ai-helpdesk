print("Welcome to IT Support System")

issue = input("Enter your problem: ")

with open("tickets.txt", "a") as file:
    file.write(issue + "\n")

print("Ticket created successfully!")