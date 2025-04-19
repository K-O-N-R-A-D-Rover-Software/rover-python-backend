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
mode = "pressure"

def up():
    mode = "color"
    print("up")
sense.stick.direction_up = up

def down():
    mode = "pressure"
    print("down")
sense.stick.direction_down = down

def left():
    mode = "acceleration"
    print("left")
sense.stick.direction_left = left

def right():
    mode = "pressure"
    print("right")
sense.stick.direction_right = right

def middle():
    mode = "pressure"
    print("middle")

sense.stick.direction_middle = middle

sense.stick.direction_up = up

sense.stick.direction_down = down

sense.stick.direction_left = left

sense.stick.direction_right = right

sense.stick.direction_middle = middle

# return temperature from the humidity sensor in celsius
def getTempInCelsius():
    return sense.get_temperature()

# return temperature from the pressure sensor in celsius
def getTempFromPressureInCelsius():
    return sense.get_temperature_from_pressure()

# return humidity in percentage
def getHumidityInPercentage():
    return sense.get_humidity()

# return pressure in millibars
def getPressureInMillibars():
    return sense.get_pressure()

# return dictionary of x, y, z in unit G
def get_accelerometer():
    return sense.get_accelerometer_raw()

# return dictionary of pitch, roll, yaw
def getOrientationDict():
    return sense.get_orientation()
