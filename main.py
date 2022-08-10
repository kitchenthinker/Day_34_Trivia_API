import tkinter

from quiz_brain import QuizBrain
from ui import QuizWindow


class MainGame:

    def __init__(self):
        self.window = QuizWindow()
        self.quiz_core = None
        self.main_fun = None
        self.is_need_to_restart = False
        self.bind_buttons()
        # start the program
        self.window.frame.mainloop()

    def initialize_quiz_core(self):
        self.quiz_core = QuizBrain()
        number_questions = self.window.spinbox_value.get()
        self.quiz_core.trivia_api.set_params(number_questions)
        self.quiz_core.set_question_bank()

    def play_next_game_question(self):
        self.window.canvas.config(bg='white')
        if not self.quiz_core.is_run_out_of_questions():
            self.quiz_core.set_next_question()

            current_text = self.quiz_core.current_question.text
            current_score = self.quiz_core.score

            self.window.change_canvas_text(current_text)
            self.window.set_score_text(current_score)
        else:
            self.set_ready_for_playing_again()

    def check_user_answer(self):
        user_answer = self.quiz_core.user_answer
        self.quiz_core.set_current_user_answer(user_answer)
        result = self.quiz_core.is_the_answer_right(user_answer)
        if result:
            self.quiz_core.increase_score_value()
        self.window.give_feedback(result)
        self.quiz_core.delete_item_from_question_bank()
        self.main_fun = self.window.frame.after(1000, self.play_game)

    def play_game(self):
        self.play_next_game_question()

    def btn_right_pressed(self, event):
        if self.window.btn_true['state'] != tkinter.DISABLED:
            self.quiz_core.set_current_user_answer(True)
            self.check_user_answer()

    def btn_wrong_pressed(self, event):
        if self.window.btn_false['state'] != tkinter.DISABLED:
            self.quiz_core.set_current_user_answer(False)
            self.check_user_answer()

    def bind_buttons(self):
        self.window.btn_true.bind('<Button-1>', self.btn_right_pressed)
        self.window.btn_false.bind('<Button-1>', self.btn_wrong_pressed)
        self.window.btn_start.bind('<Button-1>', self.btn_start_game)

    def set_ready_for_playing_again(self):
        current_text = self.quiz_core.get_game_over_text()
        self.is_need_to_restart = False
        self.window.btn_start['text'] = "START GAME"
        self.window.set_button_state(_state=tkinter.DISABLED)
        self.window.change_canvas_text(current_text)

    def btn_start_game(self, event):
        if not self.is_need_to_restart:
            self.is_need_to_restart = True
            self.window.btn_start['text'] = "STOP"
            self.window.set_button_state(_state=tkinter.NORMAL)
            self.initialize_quiz_core()
            self.main_fun = self.window.frame.after(1000, self.play_game)
        else:
            self.set_ready_for_playing_again()
            # self.btn_start_game(None)


def main_function():
    quiz = MainGame()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_function()
