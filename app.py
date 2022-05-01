from distutils.log import debug
from flask import Flask

app=Flask(__name__)

@app.route('/')
def greet():
    return 'hello world'


if __name__=='main':
    app.run(debug-True,host="0.0.0.0")