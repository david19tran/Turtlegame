#authors: 'David Tran' and 'Andy He'
#date: November 24, 2016

import turtle
import math
import random

lose=False
score=0
#set up screen
window=turtle.Screen()
window.bgcolor("white")

#draw game border
pen=turtle.Turtle()
pen.penup()
pen.setpos(-300,-300)
pen.pendown()
pen.pensize(3)
pen.speed(100)
for side in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()

#Generate and write equation at top of screen
num1=random.randint(1,10)
num2=random.randint(1,10)
equation=turtle.Turtle()
equation.penup()
equation.setpos(-290,310)
equation.hideturtle()
eqnstring=("{}+{}=".format(num1,num2))
answer=num1+num2
equation.write(eqnstring,False,align="left",font=("Arial",15,"normal"))

#print score at top of screen
scorepen=turtle.Turtle()
scorepen.penup()
scorepen.setposition(0,310)
scorepen.hideturtle()
scorestring = "Score %s" %score
scorepen.write(scorestring, False, align="center", font=("Arial",14,"normal"))

#Generate correct number for equation on map
correctNum=turtle.Turtle()
correctNum.color("blue")
correctNum.shape("circle")
correctNum.penup()
correctNum.speed(0)
correctNum.setpos(random.randint(-285,285), random.randint(-285,285))
correctNum.hideturtle()
correctNum.write(answer,False,align="center",font=("Arial",15,"normal"))

#create multiple incorrect numbers on screen
maxNum=9
nums=[]

for count in range(maxNum):
    nums.append(turtle.Turtle())
    nums[count].color("blue")
    nums[count].shape("circle")
    nums[count].penup()
    nums[count].speed(0)
    nums[count].setpos(random.randint(-285,285), random.randint(-285,285))
    goalnum=random.randint(2,20)
    #prevents number from being the same as the answer
    if goalnum==answer:
        goalnum=answer-1
    nums[count].hideturtle()
    nums[count].write(goalnum,False,align="center",font=("Arial",15,"normal"))

#create player turtle
player=turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
speed=0

#Draw start screen
start=turtle.Turtle()
start.penup()
start.hideturtle()
start.setpos(0,0)
startstring='''   Press 'Enter' to Start
Use arrow keys to move'''
start.write(startstring,False,align="center",font=("Arial",30,"bold"))

#define functions
def startgame():
    global speed
    speed=1
    start.undo()
    play=True
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
#collision detector between objects and the player
def isCollision(t1,t2):
    #Uses pythagorean theorem to calculate distance between two turtles
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
#collision detector for objects
def numCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<40:
        return True
    else:
        return False

'''Restarts game for the user, resets score
and board, respawns numbers and generates new equation for
the player'''
def gameRestart():
    global speed
    speed=1
    global score
    score=0
    player.setpos(0,0)

    #refreshes and restarts score at 0
    for i in range(2):
        scorepen.clear()
    scorepen.setposition(0,310)
    scorepen.hideturtle()
    scorestring = "Score %s" %score
    scorepen.write(scorestring, False, align="center", font=("Arial",14,"normal"))

    #generates new equation
    equation.undo()
    equation.hideturtle()
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    eqnstring=("{}+{}=".format(num1,num2))
    answer=num1+num2
    equation.write(eqnstring,False,align="left",font=("Arial",15,"normal"))

    #respawns correct number
    correctNum.undo()
    correctNum.setpos(random.randint(-285,285), random.randint(-285,285))
    correctNum.hideturtle()
    correctNum.write(answer,False,align="center",font=("Arial",15,"normal"))

    #respawns incorrect numbers around the map
    for count in range(maxNum):
        goalnum=random.randint(0,15)
        if goalnum==answer:
            goalnum=answer-1
        nums[count].undo()
        nums[count].setposition(random.randint(-300,300),random.randint(-285,285))
        nums[count].hideturtle()
        nums[count].write(goalnum,False,align="center",font=("Arial",15,"normal"))

        #spreads out correctnum and incorrectnum so they don't collide
        if numCollision(correctNum,nums[count]):
            correctNum.undo()
            correctNum.hideturtle()
            correctNum.setpos(random.randint(-285,285), random.randint(-285,285))
            correctNum.write(answer,False,align="center",font=("Arial",15,"normal"))
    
#set key bindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(startgame,"Return")
turtle.onkey(gameRestart,"r")

#main program
while True:
        player.forward(speed)

        #Lose statements
        for count in range(maxNum):
            if isCollision(player,nums[count]):
                lose=True
        if player.xcor()>300 or player.xcor()<-300:
            lose=True
        if player.ycor()>300 or player.ycor()<-300:
            lose=True

        #collision checking with correct number
        if isCollision(player,correctNum):
            score+=1
            #draw score on the screen and respawn numbers and generate new equation
            scorepen.undo()
            scorepen.penup()
            scorepen.hideturtle()
            scorestring = "Score %s" %score
            scorepen.write(scorestring, False, align="center", font=("Arial",14,"normal"))

            #Generating new equation after question is answered
            equation.undo()
            equation.hideturtle()
            num1=random.randint(1,10)
            num2=random.randint(1,10)
            eqnstring=("{}+{}=".format(num1,num2))
            answer=num1+num2
            equation.write(eqnstring,False,align="left",font=("Arial",15,"normal"))

            #Prints new correct number randomly on the map
            correctNum.undo()
            correctNum.setpos(random.randint(-285,285), random.randint(-285,285))
            correctNum.hideturtle()
            correctNum.write(answer,False,align="center",font=("Arial",15,"normal"))

            #Respawns and generates new incorrect numbers
            for count in range(maxNum):
                goalnum=random.randint(0,15)
                if goalnum==answer:
                    goalnum=answer-1
                nums[count].undo()
                nums[count].setposition(random.randint(-300,300),random.randint(-285,285))
                nums[count].hideturtle()
                nums[count].write(goalnum,False,align="center",font=("Arial",15,"normal"))

                #spreads out correct number and incorrect numbers so they don't collide
                if numCollision(correctNum,nums[count]):
                    correctNum.undo()
                    correctNum.hideturtle()
                    correctNum.setpos(random.randint(-285,285), random.randint(-285,285))
                    correctNum.write(answer,False,align="center",font=("Arial",15,"normal"))

        #Lose screen, tells user their final score and that they have lost
        if lose==True:
            player.setpos(0,0)
            speed=0
            scorepen.hideturtle()
            scorepen.setpos(0,20)
            lostscreenstring='''      You Lose
Your Score was %s
Press 'r' to restart''' %score
            scorepen.write(lostscreenstring,False,align="center",font=("Arial",15,"normal"))
            lose=False
            
