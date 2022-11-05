from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/login', methods=['POST', 'GET'])
def entry():
    error = None
    if request.method == 'POST':
        journ_entry = request.form.get("entry")
        return journ_entry
    return render_template('map.html')
