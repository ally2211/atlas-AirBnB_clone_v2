#!/usr/bin/python3
""" Import the Flask class from the flask module """
from flask import Flask

""" Create an instance of the Flask class. __name__ is the name of module."""
app = Flask(__name__)


# Use the route() decorator to trigger the function that follows.
@app.route('/', strict_slashes=False)
def hello():
    # This function is called when someone accesses '/' URL.
    return "Hello HBNB!"


# Check if not imported as a module
if __name__ == '__main__':
    # host='0.0.0.0' makes the server accessible externally.
    app.run(host='0.0.0.0', port=5000)
