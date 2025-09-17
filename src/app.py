#File for testing purposes only
#Run app.py localy and visit localhost to navigate or test the API
#Use: pip install flask flask-swagger-ui requests pytest

from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv() 
app = Flask(__name__)

# set le token dans une variable locale

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

API_URL = f"https://api.github.com/repos/cjayneb/metrics-a25-grp1-eq10"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}

@app.route("/")
def home():
    return {"message": "Kanban Metrics API is running"}

@app.route("/issues", methods=["GET"])
def get_issues():
    """Return issues of the repo"""
    r = requests.get(f"{API_URL}/issues", headers=headers)
    return jsonify(r.json())

@app.route("/pulls", methods=["GET"])
def get_pulls():
    """Return pull requests of the repo"""
    r = requests.get(f"{API_URL}/pulls", headers=headers)
    return jsonify(r.json())

@app.route("/metrics/completed", methods=["GET"])
def completed_tasks():
    """Return number of closed issues"""
    r = requests.get(f"{API_URL}/issues?state=closed", headers=headers)
    issues = r.json()
    return jsonify({"completed_count": len(issues)})

if __name__ == "__main__":
    app.run(debug=True)