#!/usr/bin/python

from bootstrap import *
import numpy as np

inst_data = np.genfromtxt('inst_data.csv',delimiter=',', usecols = 3)

red = Color(255.0,0.0,0.0)
green = Color(0.0,255.0,0.0)
blue = Color(0.0,255.0,0.0)
white = Color(255.0,255.0,255.0)

for i in inst_data:

    print i

    if i == 1:
        print 'good'
        anim = Wave(led, Color(0, 0, 100), 2)
        for i in range(10):
            anim.step()
            led.update()
        led.fillOff()
    elif i == 2:
        level = 0.25
        step = 0.04
        dir = step
        while level >= 0.25:
            led.fill(Color(0.0, 255.0, 0.0, level))
            led.update()
            if(level >= 0.7):
                dir = -step
            level += dir
    elif i == 3:
        print 'bad'
        anim = ColorWipe(led, red)
        for i in range(50):
            anim.step()
            led.update()
        led.fillOff()
    else:
        print 'UGLY'
        # anim = PartyMode(led, [red,white])
        # for i in range(50):
        #     anim.step()
        #     led.update()
        # led.fillOff()

led.all_off()