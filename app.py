# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3
import secrets
import random

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS quizzes (
                        id INTEGER PRIMARY KEY,
                        token TEXT UNIQUE,
                        title TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                        id INTEGER PRIMARY KEY,
                        quiz_token TEXT,
                        question TEXT,
                        option1 TEXT,
                        option2 TEXT,
                        option3 TEXT,
                        option4 TEXT,
                        correct_option INTEGER,
                        FOREIGN KEY (quiz_token) REFERENCES quizzes (token)
                    )''')
    conn.commit()
    conn.close()

# Initialize the database when the application starts
initialize_database()

# Function to generate a 6-digit random token

quiz_token = join(random.choices('0123456789', k=6))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():


    if request.method == 'POST':
        quiz_title = request.form['quiz_title']
        question=request.form['question_text']
        option1=request.form['option1']
        option2=request.form['option2']
        option3=request.form['option3']
        option4=request.form['option4']
        correct_option=request.form['correct_option']

        return redirect(url_for('add_question', quiz_token=quiz_token))

    return render_template('create_quiz.html', form=form)

@app.route('/add_question/<quiz_token>', methods=['GET', 'POST'])
def add_question(quiz_token):


    if request.method == 'POST' 
        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO questions (quiz_token, question, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (quiz_token, form.question_text.data, form.option1.data, form.option2.data, form.option3.data, form.option4.data, int(form.correct_option.data)))
        conn.commit()
        conn.close()

        flash('Question added successfully!')
        return redirect(url_for('add_question', quiz_token=quiz_token))

    return render_template('add_question.html', form=form, quiz_token=quiz_token)

# app.py

@app.route('/view_quiz/<quiz_token>')
def view_quiz(quiz_token):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Fetch quiz details
    cursor.execute("SELECT * FROM quizzes WHERE token = ?", (quiz_token,))
    quiz = cursor.fetchone()

    if not quiz:
        flash('Quiz not found!')
        return redirect(url_for('index'))

    # Fetch questions and options for the quiz
    cursor.execute("SELECT * FROM questions WHERE quiz_token = ?", (quiz_token,))
    questions = cursor.fetchall()

    conn.close()
    
    return render_template('view_quiz.html', quiz=quiz, questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
