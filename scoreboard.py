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
        self.high_score = 0

        self.score_display()

    def increment_score(self):
        self.score += 1
        self.score_display()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_display()

    # No longer needed....
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False,
    #                align=ALIGNMENT, font=FONT)

    def score_display(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", move=False,
                   align=ALIGNMENT, font=FONT)
