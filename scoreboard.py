from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()
        self.highscore=0
        self.readHighScore()
        self.update()

    def readHighScore(self):
        file = open("high_score.txt")
        self.highscore = int(file.read())
        file.close()

    def increaseScore(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.highscore}", move=False, align=ALIGN, font=FONT)

    def endGame(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write(arg=f"  Game Over!\nYour score is {self.score}", move=False, align=ALIGN, font=FONT)
        if self.score > self.highscore:
            print("iam writing in file")
            file = open("high_score.txt", mode="w")
            file.write(f"{self.score}")
            file.close()
