import requests
import os
from flask import Flask, jsonify, send_from_directory
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv() 

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/repos/cjayneb/metrics-a25-grp1-eq10"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

SWAGGER_URL = '/docs'
SWAGGER_API_URL = '/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    SWAGGER_API_URL,
    config={'app_name': "Kanban Metrics API"}
)

app = Flask(__name__)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.yaml')
def swagger_yaml():
    return send_from_directory('.', 'swagger.yaml')

@app.route("/")
def home():
    return {"message": "Kanban Metrics API is running"}

@app.route("/issues", methods=["GET"])
def get_issues():
    r = requests.get(f"{GITHUB_API_URL}/issues?state=all", headers=HEADERS)
    issues = r.json()

    result = []

    for issue in issues:
        milestone = issue.get("milestone")
        temp_issue = {
            "id": issue.get("id"),
            "number": issue.get("number"),
            "title": issue.get("title"),
            "state": issue.get("state"),
            "user": issue["user"]["login"] if issue.get("user") else None,
            "assignees": [a["login"] for a in issue.get("assignees", [])],
            "labels": [lbl["name"] for lbl in issue.get("labels", [])],
            "milestone": {
                "number": milestone.get("number"),
                "title": milestone.get("title"),
                "state": milestone.get("state"),
                "due_on": milestone.get("due_on"),
            } if milestone else None,
            "created_at": issue.get("created_at"),
            "updated_at": issue.get("updated_at"),
            "closed_at": issue.get("closed_at"),
        }
        result.append(temp_issue)

    return jsonify(result)

if __name__ == "__main__": # pragma: no cover (do not consider for code coverage)
    app.run()