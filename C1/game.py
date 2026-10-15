
WIDTH = 600
HEIGHT = 400

planet = Actor("planet")
planet.scale = 0.05
planet.pos = (300, 200)

x_velocity = 0.5
y_velocity = -0.3


def draw():
    screen.fill("midnightblue")

    screen.draw.filled_circle((80, 60), 2, "white")
    screen.draw.filled_circle((500, 100), 2, "white")
    screen.draw.filled_circle((150, 300), 2, "white")
    screen.draw.filled_circle((450, 330), 2, "white")

    planet.draw()


def update():
    global x_velocity, y_velocity

    planet.x += x_velocity
    planet.y += y_velocity

   