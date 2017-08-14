import flask
import tqtPrivateLib
app = flask.Flask(__name__)
# it must be __name__


@app.route('/')
def hello() -> str:
    return 'Hello Python Flask - Thieu Quang Tuan'


@app.route('/search4letters')
def do_search() -> str:
    return str(tqtPrivateLib.searchLetters('life, the universe, and everything!', 'eiru'))
app.run()