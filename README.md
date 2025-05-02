AI-Reception Bot
A Human-in-the-Loop (HITL) AI receptionist system.

Features
AI Agent: Receives customer questions via /call.

Known Answers: Responds to known questions from a local knowledge base.

Escalation: For unknown questions, creates help requests that are escalated to a supervisor.

Supervisor Panel: Admin UI to manage help requests and mark them as resolved or unresolved.

Learning: AI automatically learns new answers from supervisor input and updates the knowledge base.

Tech Stack
Python 3

Flask

HTML + Bootstrap 5

JSON (lightweight DB)

Postman (for testing)

Setup
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/ai-reception bot.git
cd ai-reception bot
Set up the virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # (Windows) or source venv/bin/activate (Linux/macOS)
Install Flask:

bash
Copy
Edit
pip install flask
Run the app:

bash
Copy
Edit
python app.py
Test the AI agent (via Postman or curl):

bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/call -d "question=What are your working hours?"
Folder Structure
bash
Copy
Edit
frontdesk-hitl/
├── aibot.py                
├── help.json    
├── responses.json   
├── interface/
│   ├── supervisor_panel.html       
│   └── faq.html      
└── README.md             
Design Decisions
JSON for storage: Lightweight and file-based instead of a database.

Timeout Logic: Unanswered requests are marked as unresolved after 10 minutes.

Self-improvement: Supervisor inputs enrich the knowledge base.

Simple UI: Bootstrap 5 for easy readability.

Scalability
Can switch to Firebase or DynamoDB for storage.

Flask API can handle 1,000+ requests per day.

Blueprint structure for future scalability.

Potential for audio calls using LiveKit or Twilio.

Future Improvements
Add authentication for the admin panel.

Implement customer IDs and SMS callbacks.

Store historical call logs and performance metrics.


