#!/usr/bin/python3
"""
Script that starts a Flask web application:

Web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display "HBNB"
/c/<text>: display “C ” followed by the value of the text variable
/python/(<text>): display “Python ”, followed by the value of the text variable
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
        - H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask
from urllib.parse import unquote
from markupsafe import escape
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<path:text>")
def c(text):
    text = unquote(text.replace("_", " "))
    return "C {}".format(escape(text))


@app.route("/python/", defaults={"text": "is_cool"})
@app.route("/python/<path:text>")
def python(text):
    text = unquote(text.replace("_", " "))
    return "Python {}".format(escape(text))


@app.route("/number/<int:n>")
def number(n):
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
