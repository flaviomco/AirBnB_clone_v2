#!/usr/bin/python3
""" This module contains a Flask instance
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def first_task():
    """ This function returns a string
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
