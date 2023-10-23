#!/usr/bin/env python3

from flask import Flask, make_response

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def root():
    return make_response('<h1>Python Operations with Flask Routing and Views</h1>',200)

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return make_response(f'{parameter}',200)

@app.route('/count/<int:parameter>')
def count(parameter):
    body = ''
    for num in range(parameter):
        body += f'{num}\n'
    return body,200

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        body= (num1 + num2)
    elif operation == "-":
        body= (num1 - num2)
    elif operation == "*":
        body= (num1 * num2)
    elif operation == "div":
        body= (num1/num2)
    elif operation == "%":
        body=(num1%num2)
    
    return f"{body}",200