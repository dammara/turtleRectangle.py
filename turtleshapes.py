import turtle, time


def wait():
    time.sleep(1)


def create_axis():          # creates the x/y axis
    turtle.speed(10)        # adjusts turtle speed to max
    turtle.forward(200)     # move x pixels forward
    turtle.backward(400)
    turtle.forward(200)    # goes backwards
    turtle.left(90)        # rotates the turtle x degrees
    turtle.forward(200)
    turtle.backward(400)
    turtle.forward(200)


turtle.shape('turtle')  # gives the arrow the shape of a turtle
create_axis()
wait()

# rectangle
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.mainloop()


