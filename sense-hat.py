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

framebuffer = [b] * 64

while True:
    pressure = bin(int(sense.pressure*1000))
    pressure = pressure[2:]
    print(pressure)
    for i in range(len(pressure)+2):
        match pressure[i+2]:
            case "0":
                framebuffer[i] = n
            case "1":
                framebuffer[i] = r
            case _:
                framebuffer[i] = g
    sense.set_pixels(framebuffer)
    time.sleep(500)