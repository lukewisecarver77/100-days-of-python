from day17_question_model import Question
from day17_data import question_data
from day17_quiz_brain import QuizBrain

question_bank = []
for pair in question_data:

    question_text = pair["text"]
    question_answer = pair["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've complete the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

