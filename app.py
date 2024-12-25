from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello1')
def hello_world1():
    return 'Hello, World1!'

@app.route('/hello2')
def hello_world2():
    return 'Hello, World!2'

@app.route('/test_fun')
def test():
    a = 5+6
    return 'this is my first function in flask {}'.format(a)

@app.route('/input_url')
def request_input():
    data = request.args.get('x')
    return 'This is my input URL {}'.format(data)
# http://127.0.0.1:5000/input_url?x=zoya x => query/key

if __name__ == '__main__':
    app.run(debug=True)
