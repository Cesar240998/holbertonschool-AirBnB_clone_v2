#!/usr/bin/python3
"""Script to starts a Flask web application and use storage for
fetching data from the storage engine"""
from flask import Flask, render_template
from markupsafe import escape
from models.state import State
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """This method display list of all State present in DBStorage
    sorted by name"""
    values = storage.all(State).values()
    return (render_template("7-states_list.html", states=values))


@app.teardown_appcontext
def close_session(self):
    """This method remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
