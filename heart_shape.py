import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(8)
pen.color("pink")

# Function to draw lines forming the heart shape
def draw_heart_line(x, y):
    pen.penup()
    pen.goto(0, 0)  # Starting point at the center
    pen.pendown()
    pen.goto(x, y)

# Draw heart with lines
for angle in range(0, 360, 5):  # Adjust the step size to control line density
    radians = math.radians(angle)
    x = 200 * math.sin(radians)**3  # X coordinate for heart shape
    y = 150 * math.cos(radians) - 50 * math.cos(2 * radians) - 20 * math.cos(3 * radians) - 10 * math.cos(4 * radians)  # Y coordinate for heart shape
    draw_heart_line(x, y)
    

pen.hideturtle()
screen.mainloop()
