from flask import Flask, request, render_template, render_template_string, session
from pymongo import MongoClient
import subprocess

app = Flask(__name__)
app.secret_key = "supersecretkey"

client = MongoClient("mongodb://localhost:27017/")
db = client.vuln_db
users = db.users

@app.route("/")
def home():
    return render_template("index.html")

# NoSQL Injection (Vulnerable)
@app.route("/nosql", methods=["POST"])
def nosql_injection():
    username = request.form.get("username")
    password = request.form.get("password")
    user = users.find_one({"username": username, "password": password})
    if user:
        return "Login successful!"
    return "Login failed."

# NoSQL Injection (Secure Fix)
@app.route("/nosql_secure", methods=["POST"])
def nosql_secure():
    username = request.form.get("username")
    password = request.form.get("password")
    if not isinstance(username, str) or not isinstance(password, str):
        return "Invalid input."
    user = users.find_one({"username": username, "password": password})
    if user:
        return "Login successful!"
    return "Login failed."

# IDOR
@app.route("/idor", methods=["GET"])
def idor():
    user_id = request.args.get("user_id")
    user = users.find_one({"_id": user_id})
    return str(user)

# XSS
@app.route("/xss", methods=["POST"])
def xss():
    comment = request.form.get("comment")
    return f"<h3>Your comment:</h3> {comment}"

# CSRF
@app.route("/csrf", methods=["POST"])
def csrf():
    if "balance" not in session:
        session["balance"] = 1000
    session["balance"] -= 100
    return f"Balance updated: {session['balance']}"

# Code Injection
@app.route("/code_injection", methods=["POST"])
def code_injection():
    cmd = request.form.get("command")
    output = subprocess.check_output(cmd, shell=True).decode()
    return f"<pre>{output}</pre>"

# SSTI
@app.route("/ssti", methods=["POST"])
def ssti():
    user_input = request.form.get("template")
    return render_template_string(user_input)

if __name__ == "__main__":
    app.run(debug=True)
