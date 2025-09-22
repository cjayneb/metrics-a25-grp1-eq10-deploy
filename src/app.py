#File for testing purposes only
#Run app.py localy and visit localhost to navigate or test the API
#Use: pip install flask flask-swagger-ui requests pytest

from flask import Flask, jsonify, send_from_directory
import requests
import os
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv() 
app = Flask(__name__)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/repos/cjayneb/metrics-a25-grp1-eq10"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

SWAGGER_URL = '/docs'
SWAGGER_API_URL = '/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    SWAGGER_API_URL,
    config={'app_name': "Kanban Metrics API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.yaml')
def swagger_yaml():
    return send_from_directory('.', 'swagger.yaml')

@app.route("/")
def home():
    return {"message": "Kanban Metrics API is running"}

@app.route("/issues", methods=["GET"])
def get_issues():
    r = requests.get(f"{GITHUB_API_URL}/issues?state=all", headers=headers)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True)