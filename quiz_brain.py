import data
import html
import random


class QuizBrain:

    def __init__(self):
        self.trivia_api = data.TriviaApi()
        self.question_number = 0
        self.score = 0
        self.question_bank: list = []
        self.current_question = None
        self.user_answer = False

    def set_question_bank(self):
        trivia = self.trivia_api.get_questions_data()
        if trivia is not None:
            self.question_bank = [Question(item) for item in trivia]
            self.question_number = len(self.question_bank)

    def is_run_out_of_questions(self):
        return self.question_bank == []

    def delete_item_from_question_bank(self):
        self.question_bank.remove(self.current_question)

    def set_next_question(self):
        self.current_question = random.choice(self.question_bank)
        self.question_number += 1

    def set_current_user_answer(self, user_answer: bool):
        self.user_answer = user_answer

    def is_the_answer_right(self, user_answer):
        return self.current_question.answer == self.user_answer

    def increase_score_value(self, step: int = 1):
        self.score += step

    def checking_answer(self):
        if self.is_the_answer_right(self.user_answer):
            self.increase_score_value()

    def get_game_over_text(self):
        current_text = f"You've run out of questions. \n" \
                       f"Your score is {self.score}"
        return current_text


class Question:

    def __init__(self, _data):
        self.text = html.unescape(_data['question'])
        self.answer = _data['correct_answer'] == 'True'
