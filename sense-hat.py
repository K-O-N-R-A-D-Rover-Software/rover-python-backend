from sense_hat import SenseHat

sense = SenseHat()

g = (0, 255, 0)
y = (255, 255, 0)
b = (0, 0, 255)
r = (255, 0, 0)
w = (255,255,255)
n = (0,0,0)
p = (255,105, 180)

sense.show_message("DOOM", text_colour=r)

framebuffer = []

while True:
    pressure = sense.pressure
    for i in range(64):
        match pressure:
            case 0:
                framebuffer[i] = "n"
            case 1:
                framebuffer[i] = "r"
            case _:
                framebuffer[i] = "n"
    sense.set_pixels(framebuffer)