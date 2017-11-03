import turtle
from Jump import * # Imports every function from Jump.py 
illusion = turtle.Turtle()

illusion.speed(0) # sets the speed so it can be fast, 0 is the fastest.
turtle.bgcolor('black') # sets the background color to black
illusion.color("cyan")


for times in range(200): # repeats the code certain amount of times.
    illusion.forward(400) # going toward and setting the size
    illusion.right(30)
    illusion.forward(20)
    illusion.left(60)
    illusion.forward(50)
    illusion.right(30)
    
    jump (illusion, 0, 0)
    
    illusion.right(2)
turtle.done() # adds some finishes touhes to the design
   
    
    

