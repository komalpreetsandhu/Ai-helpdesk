from datetime import datetime

print("=== IT Support System ===")
print("1. Create Ticket")
print("2. View Tickets")

choice = input("Choose option: ")

if choice == "1":
    issue = input("Enter your problem: ")

    if "server" in issue.lower() or "network" in issue.lower():
        priority = "HIGH"
    else:
        priority = "NORMAL"

    ticket_id = datetime.now().strftime("%Y%m%d%H%M%S")

    with open("tickets.txt", "a") as file:
        file.write(f"ID: {ticket_id} | Issue: {issue} | Priority: {priority} | Status: OPEN\n")

    print(f"Ticket created! ID: {ticket_id}")

elif choice == "2":
    with open("tickets.txt", "r") as file:
        print("\n--- All Tickets ---")
        print(file.read())