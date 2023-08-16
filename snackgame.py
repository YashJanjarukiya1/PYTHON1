#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yashp
#
# Created:     02-12-2022
# Copyright:   (c) yashp 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
import random
import time

delay=0.1
score=0
heighestscore=0

#snakebodies
bodies=[]

#getting a screen
s=turtle.screen()
s.title("snake game")
s.bgcolor("gray")
s.setup(width=600,height=600)

#create snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)

#score board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("score:0  | heighest score:0")

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        y=head.ycor()
        head.sety(x-20)
    if head.direction=="right":
        y=head.ycor()
        head.sety(x+20)

#event handling
s.listen()
s.onkey(moveup,"up")
s.onkey(movedown,"down")
s.onkey(moveleft,"left")
s.onkey(moveright,"right")
s.onkey(movestop,"space")

#main loop
while True:
    s.update()

    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)

        score+=10

        delay-=0.001

        if score>heighestscore:
            heighestscore=score
        sb.clear()
        sb.write("Score:{} Highest Score:{}".format(score,highestscore))

        for index in range(len(bodies)-1,0,-1):
            x=bodies[index-1].xcor()
            x=bodies[index-1].ycor()
            bodies[index].goto(x,y)

        if len(bodies)>0:
            x=head.xcor()
            y=head.ycor()
            bodies[0].goto(x,y)
        move()

        for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction="stop"

                for body in bodies:
                    body.ht()
                bodies.clear()

                score=0
                delay=0.1

                sb.clear()
                sb.write("score:{}Highest Score:{}".format(score,highestscore))
            time.sleep(delay)

s.mainloop()






