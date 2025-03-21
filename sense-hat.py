from sense_hat import SenseHat
import time

sense = SenseHat()

g = (0, 255, 0)
y = (255, 255, 0)
b = (0, 0, 255)
r = (255, 0, 0)
w = (255,255,255)
n = (0,0,0)
p = (255,105, 180)

#sense.show_message("DOOM", text_colour=r)


sense.color.gain = 16

sense.color.integration_cycles = 32


framebuffer = []

def reset():
    global framebuffer
    framebuffer = [n] * 64

reset()
mode = "color"

def up():
    mode = "color"
sense.stick.direction_up = up

def down():
    mode = "pressure"
sense.stick.direction_down = down

def left():
    mode = "pressure"
sense.stick.direction_left = left

def right():
    mode = "pressure"
sense.stick.direction_right = right

def middle():
    mode = "pressure"
sense.stick.direction_middle = middle

while True:
    match mode:
        case "color":
            framebuffer[0] = sense.colour.colour[:3] # return tuple of (r,g,b,clear)
            for i in range(3):
                framebuffer[0][i] = round(framebuffer[0][i]*255/256)
            print(sense.colour.colour[:3])
            sense.colour.integration_time
        case "pressure":
            pressure = bin(int(sense.acceleration*1000))
            data = pressure[2:]
            print(data)
            for i in range(len(data)):
                match pressure[i]:
                    case "0":
                        framebuffer[i] = n
                    case "1":
                        framebuffer[i] = r
                    case _:
                        framebuffer[i] = g
    sense.set_pixels(framebuffer)
    time.sleep(.2)