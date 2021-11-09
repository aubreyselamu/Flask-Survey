from flask import Flask, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY']= 'Yohanna_12'
toolbar = DebugToolbarExtension(app)

responses = []

@app.route('/')
def start_page():
    '''Display start page'''
    
    title = survey.title
    instructions = survey.instructions
    return render_template('start_survey.html', title=title, instructions=instructions)

@app.route('/questions/<int:qid>')
def get_questions_page(qid):
    '''Display current question'''

    question = survey.questions[qid]
    return render_template('questions.html', question=question)

    

    
    
    