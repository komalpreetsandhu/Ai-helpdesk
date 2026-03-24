# AI IT Support System (Web Version)

A **web-based IT Support System** with AI-powered suggestions and a professional dashboard.  
This project simulates real-world IT support workflows and is ideal for portfolio use.

---

## 🚀 Features

- **Simulated AI Suggestions** – Provides advice for common IT problems like VPN, printer, network, and password issues.
- **Ticket System** – Automatically creates tickets when AI cannot solve the issue.
- **Ticket Management** – Tickets have ID, Issue, Priority (HIGH/NORMAL), and Status (OPEN/CLOSED).
- **Close Ticket Functionality** – Mark tickets as CLOSED directly from the dashboard.
- **Professional Dashboard** – Colored badges for priority and status, AI suggestion box, and clean UI.
- **Fully Local and Free** – No API keys required.

---


## 📂 Project Structure

- **ai-helpdesk/**
  - `app.py` – Flask backend
  - `tickets.txt` – Ticket storage
  - `requirements.txt` – Dependencies
  - `README.md` – Project description
  - **templates/**
    - `index.html` – Webpage
  - **static/**
    - `style.css` – CSS for UI
---

## 💻 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/komalpreetsandhu/Ai-helpdesk.git
cd Ai-helpdesk
Install dependencies:
pip install -r requirements.txt
Run the app:
python app.py
Open in browser:
http://127.0.0.1:5000

🖥️ Usage
Enter your IT problem in the input box (e.g., “VPN not working”).
AI will provide a suggestion if it recognizes the issue.
If AI cannot solve the issue, a ticket is automatically created.
Tickets appear in the table below with ID, Issue, Priority, Status.
Click Close Ticket to mark a ticket as CLOSED.

🎨 UI Highlights
AI suggestions are displayed in a highlighted box.
Priority badges:
HIGH → Red
NORMAL → Green
Status badges:
OPEN → Yellow
CLOSED → Cyan
Clean professional table and responsive layout.

Tech Stack
Python 3.x
Flask – Web framework
HTML/CSS – Frontend
Jinja2 – Template rendering
🌟 Future Improvements
Add real AI integration (OpenAI API) for dynamic responses.
Add user authentication for multiple technicians.
Add ticket filtering by priority or status.
Deploy as an online web portal using Heroku, Render, or GitHub Pages (frontend only).
📌 Author

Komalpreet Sandhu – Portfolio Project
