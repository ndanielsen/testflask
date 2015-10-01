"""
Hello world on heroku
"""

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Samra, you're doing a great so far!"