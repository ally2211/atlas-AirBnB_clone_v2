#!/usr/bin/python3
""" Import the Flask module"""
from flask import Flask, render_template
from models import storage

""" Create an instance of the Flask class"""
app = Flask(__name__)


"""set strict slashes to false"""
app.url_map.strict_slashes = False


@app.route('/states/', defaults={'id': None})
@app.route('/states/<id>')
def states(id):
    """Fetches data from the storage engine
    and renders it to the template."""
    if id is None:
        # No id is provided, render template with state=None
        return render_template("9-states.html", state=None)
    else:
        # Assuming storage.all("State") returns a dictionary-like object
        state = next((state for state in storage.all("State").values() if str(state.id) == id), None)
        if state is None:
            # No state found for the given id, render template with state=None
            return render_template("9-states.html", state=None)
        else:
            # State found, render template with the found state
            return render_template("9-states.html", state=state)


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


@app.route('/hbnb_filters/')
def hbnb_filters():
    """Fetches data from the storage engine
    and renders it to the 8-cities_by_states.html template."""
    
    states = list(storage.all("State").values())
    # Sort states by name
    states.sort(key=lambda state: state.name)
  
    amenities = storage.all("Amenities").values()
    for amenity in amenities:
        amenity.sort(key=lambda amenity: amenity.name)    

    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage on app context teardown."""
    storage.close()


""" The server only starts if the script is executed directly"""
if __name__ == "__main__":
    # Run the Flask application on host '0.0.0.0' and port '5000'
    app.run(host='0.0.0.0', port=5000, debug=True)
