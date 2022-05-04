#main.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from host'

if __name__ == '__main__':
    app.run(debug=True,host='20.216.26.23',port=8000)