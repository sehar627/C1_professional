WIDTH = 600
HEIGHT = 400

rocket = Actor("rocket_small")
rocket.scale = 0.01
rocket.pos = (300, 350)

y_velocity = -1

def draw():
    screen.fill("midnightblue")

    # Stars
    screen.draw.filled_circle((80, 60), 2, "white")
    screen.draw.filled_circle((500, 100), 2, "white")
    screen.draw.filled_circle((150, 200), 2, "white")
    screen.draw.filled_circle((450, 250), 2, "white")
    screen.draw.filled_circle((350, 80), 2, "white")

    # Rocket
    rocket.draw()

def update():
    global y_velocity

    rocket.y += y_velocity

   