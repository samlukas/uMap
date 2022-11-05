from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('okok.html')


@app.route('/entry', methods=['POST', 'GET'])
def entry():
    if request.method == 'POST':
        journ_entry = request.form.get('entry')
        return journ_entry
    return render_template('map.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')


if __name__ == '__main__':
    app.run()
