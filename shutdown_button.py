#!/usr/bin/python   
import lcddriver
from gpiozero import Button
import subprocess

## GPIO 17 et GROUND
## https://projects.raspberrypi.org/en/projects/push-button-stop-motion/6
## Run at Start up : In /etc/rc.local   =>   python /home/pi/scripts/shutdown_button.py &

button = Button(17)
while True:
    try:
        button.wait_for_press()
        
        lcd = lcddriver.lcd()
        lcd.lcd_clear()

        lcd.lcd_display_string("Shutting down ...", 1)

        subprocess.call("shutdown -h now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except KeyboardInterrupt:
        break
