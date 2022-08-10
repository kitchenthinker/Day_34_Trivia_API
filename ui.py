from tkinter import *
THEME_COLOR = "#725362"
DEFAULT_CANVAS_COLOUR = 'white'


def canvas_create_text(_canvas, _x, _y, _width, _font=("Arial", 20, "italic")):
    return _canvas.create_text(_x, _y, width=_width, font=_font)


def canvas_create_button(btn_image=None, _text="", _bg=THEME_COLOR, _state=DISABLED):
    return Button(image=btn_image, state=_state, highlightthickness=0, text=_text, bg=_bg)


def canvas_create_spinbox(_from=0, _to=100):
    default_value = StringVar(value=str(10))
    return Spinbox(from_=_from, to=_to, textvariable=default_value)


class QuizWindow:

    def __init__(self):
        # self.quiz_game = quiz_game
        self.score = None
        self.frame = Tk()
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.images_items = {
            "btn_true": PhotoImage(file="./images/true.png"),
            "btn_false": PhotoImage(file="./images/false.png"),
        }
        self.score = Label(bg=THEME_COLOR, highlightthickness=0)
        self.canvas_text = canvas_create_text(self.canvas, 150, 125, 250)
        self.btn_true = canvas_create_button(self.images_items['btn_true'])
        self.btn_false = canvas_create_button(self.images_items['btn_false'])
        self.btn_start = canvas_create_button(_text="START GAME", _bg='white', _state=NORMAL)
        self.spinbox_value = canvas_create_spinbox()
        self.spinbox_label = Label(bg=THEME_COLOR, highlightthickness=0, text="Choose a number of questions: ")
        self.default_setting()
        self.set_score_text()
        self.set_grid_default()

    def default_setting(self):
        self.setup_window_default()

    def set_button_state(self, _state=DISABLED):
        self.btn_false['state'] = _state
        self.btn_true['state'] = _state

    def give_feedback(self, is_true: bool):
        feedback_colour = 'green' if is_true else 'red'
        self.canvas.config(bg=feedback_colour)

    def set_grid_default(self):
        self.spinbox_label.grid(row=0, column=0, sticky="EW")
        self.spinbox_value.grid(row=0, column=1, sticky="EW")
        self.btn_start.grid(row=0, column=2, sticky="EW")
        self.canvas.grid(row=1, column=0, columnspan=3, sticky="EW")
        self.btn_true.grid(row=2, column=0, sticky="W")
        self.score.grid(row=2, column=1, sticky="")
        self.btn_false.grid(row=2, column=2, sticky="E")

    def set_score_text(self, value: int = 0):
        self.score.config(text=f"Score: {value}", bg="white")

    def setup_window_default(self):
        self.frame.title("QUIZZLER")
        self.frame.config(pady=20, padx=20, background=THEME_COLOR, highlightthickness=0)

    def change_canvas_text(self, value):
        self.canvas.itemconfig(self.canvas_text, text=value)
