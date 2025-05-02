# Frontdesk HITL AI Supervisor

A simple Flask-based simulation of a Human-in-the-Loop (HITL) AI receptionist system, designed for handling customer interactions with AI assistance and supervisor escalation.

## Features
- **AI Receptionist**: Handles incoming customer queries via `/call`.
- **Knowledge Base**: Responds to known questions stored in a local knowledge base.
- **Escalation Process**: If the AI can't answer, it creates a help request that gets escalated to a supervisor.
- **Admin Panel**: A simple UI to manage help requests, mark them as resolved or unresolved, and view the knowledge base.
- **Learning**: Supervisors can add answers to the knowledge base, allowing the AI to learn and improve.

## Tech Stack
- Python 3
- Flask
- HTML + Bootstrap 5
- JSON (lightweight database)
- Postman (for testing)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/frontdesk-hitl.git
   cd frontdesk-hitl
Set up the virtual environment:

bash
Always show details

Copy
python -m venv venv
venv\Scripts\activate  # (Windows) or source venv/bin/activate (Linux/macOS)
Install dependencies:

bash
Always show details

Copy
pip install flask
Run the application:

bash
Always show details

Copy
python app.py
Test the AI agent (via Postman or curl):

bash
Always show details

Copy
curl -X POST http://127.0.0.1:5000/call -d "question=What are your working hours?"
Folder Structure
bash
Always show details

Copy
frontdesk-hitl/
├── app.py                # Flask server
├── help_requests.json    # Help request data (simulated DB)
├── knowledge_base.json   # Knowledge base for AI
├── templates/
│   ├── admin.html        # Admin panel UI
│   └── learned.html      # View for learned answers
└── README.md             # This README file
Design Considerations
File-based Storage: Uses JSON files instead of a database for simplicity and lightweight storage.

Timeout Feature: Requests are marked as unresolved if unanswered for more than 10 minutes.

Learning from Supervisor: Supervisor answers enrich the AI’s knowledge base.

UI Design: Simple, clean, and responsive using Bootstrap 5 for quick accessibility.

Scalability Notes
Easily replace JSON with Firebase or DynamoDB for production-level storage.

The system is designed to scale and can handle 1,000+ requests per day.

Future improvements can include Flask blueprints for modularity and integrations like LiveKit or Twilio for real-time call audio.

Planned Improvements
Authentication: Secure the admin panel with login functionality.

Customer Interaction: Implement customer IDs and SMS callback features.

Call Logs & Metrics: Store historical data for performance tracking and analytics.
