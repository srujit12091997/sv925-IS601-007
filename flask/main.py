import os

from flask import Flask, request

app = Flask(_name_)


@app.route('/')
def hello_world():
    name = request.args.get('name', 'World')
    return f'Hello {name}!'


if _name_ == "_main_":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))