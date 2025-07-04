import turtle

window=turtle.Screen()
window.title("Turtle Graphics Example")
window.bgcolor("black")


#creating turtle
t = turtle.Turtle()
t.color("white")
t.pensize(2)
t.speed(3)
t.hideturtle()
# Drawing a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Hide the turtle and finish
t.hideturtle()
window.mainloop()
