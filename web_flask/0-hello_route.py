#!/usr/bin/python3
# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class. __name__ is just the name of the module.
app = Flask(__name__)

# Use the route() decorator to trigger the function that follows.
@app.route('/', strict_slashes=False)
def hello():
    # This function is called when someone accesses '/' URL.
    return printf("Hello HBNB!")


# Check if the executed script is the main program and not imported as a module 
if __name__ == '__main__':
    # Run the Flask application  host='0.0.0.0' makes the server accessible externally.
    app.run(host='127.0.0.1', port=5000)