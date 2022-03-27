from flask import Flask, request, render_template, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = os.path.dirname(os.path.realpath(__file__)) + "\\static\\uploads"


# app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG"]


@app.route('/')
@app.route('/index')
def upload_image():
    if request.method == "POST":
        image = request.files['file']

        if image.filename == '':
            print("Image must have a file name")
            return redirect(request.url)

        filename = secure_filename(image.filename)

        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"], filename))

        return render_template("index.html", filename=filename)

    return render_template('index.html', title='Parking Alerts')


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename="/uploads" + filename), code=301)


app.run(port=8044)
