#!/usr/bin/python3
"""
Initialize a Flask application with state_list
(all states or one state depending of URL), using the Storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from markupsafe import escape

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<string:id>", strict_slashes=False)
def states(id=''):
    """Display cities by states (one or all or nothing)"""
    exist = 1
    escaped_id = escape(id)

    if (escaped_id == ''):
        values = list(storage.all(State).values())
        return (render_template('/9-states.html', states=values,
                                exist=exist, id=escaped_id))
    else:
        values = [storage.all(State).get('State.{:s}'.format(escaped_id))]

    if (values[0] is None):
        exist = 0

    return (render_template('/9-states.html', states=values,
                            exist=exist, id=escaped_id))


@app.teardown_appcontext
def close_session(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
