import sqlite3

def take_quiz(quiz_token):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quizzes WHERE token = ?", (quiz_token,))
    quiz = cursor.fetchone()

    if not quiz:
        print('Quiz not found!')
        return

    cursor.execute(f"SELECT * FROM quiz_{quiz_token}")
    questions = cursor.fetchall()
    conn.close()

    print(f"Welcome to the quiz: {quiz['title']}\n")

    score = 0
    total_questions = len(questions)
    correct_answers = {}

    for question in questions:
        print(f"{question['id']}. {question['question']}")
        print(f"   1. {question['option1']}")
        print(f"   2. {question['option2']}")
        print(f"   3. {question['option3']}")
        print(f"   4. {question['option4']}")

        user_answer = int(input("Your choice (1-4): "))
        correct_answers[question['id']] = question['correct_option']

        if user_answer == question['correct_option']:
            score += 1

        print()

    print(f"Quiz submitted! Your score: {score}/{total_questions}")

    conn.close()

if __name__ == '__main__':
    quiz_token = input("Enter the quiz token: ")
    take_quiz(quiz_token)
