from flask import Flask, jsonify, render_template, send_file


app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/sample.dot')
def get_data():
    file_path = 'sample.dot'
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)
