from gamedata import data
from quizzgameOOP import Question
from quizz_brain import QuizzBrain

question_bank = []
for question in data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_object = Question(question_text,question_answer)
    question_bank.append(question_object)

game = QuizzBrain(question_bank)

while True:
    if game.still_has_questions():
        if game.next_question():
            continue
        else:
            break