from time import sleep
from typing import Literal
from sense_hat import SenseHat

sense = SenseHat()

while (True):
    t = sense.temp
    temp = 0.0 if not isinstance(t, (int, float)) else float(t)
    text = str(temp)
    sense.show_message(text)
    sleep(5)

