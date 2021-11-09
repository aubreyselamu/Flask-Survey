from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question,Survey, satisfaction_survey

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY']= 'Yohanna_12'
toolbar = DebugToolbarExtension(app)

responses = []

@app.route('/')
def start_page():
    
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('base.html', title=title, instructions=instructions)
