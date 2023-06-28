#!/usr/bin/python3
"""flask routes"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    states = storage.all(State)
    if id:
        key = 'State.' + id
        cities = []
        if key in states:
            state = states[key]
            if storage_type == 'db':
                cities = state.cities
            else:
                cities = state.cities()
        return render_template('9-states.html', states=states, id=id, cities=cities)
    else:
        return render_template('9-states.html', states=states, id=id, cities=None)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
