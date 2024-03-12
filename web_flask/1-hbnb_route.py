#!/usr/bin/python3
""" Import the Flask class from the flask module """
from flask import Flask

""" Create an instance of the Flask class. __name__ is the name of module."""
app = Flask(__name__)

"""set strict slashes to false"""
app.url_map.strict_slashes = False


# Use the route() decorator to trigger the function that follows.
@app.route('/')
def hello():
    # This function is called when someone accesses '/' URL.
    return "Hello HBNB!"

@app.route('/hbnb')
def hello_hbnb():
    # This function is called when someone accesses '/' URL.
    return "HBNB"


# Check if not imported as a module
if __name__ == '__main__':
    # host='0.0.0.0' makes the server accessible externally.
    app.run(host='0.0.0.0', port=5000)
