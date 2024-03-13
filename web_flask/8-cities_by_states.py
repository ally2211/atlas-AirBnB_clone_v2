#!/usr/bin/python3
""" Import the Flask module"""
from flask import Flask, render_template
from models import storage

""" Create an instance of the Flask class"""
app = Flask(__name__)


"""set strict slashes to false"""
app.url_map.strict_slashes = False


@app.route('/states_list/')
def states_list():
    """Fetches data from the storage engine
    and renders it to the 7-states_list.html template."""
    # 'State' is the model class for states
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.route('/cities_by_states/')
def cities_by_states():
    """Fetches data from the storage engine
    and renders it to the 8-cities_by_states.html template."""
    # Assuming 'State' is the model class for states
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage on app context teardown."""
    storage.close()


""" The server only starts if the script is executed directly"""
if __name__ == "__main__":
    # Run the Flask application on host '0.0.0.0' and port '5000'
    app.run(host='0.0.0.0', port=5000, debug=True)
