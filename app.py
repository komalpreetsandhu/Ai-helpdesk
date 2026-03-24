from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# --- Simulated AI ---
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

# --- Read tickets safely ---
def get_tickets():
    tickets_list = []
    try:
        with open("tickets.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split('|')
                if len(parts) != 4:
                    continue
                ticket_dict = {
                    "id": parts[0].split(": ")[1].strip(),
                    "issue": parts[1].split(": ")[1].strip(),
                    "priority": parts[2].split(": ")[1].strip(),
                    "status": parts[3].split(": ")[1].strip()
                }
                tickets_list.append(ticket_dict)
        return tickets_list
    except FileNotFoundError:
        return []

# --- Create ticket ---
def create_ticket(issue):
    if "server" in issue.lower() or "network" in issue.lower():
        priority = "HIGH"
    else:
        priority = "NORMAL"
    ticket_id = datetime.now().strftime("%Y%m%d%H%M%S")
    with open("tickets.txt", "a") as file:
        file.write(f"ID: {ticket_id} | Issue: {issue} | Priority: {priority} | Status: OPEN\n")

# --- Close ticket ---
def close_ticket(ticket_id):
    tickets = get_tickets()
    with open("tickets.txt", "w") as file:
        for t in tickets:
            if t["id"] == ticket_id:
                t["status"] = "CLOSED"
            file.write(f'ID: {t["id"]} | Issue: {t["issue"]} | Priority: {t["priority"]} | Status: {t["status"]}\n')

# --- Flask route ---
@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    if request.method == "POST":
        if "issue" in request.form:  # AI form submitted
            issue = request.form["issue"]
            ai_response = ask_ai(issue)
            if "not sure" in ai_response.lower():
                create_ticket(issue)
            response = ai_response
        elif "close_id" in request.form:  # Close ticket form submitted
            close_ticket(request.form["close_id"])
            return redirect(url_for('home'))

    tickets = get_tickets()
    return render_template("index.html", response=response, tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)