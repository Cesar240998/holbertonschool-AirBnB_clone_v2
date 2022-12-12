#!/usr/bin/python3
"""Script to starts a Flask web application and use storage for fetching data from the storage engine"""
from flask import Flask, render_template
from markupsafe import escape
from models.state import State
from models.city import City
from models import storage
from models.amenity import Amenity
from models.state import State
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def cities_states(id=''):
    """Display a HTML page like 6-index.html"""
    amenities = list(storage.all(Amenity).values())
    states = list(storage.all(State).values())

    return (render_template('/10-hbnb_filters.html', amenities=amenities, states=states))

@app.teardown_appcontext
def close_session(self):
    """This method remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
