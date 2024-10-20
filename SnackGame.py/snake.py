from turtle import Turtle
position=[(0,0),(-20,0),(-40,0)]
move_snake=20
up=90
down=270
left=180
right=0
class snake:
    def __init__(self):
        self.segment=[]
        self.creat_snake()
        self.head=self.segment[0]

    def creat_snake(self): 
        for item in position:
         self.add_segment(item)
    def add_segment(self,item):
        new_segment=Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(item)
        self.segment.append(new_segment)
    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
         new_x = self.segment[seg_num-1].xcor()
         new_y = self.segment[seg_num-1].ycor()
         self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(move_snake)
    def up(self):
        if self.head.heading()!=down:
         self.head.setheading(up)

    def down(self):
        if self.head.heading()!=up:
         self.head.setheading(down)

    def left(self):
        if self.head.heading()!=right:
         self.head.setheading(left)

    def right(self):
        if self.head.heading()!=left:
         self.head.setheading(right)




        