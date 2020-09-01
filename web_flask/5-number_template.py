from flask import Flask, render_template
""" An application server """

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


@app.route('/python')
@app.route('/python/<string:value>')
def python(value="is_cool"):
    """ an simply routing with the default parameters """
    return 'Python %s' % value.replace('_', ' ')


@app.route('/number/<int:value>')
def number(value):
    """ an simply routing with the default parameters """
    return '%d is a number' % value

@app.route('/number_template/<int:value>')
def number_template(value):
    """ an simply routing with the default parameters """
    return render_template('5-number.html', number=value)


if __name__ == '__main__':
    app.run()
