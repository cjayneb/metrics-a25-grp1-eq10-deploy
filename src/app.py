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
    r = requests.get(f"{API_URL}/issues?state=all", headers=headers)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True)