from flask import Flask, render_template
from models import storage
""" An application server """

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def close():
     """ This function provide a method to close an session of
     the storage"""
     storage.close()


@app.route('/display')
def home():
    """ an simply routing to display a list of the state """
    print(storage.all('State'))
    return render_template('7-states_list.html')


if __name__ == '__main__':
    app.run()
