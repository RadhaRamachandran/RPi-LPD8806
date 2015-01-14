#!/usr/bin/python

from bootstrap import *
import numpy as np

inst_data = np.genfromtxt('inst_data.csv',delimiter=',', usecols = 3)

#green pulse
r,g,b = (0.0,255.0,0.0)
step = 0.1
level = 0.1
dir = step

for i in inst_data:
    print i
    if i == 1:
        #print i
        while level >= 0.0:
            led.fill(Color(r, g, b, level))
            led.update()
            if(level >= 0.8):
                dir = -step
            level += dir
            #sleep(0.005)
    else:
        #print i
        led.fill(Color(0.0, 0.0, 255.0, .2))

#led.all_off()