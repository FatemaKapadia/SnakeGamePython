from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.length = 3
        self.x = 0
        self.y = 0
        self.makeSnake()
        self.head = self.segments[0]

    def makeSnake(self):
        for i in range(self.length):
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.setpos(x=self.x, y=self.y)
            self.segments.append(t)
            t.penup()
            self.x -= 20

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.segments[0].forward(20)

    def turnUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turnDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turnLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turnRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def addSegment(self):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        prev = self.segments[-1]
        t.goto(prev.pos())
        self.segments.append(t)

    def isOverlap(self):
        for i in range(4, len(self.segments)):
            seg = self.segments[i]
            if self.head.distance(seg) < 15:
                return True

        return False
