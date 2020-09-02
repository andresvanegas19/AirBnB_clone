from flask import Flask, render_template
from models import storage
from models import *
""" An application server """

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """ This function provide a method to close an session of
    the storage"""
    storage.close()


@app.route('/states')
def local():
    """ an simply routing to display a list of the state """
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.route('/states/<string:value>')
def local_with_state(value):
    """ an simply routing to display a list of the state """
    clases = storage.all().values()
    result = []
    name = None
    for clase in clases:
        if value == clase.id:
            name= clase.name
        if clase.__class__.__name__ == 'City':
            if value == clase.state_id:
                result.append(clase)

    return render_template('9-states.html',cities=result, name_state=name)



if __name__ == '__main__':
    app.run()
