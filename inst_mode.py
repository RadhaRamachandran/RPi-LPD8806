#!/usr/bin/python

from bootstrap import *
import numpy as np

inst_data = np.genfromtxt('inst_data.csv',delimiter=',', usecols = 3)

#green pulse

for i in inst_data:
    print i
    if i == 1:
        print 'I\'m an energy saver!'
        # level = 0.2
        # step = 0.1
        # dir = step
        # while level >= 0.2:
        #     led.fill(Color(0.0, 255.0, 0.0, level))
        #     led.update()
        #     if(level >= 0.8):
        #         dir = -step
        #     level += dir
    elif i == 2:
        anim = Rainbow(led)
        for i in range(60):
            anim.step()
            led.update()
    else:
        print 'else color blue'
        led.fill(Color(0.0, 0.0, 255.0, .8))

#led.all_off()