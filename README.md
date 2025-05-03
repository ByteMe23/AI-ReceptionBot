# AI-ReceptionBot

This project demonstrates how an AI receptionist can escalate unfamiliar queries to a human supervisor, follow up with customers, and continuously update its internal knowledge base.

## Features
- **Automated Responses**: Handles incoming customer queries via a RESTful API.
- **Knowledge Base**: Responds to known questions stored in a local knowledge base.
- **Human Escalation**: Escalates unanswered questions to human supervisors.
- **Faq_Panel**: Manage help requests, mark them as resolved/unresolved, and update the knowledge base.
- **Continuous Learning**: Learns from supervisor inputs to enhance future responses.

## Tech Stack
- **Python**
- **Flask**
- **HTML + Bootstrap**
- **JSON**
- **Postman**

## Setup Instructions
1. Clone the repo
   ```bash
   git clone https://github.com/yourusername/ai-receptionbot.git
   cd ai-receptionbot
   ```
2. Set up virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate  # (Windows) or source venv/bin/activate (Linux/macOS)
   pip install flask
   ```

4. Run the app
   ```bash
   aibot.py
   ```

5. Test the AI agent 
```bash
  curl -X POST http://127.0.0.1:5000/call -d "question=Write your question here?"
```

## Extensibility
- **The system is easily extensible to support databases like Firebase or Amazon DynamoDB instead of local JSON files.**
- **Built to handle high-throughput usage with minimal latency—ideal for production workloads and 1K+ daily requests.**
- **Modular architecture can be further improved using Flask Blueprints to separate concerns and isolate functionality.**
- **Future integration with LiveKit or Twilio would enable real-time audio calls, enhancing the agent’s interactivity.**

## Future Improvements
- **Add authentication to secure the admin panel.**
- **Implement customer ID tagging and enable real SMS callbacks for improved tracking and communication.**
- **Store historical call logs and track supervisor performance metrics for analysis and optimization.**
