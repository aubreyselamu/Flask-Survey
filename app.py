from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY']= 'Yohanna_12'
toolbar = DebugToolbarExtension(app)

