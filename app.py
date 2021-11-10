from flask import Flask, render_template, session, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY']= 'Yohanna_12'
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


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
    
    #add the reponse to the response variable
    responses.append(choice)
    

    if len(survey.questions) == len(responses):
        return render_template('thankyou.html')
    else:
        return redirect(f'/questions/{len(responses)}')

@app.route('/complete')
def complete():
    return render_template('thankyou.html')