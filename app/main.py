import os
import random
import json

from flask import Flask
from flask import jsonify
from flask import render_template
from json.decoder import JSONDecodeError

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/skills")
def skills():
    data, err = read_data(f"{os.getcwd()}/app/data/db.json")
    if err:
        return jsonify({"skill": "Fallback skills"})

    return jsonify(random.choice(data))

def read_data(source):
    data = []
    errors = []
    try:
        with open(source, encoding="utf8") as db:
            content = db.read()
        data = json.loads(content)
    except FileNotFoundError as err:
        errors = [f"Reading {source}, {str(err)}"]
    except JSONDecodeError as err:
        errors = [f"Reading {source}, {str(err)}"]
    except Exception as err:
        errors = [f"Reading {source}, {str(err)}"]

    return data, errors
