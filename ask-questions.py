import random
import json

import tkinter as tk

import code


class JeopardyCodeGame(object):
    FILENAMES = ['questions_0.json', 'questions_1.json']

    def __init__(self):
        self.master = tk.Tk()
        self.questions = []
        for filename in self.FILENAMES:
            with open(filename) as f:
                questions = json.loads(f.read())
                self.questions.extend(questions)
        self.current_answer = None
        self.scores = [0, 0]

        self.master.title('Jeopardy Code Game')
        self.master.geometry(
            "{0}x{1}+0+0".format(
                self.master.winfo_screenwidth(),
                self.master.winfo_screenheight(),
            )
        )

        self.window = tk.Frame(self.master)
        self.window.pack(fill=tk.BOTH, expand=1, padx=40, pady=40)

        self.question = tk.Label(
            self.window,
            text='Get Ready...',
            font=('Courier', 20),
            wraplength=1000,
        )
        self.question.pack(pady=(40, 0))
        self.answer = tk.Label(
            self.window,
            text='For Jeopardy Code Gaaame!',
            font=('Courier', 20),
            wraplength=1000,
        )
        self.answer.pack(pady=(40, 0))

        self.question_button = tk.Button(
            self.window,
            text='Next Question',
            font=('Courier', 20),
            command=self.show_next_question,
        )
        self.question_button.pack(pady=(80, 0))

        self.answer_button = tk.Button(
            self.window,
            text='Show Answer',
            font=('Courier', 20),
            command=self.show_answer,
            state=tk.DISABLED,
        )
        self.answer_button.pack(pady=(15, 0))

        self.score_area = tk.Frame(self.master)
        self.score_area.pack(pady=(0, 200))

        self.score_labels = [
            tk.Label(self.score_area, text='0', font=('Courier', 20)),
            tk.Label(self.score_area, text='0', font=('Courier', 20)),
        ]
        self.score_pluses = [
            tk.Button(
                self.score_area,
                text='+',
                command=self.add_to_score(0, 1),
            ),
            tk.Button(
                self.score_area,
                text='+',
                command=self.add_to_score(1, 1),
            ),
        ]
        self.score_minuses = [
            tk.Button(
                self.score_area,
                text='-',
                command=self.add_to_score(0, -1),
            ),
            tk.Button(
                self.score_area,
                text='-',
                command=self.add_to_score(1, -1),
            ),
        ]
        self.score_minuses[0].pack(side=tk.LEFT)
        self.score_labels[0].pack(side=tk.LEFT, padx=20)
        self.score_pluses[0].pack(side=tk.LEFT)
        self.score_minuses[1].pack(side=tk.LEFT, padx=(50, 0))
        self.score_labels[1].pack(side=tk.LEFT, padx=20)
        self.score_pluses[1].pack(side=tk.LEFT)

    def show_next_question(self):
        question_obj = random.choice(self.questions)
        category = question_obj['category']
        question = question_obj['question']
        answer = question_obj['answer']
        self.question.config(text=category + '\n\n' + question)
        self.question_button.config(state=tk.DISABLED)
        self.answer.config(text='???')
        self.answer_button.config(state=tk.NORMAL)
        self.current_answer = answer

    def show_answer(self):
        self.question_button.config(state=tk.NORMAL)
        self.answer.config(text=self.current_answer)
        self.answer_button.config(state=tk.DISABLED)

    def add_to_score(self, player_idx, delta):
        def command():
            self.scores[player_idx] += delta
            self.score_labels[player_idx].config(text=self.scores[player_idx])
        return command

    def play(self):
        self.master.mainloop()


def main():
    JeopardyCodeGame().play()


if __name__ == '__main__':
    main()
