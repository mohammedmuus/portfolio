from flask import Flask
app = Flask(__name__)
import http

def make_bold(function):
    def wrapper_function():
        func=f'<b>{function()}</b>'
        return func
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        func=f'<em>{function()}</em>'
        return func
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'
@app.route('/bye')
@make_bold
@make_italic
def bye():
    return "Bye"

@app.route('/<name>')
def greeting(name):
    return f'hello there {name}'
if __name__== "__main__":
    app.run(debug=True)