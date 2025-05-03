# AI-ReceptionBot

This project demonstrates how an AI receptionist can escalate unfamiliar queries to a human supervisor, follow up with customers, and continuously update its internal knowledge base.

## Features
- **Automated Responses**: Handles incoming customer queries via a RESTful API.
- **Knowledge Base**: Responds to known questions stored in a local knowledge base.
- **Human Escalation**: Escalates unanswered questions to human supervisors.
- **Faq_Panel**: Manage help requests, mark them as resolved/unresolved, and update the knowledge base.
- **Continuous Learning**: Learns from supervisor inputs to enhance future responses.

## Tech Stack
Python 3
Flask
HTML + Bootstrap 
JSON (as a lightweight DB)
Postman (to simulate customer calls)

##Setup Instructions
Clone the repo
git clone https://github.com/yourusername/frontdesk-hitl.git
cd frontdesk-hitl
Set up virtual environment
python -m venv venv
venv\Scripts\activate  # (Windows) or source venv/bin/activate (Linux/macOS)
pip install flask
Run the app
 python app.py
Test the AI agent (via Postman or curl)

Example with curl:

curl -X POST http://127.0.0.1:5000/call -d "question=What are your working hours?"
📂 Folder Structure
frontdesk-hitl/
│
├── app.py                 # Flask server
├── help_requests.json     # Simulated DB of help tickets
├── knowledge_base.json    # Simulated knowledge base
├── templates/
│   ├── admin.html         # Admin panel
│   └── learned.html       # Learned answers viewer
└── README.md              # You're reading it

🧠 Design Decisions
JSON was used instead of a database to keep things lightweight and file-based.
Timeout logic automatically marks unanswered requests as "unresolved" after 10 minutes.
Supervisor answers directly enrich the knowledge base, allowing the AI to self-improve.
Admin UI is kept simple but clean using Bootstrap 5 for fast readability and UX.
Code is modularized for scalability — separate logic for data handling, routes, and UI.
📈 Scalability Notes
Easily extensible to use Firebase or DynamoDB in place of JSON files.
Can scale up to 1,000+ requests/day with lightweight API-backed architecture.
Flask blueprints could be introduced to isolate modules.
LiveKit or Twilio integration would enable real-time call audio in the future.
🙋‍♂️ What I'd Improve Next
Add authentication to the admin panel.
Implement customer ID tagging and actual SMS callbacks.
Store historical call logs and supervisor performance metrics.
