from flask import Flask, request, render_template
import blog_entry
import database_interaction

app = Flask(__name__)

collection_id = '6366bccc925200b44bce'
database_id = '6366bcb8b6d5c310ab4a'


@app.route('/')
def home():
    """
    initialize home html template
    """
    return render_template('okok.html')


@app.route('/', methods=['GET', 'POST'])
def post_info():
    """
    fetch entry submited into form and send it to the database
    """
    if request.method == 'POST':
        files = request.form.get('filename')
        date = request.form.get('date')
        latitude = float(request.form.get('lat'))
        longitude = float(request.form.get('lng'))
        entry = request.form.get('words')

        data = blog_entry.create_blog_entry('test', 'test', entry, date, latitude, longitude, files)
        database_interaction.format_collection(database_id, collection_id)
        database_interaction.create_document(data, database_id, collection_id)

    return render_template('okok.html')


if __name__ == '__main__':
    app.run()
