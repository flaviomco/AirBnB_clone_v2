#!/usr/bin/python3
""" This script starts a web application. It takes requests
    and generates a web page
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ This function loads the list of states
    and creates the web page
    """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states.values())


@app.teardown_appcontext
def close_session(self):
    """ This function closes a session
    with the storage.close() method
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
