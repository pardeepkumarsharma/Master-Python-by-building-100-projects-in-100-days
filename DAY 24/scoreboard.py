from turtle import Turtle
ALIGNMENT="center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.read_file()
        self.update_scoreboard()
        self.hideturtle()

    def read_file(self):
        with open("my_file.txt", "r") as file:
            self.highscore = int(file.read())

    def write_file(self):
        with open("my_file.txt", "w") as file:
            file.write(str(self.highscore))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        self.write_file()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

