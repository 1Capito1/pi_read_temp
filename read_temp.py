from time import sleep
from typing import Literal
from sense_hat import SenseHat

sense = SenseHat()

def get_temp():
    t = sense.temp
    temp = 0.0 if not isinstance(t, (int, float)) else float(t)
    text = f"{temp:.1f}"
    sense.show_message(text)
    sleep(5)

while (True):
    try:
        get_temp()
    except KeyboardInterrupt:
        print("exiting gracefully")
        sense.clear
