#!/usr/bin/python3
""" An application server """

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """ This function provide a method to close an session of
    the storage"""
    storage.close()


@app.route('/states_list')
def home():
    """ an simply routing to display a list of the state """
    return render_template(
        '7-states_list.html',
        states=storage.all('State').values())


if __name__ == '__main__':
    app.run()
