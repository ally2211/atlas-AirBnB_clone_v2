#!/usr/bin/python3
""" Import the Flask module"""
from flask import Flask, render_template

""" Create an instance of the Flask class"""
app = Flask(__name__)


"""set strict slashes to false"""
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    # Replace underscores with spaces in the text
    text_with_spaces = text.replace("_", " ")
    return "C " + text_with_spaces


@app.route('/python/<text>')
def python_is_magic(text='is cool'):
    # Replace underscores with spaces in the text
    text_with_spaces = text.replace("_", " ")
    return "Python " + text_with_spaces


@app.route('/number/<int:n>')
def show_number(n):
    return '%d is a number' % n


@app.route('/number_template/<int:number>')
def number_template(number):
    return render_template("5-number.html", number=number)


@app.route('/number_odd_or_even/<int:number>')
def number_odd_or_even(number):
    if (number % 2 == 0):
        evenodd = "even"
    else:
        evenodd = "odd"
    return render_template("6-number_odd_or_even.html",
                           number=number, evenodd=evenodd)


""" The server only starts if the script is executed directly"""
if __name__ == "__main__":
    # Run the Flask application on host '0.0.0.0' and port '5000'
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
