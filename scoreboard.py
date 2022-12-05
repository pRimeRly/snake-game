from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        if os.stat("data.txt").st_size == 0:
            self.high_score = 0
        else:
            with open("data.txt", mode="r") as self.data:
                self.high_score = int(self.data.read())
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=265)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as self.data:
                self.data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
