import turtle
import random

# We will need the edges of our box, so we set them
width = 300
height = 400
window = turtle.Screen()
window.setup(width, height)
window.tracer(4)

color = ["blue",
        "yellow",
        "red",
        "darkgreen", 
        "cyan", 
        "violet",
        "magenta",
        "orange",
        "purple", 
        "navy", 
        "brown", 
        "maroon",
        "turquoise", 
        "lightgreen", 
        "green", 
        "skyblue", 
        "black", 
        "gold",
        "gray"]

shapes = ["arrow",
        "turtle",
        "circle",
        "square", 
        "triangle", 
        "classic"]

N = 6 # Number of balls
balls = [] # A list to hold the balls

# Set up N balls and start them in random positions
for i in range(N):
    balls.append(turtle.Turtle())
    balls[i].penup()
    balls[i].shape(shapes[i%len(shapes)])
    balls[i].color(color[i%len(color)])

    # Set random starting position
    balls[i].setx(random.randint(0,height / 4))
    balls[i].sety(random.randint(0,height / 4))

# Free fall acceleration
g = -9.81

# Timestep size
t = 0.005

# Starting velocity is now also a list, we need one velocity per ball
ux = []
uy = []
#starting mass
mass = []
#rotation
rotation = []
for i in range(N):
    ux.append(random.randint(-width/10,width/10))
    uy.append(0)
    mass.append(random.randint(1,10))
    rotation.append(random.randint(-2,2))
    #balls[i].shapesize(mass[i]**0.5)


while True:
    for i in range(N):
        g = -9.81 * mass[i]
        balls[i].right((rotation[i]))
        uy[i] += g*t
        balls[i].setx(ux[i]*t + balls[i].xcor())
        balls[i].sety(uy[i]*t + balls[i].ycor())

        if balls[i].ycor() < -height / 2 or balls[i].ycor() > height / 2:
            uy[i] = -uy[i]
            balls[i].sety(balls[i].ycor() - t*t*g)
        if balls[i].xcor() < -width / 2 or balls[i].xcor() > width / 2:
            ux[i] = -ux[i]

        # Check for collisions
        for j in range(N):
            if i != j and \
            abs(balls[i].xcor() - balls[j].xcor()) < 10 and \
            abs(balls[i].ycor() - balls[j].ycor()) < 10:
                        uxh = ux[i]
                        uyh = uy[i]
                        ux[i] = ux[j]
                        uy[i] = uy[j]
                        ux[j] = uxh
                        uy[j] = uyh

    window.update()


