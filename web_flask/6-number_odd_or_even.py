#!/usr/bin/python3
"""Script to starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    """Return message HBNB"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    """Display C followed by text"""
    return ('C {:s}'.format(escape(text)).replace('_', ' '))


@app.route("/python/<string:text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def variable_text_default(text="is cool"):
    """Return text variable with default"""
    new_text = text.replace('_', ' ')
    return ('Python {:s}'.format(escape(new_text)))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """number_route"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """number_template"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even(n):
    """Display a HTML page only if n is a integer and is even or odd"""
    return render_template('6-number_odd_or_even.html', num_2=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
