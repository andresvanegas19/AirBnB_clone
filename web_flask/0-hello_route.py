from flask import Flask
""" An application server """

app = Flask(__name__)

@app.route('/')
def hello():
     """ an simply routing """
     return 'Hello HBNB!'

if __name__ == '__main__':
     app.run()
