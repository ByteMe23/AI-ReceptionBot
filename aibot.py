from flask import Flask, request, render_template, redirect
import json
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)

HELP_REQUESTS_FILE = 'help_requests.json'
KB_FILE = 'knowledge_base.json'

try:
    with open(KB_FILE, 'r') as kb_file:
        knowledge_base = json.load(kb_file)
except FileNotFoundError:
    knowledge_base = {}

try:
    with open(HELP_REQUESTS_FILE, 'r') as f:
        help_requests = json.load(f)
except FileNotFoundError:
    help_requests = []

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    return "Frontdesk AI System Running!"

@app.route('/call', methods=['POST'])
def simulate_call():
    question = request.form.get("question", "").strip().lower()
    print(f"\n📞 Incoming customer question: {question}")

    if question in knowledge_base:
        answer = knowledge_base[question]
        print(f"✅ AI Response: {answer}")
        return f"AI: {answer}"

    print("⚠️ AI: Let me check with my supervisor and get back to you.")

    help_requests.append({
        "id": str(uuid.uuid4()),
        "question": question,
        "status": "pending",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "response": None
    })

    save_json(help_requests, HELP_REQUESTS_FILE)
    print(f"📲 [Supervisor Notification]: Hey, I need help answering: '{question}'")
    return "AI: Let me check with my supervisor and get back to you."

@app.route('/admin')
def admin_panel():
    now = datetime.now()
    timeout = timedelta(minutes=10)

    for req in help_requests:
        if req["status"] == "pending":
            req_time = datetime.strptime(req["timestamp"], "%Y-%m-%d %H:%M:%S")
            if now - req_time > timeout:
                req["status"] = "unresolved"
                print(f"⏰ Request '{req['question']}' marked as unresolved due to timeout.")

    save_json(help_requests, HELP_REQUESTS_FILE)
    return render_template('admin.html', help_requests=help_requests)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    request_id = request.form.get("request_id")
    answer = request.form.get("answer")

    for req in help_requests:
        if req["id"] == request_id:
            req["status"] = "resolved"
            req["response"] = answer
            knowledge_base[req["question"]] = answer
            print(f"\n📩 AI Follow-up: Texting customer back: '{answer}'")
            break

    save_json(help_requests, HELP_REQUESTS_FILE)
    save_json(knowledge_base, KB_FILE)
    return redirect('/admin')

@app.route('/learned')
def learned_answers():
    return render_template('learned.html', kb=knowledge_base)

if __name__ == '__main__':
    app.run(debug=True)
