import random
import json

import tkinter as tk

import code


class JeopardyCodeGame(object):
    FILENAMES = ["questions_0.json", "questions_1.json"]

    def __init__(self):
        self.master = tk.Tk()
        self.questions = []
        for filename in self.FILENAMES:
            with open(filename) as f:
                questions = json.loads(f.read())
                self.questions.extend(questions)
        self.num_players = 8
        self.scores = [0 for _ in range(self.num_players)]
        self.current_answer_text = None

        self.master.title("Jeopardy Code Game")
        self.master.geometry(
            "{0}x{1}+0+0".format(
                self.master.winfo_screenwidth(), self.master.winfo_screenheight(),
            )
        )

        self.window = tk.Frame(self.master)
        self.window.pack(fill=tk.BOTH, expand=1, padx=40, pady=40)

        ## Question and Answer Display

        self.question_display = tk.Label(
            self.window, text="Get Ready...", font=("Courier", 20), wraplength=1000,
        )
        self.question_display.pack(pady=(15, 0))
        self.answer_display = tk.Label(
            self.window,
            text="For Jeopardy Code Gaaame!",
            font=("Courier", 20),
            wraplength=1000,
        )
        self.answer_display.pack(pady=(40, 0))

        ## Question and Answer Buttons

        self.question_button = tk.Button(
            self.window,
            text="Next Question",
            font=("Courier", 20),
            command=self.show_next_question,
        )
        self.question_button.pack(pady=(80, 0))

        self.answer_button = tk.Button(
            self.window,
            text="Show Answer",
            font=("Courier", 20),
            command=self.show_answer,
            state=tk.DISABLED,
        )
        self.answer_button.pack(pady=(15, 0))

        ## Score Area

        self.score_area = tk.Frame(self.master)
        self.score_area.pack(pady=(0, 200))

        self.score_labels = [
            tk.Label(self.score_area, text="0", font=("Courier", 20))
            for _ in range(self.num_players)
        ]
        self.score_pluses = [
            tk.Button(
                self.score_area,
                text="+",
                command=self.add_to_score_func(player_idx=player_idx, delta=1),
            )
            for player_idx in range(self.num_players)
        ]
        self.score_minuses = [
            tk.Button(
                self.score_area,
                text="-",
                command=self.add_to_score_func(player_idx=player_idx, delta=-1),
            )
            for player_idx in range(self.num_players)
        ]
        for player_idx in range(self.num_players):
            self.score_minuses[player_idx].pack(side=tk.LEFT, padx=(25, 0))
            self.score_labels[player_idx].pack(side=tk.LEFT, padx=10)
            self.score_pluses[player_idx].pack(side=tk.LEFT, padx=(0, 25))

    ###############
    ### HELPERS ###
    ###############

    def show_next_question(self):
        question_obj = random.choice(self.questions)
        category = question_obj["category"]
        value = question_obj["value"]
        question_text = question_obj["question"]
        answer_text = question_obj["answer"]
        air_date = question_obj["air_date"]
        year = air_date[:4]
        self.question_display.config(
            text=f"(aired {year})\n\n{category}\n\n{value}\n\n{question_text}"
        )
        self.question_button.config(state=tk.DISABLED)
        self.answer_display.config(text="???")
        self.answer_button.config(state=tk.NORMAL)
        self.current_answer_text = answer_text

    def show_answer(self):
        self.question_button.config(state=tk.NORMAL)
        self.answer_display.config(text=self.current_answer_text)
        self.answer_button.config(state=tk.DISABLED)

    def add_to_score_func(self, player_idx, delta):
        def command():
            self.scores[player_idx] += delta
            self.score_labels[player_idx].config(text=self.scores[player_idx])

        return command

    def play(self):
        self.master.mainloop()


def main():
    JeopardyCodeGame().play()


if __name__ == "__main__":
    main()
