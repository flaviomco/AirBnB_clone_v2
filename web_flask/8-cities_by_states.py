#!/usr/bin/python3
""" This script starts a web application. It takes requests
    and generates a web page
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    """ This function loads the list of states
    and creates the web page
    """
    states = storage.all('State')
    cities = storage.all('City')
    return render_template('8-cities_by_states.html', states=states.values(), cities=cities.values())


@app.teardown_appcontext
def close_session(self):
    """ This function closes a session
    with the storage.close() method
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
