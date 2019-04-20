#############################
### Chapter 5: Exercise 2 ###
#############################

# import necessary modules
import turtle

# steal draw_square function from last exercise
# edit it so it draws a square centered on the window
def draw_centered_square(t, sz):
    """Get turtle t to draw a square with sz side""" 
    t.penup()
    t.setposition(-sz/2,-sz/2)
    t.pendown()
    for i in range(4):
        t.forward(sz)
        t.left(90)

# set up the main function
def main():
    # set up turtle
    tess = turtle.Turtle()
    tess.color("hotpink")
    tess.pensize(3)

    # set up screen
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    # draw some squares
    for size in range(20, 101, 20):
        draw_centered_square(tess, size)

# call main function if __name__ == '__main__'
if __name__ == "__main__":
    main()



#############################
### Chapter 5: Exercise 5 ###
#############################

# import necessary modules
import turtle

# steal draw_poly function
def draw_poly(t, sides, side_length):
    for i in range(sides):
        t.forward(side_length)
        t.left(360/sides)

# write draw_equi_triangle(turtle, size) which calls draw_poly function
def draw_equi_triangle(t, size):
    draw_poly(t, 3, size)

# set up main function
def main():
    # set up screen
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    # set up turtle
    tess = turtle.Turtle()
    tess.color('hotpink')
    tess.pensize(3)

    # call draw_equi_triangle
    draw_equi_triangle(tess, 50)

# call main function if __name__ == '__main__'
if __name__ == "__main__":
    main()



#############################
### Chapter 5: Exercise 8 ###
#############################

import turtle

def drawFivePointStar(someturtle):
    t = someturtle
    length_of_side = 100
    number_of_sides = 5
    total_number_of_full_turns = 2
    degrees_to_turn = total_number_of_full_turns*360/number_of_sides 
    
    for i in range(number_of_sides):
        t.forward(length_of_side)
        t.right(degrees_to_turn)
        
def drawFiveFivePointStars(someturtle):
    t = someturtle
    for i in range(5):
        t.pendown()
        drawFivePointStar(t)
        t.penup()
        t.left(144)
        t.backward(350)
    
wn = turtle.Screen()
wn.setup(500,500)
alex = turtle.Turtle()
wn.bgcolor("lightblue")
alex.color("purple")
alex.speed(10)
alex.penup()
alex.forward(-175)
alex.left(90)
alex.forward(50)
alex.right(90)

drawFiveFivePointStars(alex)



##############################
### Chapter 5: Exercise 10 ###
##############################

import turtle

def drawSprite(someturtle, num_of_legs, length_of_legs):
    t = someturtle
    degrees_to_turn = 360/num_of_legs
    for i in range(num_of_legs):
        t.forward(length_of_legs)
        t.forward(-length_of_legs)
        t.right(degrees_to_turn)
        
wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("circle")
alex.color("blue")
wn.bgcolor("lightgreen")
alex.stamp()

drawSprite(alex,15,120)