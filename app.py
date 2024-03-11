from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/')
def get_data():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
