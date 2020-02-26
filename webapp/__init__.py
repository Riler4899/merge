from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b8ead5f7135721d7ce35cc253caa228'

CORS(app)

from webapp import routes