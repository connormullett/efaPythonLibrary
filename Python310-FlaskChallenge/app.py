
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/<int:c>')
def convert(c):
    return jsonify({'farhenheit': (c * 1.8) + 32})

