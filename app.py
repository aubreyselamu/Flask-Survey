from flask import Flask, render_template, session, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.wrappers import response
from surveys import satisfaction_survey as survey

RESPONSE_KEY = "responses"

app = Flask(__name__)
app.config['SECRET_KEY']= 'Yohanna_12'
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def start_page():
    '''Display start page'''

    title = survey.title
    instructions = survey.instructions
    return render_template('start_survey.html', title=title, instructions=instructions)

@app.route('/begin', methods=["POST"])
def begin():
    '''Clear the session of responses'''

    session[RESPONSE_KEY] = []

    return redirect('/questions/0')

@app.route('/questions/<int:qid>')
def get_questions_page(qid):
    '''Display current question'''
    
    responses = session.get(RESPONSE_KEY)
    
    if(responses is None):
        return redirect('/')
    
    if (len(survey.questions) == len(responses)):
        return redirect('/complete')
    
    
    if(len(responses) != qid):
        flash(f"Invalid Question id: {qid}!")
        return redirect(f'/questions/{len(responses)}')

    question = survey.questions[qid]
    return render_template('questions.html', question=question)



@app.route('/answer', methods=["POST"])
def get_choice():
    '''Save response and moving on to next question'''

    #get the response choice
    choice = request.form['answer']
    
    #add the reponse to the session
    responses = session[RESPONSE_KEY]
    responses.append(choice)
    session[RESPONSE_KEY] = responses

    if len(survey.questions) == len(responses):
        return redirect('/complete')
    else:
        return redirect(f'/questions/{len(responses)}')

@app.route('/complete')
def complete():
    '''Survey complete. Completion page shown'''
    return render_template('thankyou.html')