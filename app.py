from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods = ['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = f'The sum of  {num1} and {num2} is {r}'
        elif(ops == 'subtract'):
            r = num1 - num2
            result = f'The subtraction of  {num1} and {num2} is {r}'
        elif(ops == 'multiply'):
            r = num1 * num2
            result = f'The multiplication of  {num1} and {num2} is {r}'
        elif(ops == 'divide'):
            if(num2 == 0):
                result = 'Can\'t divide by 0'
            else:
                r = num1 / num2
                result = f'The division of  {num1} and {num2} is {r}'
        return render_template('results.html', result = result)

@app.route('/postman_action', methods = ['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = f'The sum of  {num1} and {num2} is {r}'
        elif(ops == 'subtract'):
            r = num1 - num2
            result = f'The subtraction of  {num1} and {num2} is {r}'
        elif(ops == 'multiply'):
            r = num1 * num2
            result = f'The multiplication of  {num1} and {num2} is {r}'
        elif(ops == 'divide'):
            if(num2 == 0):
                result = 'Can\'t divide by 0'
            else:
                r = num1 / num2
                result = f'The division of  {num1} and {num2} is {r}'
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/hello1')
# def hello_world1():
#     return 'Hello, World1!'

# @app.route('/hello2')
# def hello_world2():
#     return 'Hello, World!2'

# @app.route('/test_fun')
# def test():
#     a = 5+6
#     return 'this is my first function in flask {}'.format(a)

# @app.route('/input_url')
# def request_input():
#     data = request.args.get('x')
#     return 'This is my input URL {}'.format(data)
# # http://127.0.0.1:5000/input_url?x=zoya x => query/key