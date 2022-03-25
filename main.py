from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='PArking Alerts')


app.run(host='0.0.0.0', port=8040)
