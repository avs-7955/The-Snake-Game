from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.score = 0

        self.score_display()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.score_display()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False,
                   align=ALIGNMENT, font=FONT)

    def score_display(self):
        self.write(f"Score:{self.score}", move=False,
                   align=ALIGNMENT, font=FONT)
