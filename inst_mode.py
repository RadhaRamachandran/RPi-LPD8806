#!/usr/bin/python

from bootstrap import *

#green pulse
r,g,b = (0.0,255.0,0.0)
step = 0.1
level = 0.1
dir = step
while level >= 0.0:
    led.fill(Color(r, g, b, level))
    led.update()
    if(level >= 0.99):
        dir = -step
    level += dir
    #sleep(0.005)

led.all_off()