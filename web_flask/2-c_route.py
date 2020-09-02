#!/usr/bin/python3
""" An application server """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """ an simply routing """
    return 'Hello HBNB!'


@app.route('/hbnb')
def other_home():
    """ an simply routing """
    return 'HBNB'


@app.route('/c/<string:value>')
def c(value):
    """ an simply routing """
    return 'C %s' % value.replace('_', ' ')


if __name__ == '__main__':
    app.run()
