#!/usr/bin/python3
""" An application server """

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """ an simply routing """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
