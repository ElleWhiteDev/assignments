from flask import Flask, render_template, request, redirect, url_for, flash, session

from surveys import surveys

app= Flask(__name__)
app.secret_key = "hibbidybibiddyboo"

satisfaction_survey = surveys["satisfaction"]

responses = "responses"


@app.route("/")
def root_page():
    """Button to redirect to survey"""

    return render_template("root_page.html", satisfaction_survey=satisfaction_survey)


@app.route("/begin-survey", methods=["POST"])
def start_session():
    """Create responses in session"""

    session["responses"] = []
    return redirect(url_for("questions_page", num=0))


@app.route("/questions/<num>", methods=["GET", "POST"])
def questions_page(num):
    """Questions and answers displayed to user"""
        
    if request.method == "POST":
        return handle_answer(num)

    num = int(num)
    current_question_num = len(session["responses"])

    if num != current_question_num or num >= len(satisfaction_survey.questions):
        flash("Invalid option. Please answer the questions in order.", "error")
        return redirect(url_for("questions_page", num=current_question_num))

    question = satisfaction_survey.questions[num]

    # if num <= len(satisfaction_survey.questions) - 1:
    return render_template("questions.html", question=question, satisfaction_survey=satisfaction_survey, num=num)
    # else:
    #     return render_template("thank_you.html")


@app.route("/answer", methods=["POST"])
def handle_answer():
    """Capture user answers and redirect to next question"""
    current_question_num = len(session["responses"])
    choice = request.form.get(str(current_question_num))

    if not choice:
        flash("Please select an answer before proceeding.", "error")
        return redirect(url_for("questions_page", num=current_question_num))

    if len(session["responses"]) == current_question_num:
        responses = session["responses"]
        responses.append(choice)
        session["responses"] = responses
        next_question_num = current_question_num + 1

        if next_question_num < len(satisfaction_survey.questions):
            return redirect(url_for("questions_page", num=next_question_num))
        else:
            return redirect(url_for("thank_you_page"))
    else:
        return redirect(url_for("questions_page", num=current_question_num))


@app.route("/thank_you", methods=["GET"])
def thank_you_page():
    """Thank you message with gif"""
    return render_template("thank_you.html", satisfaction_survey=satisfaction_survey)