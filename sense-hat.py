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

while True:
    sense.show_message("Pressure: "+str(round(sense.pressure,2))+" mB", text_colour=r, scroll_speed=0.05)