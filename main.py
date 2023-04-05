
import turtle,time
from random import randint as r



'''
FUNCTIONS AND CLASS DEFINITIONS 
'''
def border():
	p = turtle.Turtle()
	p.speed(0)
	p.ht()
	p.pu()
	p.width(10)
	p.color("white")
	p.goto(-110,200)
	p.pendown()
	p.begin_fill()
	for i in range(2):
		p.forward(220)
		p.right(90)
		p.forward(400)
		p.right(90)
	p.end_fill()




####### PROGRAM #############
# Creates screen object







"""
PROGRAM
"""

############ SCREEN ############
screen = turtle.Screen()
screen.bgcolor("black")
# the listen function notifies the program that it will need to be paying attention to inputs(key presses) from the user.
screen.listen()

############ BORDER ##########
border()




########## GAME LOOP #########