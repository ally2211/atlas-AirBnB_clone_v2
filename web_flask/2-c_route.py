#!/usr/bin/python3
""" Import the Flask module"""
from flask import Flask

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


""" The server only starts if the script is executed directly"""
if __name__ == "__main__":
    # Run the Flask application on host '0.0.0.0' and port '5000'
    app.run(host='0.0.0.0', port=5000)
