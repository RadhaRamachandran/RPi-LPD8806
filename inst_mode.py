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
        level = 0.2
        step = 0.1
        dir = step
        while level >= 0.2:
            led.fill(Color(0,255,0), level)
            led.update()
            if(level >= 0.8):
                dir = -step
            level += dir
        led.fillOff()
    elif i == 2:
        print 'okay'
        anim = Rainbow(led)
        for i in range(50):
            print 'rainbow'
            anim.step()
            led.update()
        led.fillOff()
    elif i == 3:
        print 'bad'
        anim = ColorWipe(led, red)
        for i in range(num):
            print 'colorwipe'
            anim.step()
            led.update()
        led.fillOff()
    else:
        print 'UGLY'
        anim = PartyMode(led, [red,white])
        for i in range(50):
            print 'partymode'
            anim.step()
            led.update()
        led.fillOff()

led.all_off()