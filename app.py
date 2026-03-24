from datetime import datetime

# 🤖 Simulated AI function
def ask_ai(issue):
    issue = issue.lower()

    if "vpn" in issue:
        return "Try reconnecting your VPN and check your internet connection."
    elif "password" in issue:
        return "Use the 'Forgot Password' option to reset your password."
    elif "printer" in issue:
        return "Restart the printer and reconnect it to your computer."
    elif "network" in issue:
        return "Check your router and restart your network connection."
    elif "slow" in issue:
        return "Try restarting your computer and closing unused programs."
    else:
        return "I'm not sure about this issue."

# 🎫 Function to create ticket
def create_ticket(issue):
    # Set priority
    if "server" in issue.lower() or "network" in issue.lower():
        priority = "HIGH"
    else:
        priority = "NORMAL"

    # Create unique ticket ID
    ticket_id = datetime.now().strftime("%Y%m%d%H%M%S")

    # Save to file
    with open("tickets.txt", "a") as file:
        file.write(f"ID: {ticket_id} | Issue: {issue} | Priority: {priority} | Status: OPEN\n")

    print(f"\n✅ Ticket created successfully! ID: {ticket_id}")

# 📄 Function to view tickets
def view_tickets():
    try:
        with open("tickets.txt", "r") as file:
            print("\n📋 --- All Tickets ---")
            print(file.read())
    except FileNotFoundError:
        print("\n⚠️ No tickets found yet.")

# 🚀 Main program
while True:
    print("\n=== IT Support System ===")
    print("1. Ask for Help (AI)")
    print("2. View Tickets")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        issue = input("\nEnter your problem: ")

        print("\n🤖 Checking solution...\n")
        response = ask_ai(issue)

        print("💡 Suggestion:", response)

        if "not sure" in response.lower():
            user_choice = input("\nDo you want to create a ticket? (yes/no): ")

            if user_choice.lower() == "yes":
                create_ticket(issue)
        else:
            user_choice = input("\nDid this solve your issue? (yes/no): ")

            if user_choice.lower() == "no":
                create_ticket(issue)

    elif choice == "2":
        view_tickets()

    elif choice == "3":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")