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


@app.route('/hbnb', strict_slashes=False)
def second_task():
    """ This function returns a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def third_task(text):
    """ This function returns a string.
    It also takes a variable
    """
    return 'C %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
