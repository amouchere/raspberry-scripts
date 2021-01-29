#!/usr/bin/python   
from gpiozero import Button
import subprocess

## GPIO 17 et GROUND
## https://projects.raspberrypi.org/en/projects/push-button-stop-motion/6

button = Button(17)
while True:
    try:
        button.wait_for_press()

        subprocess.call("shutdown -h now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except KeyboardInterrupt:
        break
