"""
Hello world on heroku
"""

import csv
import os
from flask import Flask

app = Flask(__name__)


def open_csv(filename):
    with open(filename, 'r') as f:
        data = csv.reader(f)
        return list(data)


@app.route('/')
def hello():
    filename = "gutenbergscifi.csv"
    data = open_csv(filename)

    return "The author is %s" % data[0][1]