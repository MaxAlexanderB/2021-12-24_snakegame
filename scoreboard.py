from turtle import Turtle


class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.refresh()


    def refresh(self):
        self.clear()
        self.goto(0, 250)
        your_score = (f"Your score is {self.score} and highscore is {self.high_score}")
        self.write(your_score, move=False, align="center", font=("Arial",8,"normal"))


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        your_score = (f"GAME OVER\nYour score is {self.score} and highscore is {self.high_score}")
        self.write(your_score, move=False, align="center", font=("Arial",8,"normal"))
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.refresh()
