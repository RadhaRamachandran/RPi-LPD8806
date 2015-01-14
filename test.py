#!/usr/bin/python

from bootstrap import *

#animations - each animation method moves the animation forward one step on each call
#after each step, call update() to push it to the LED strip
#sin wave animations
anim = Wave(led, Color(255, 0, 0), 4)
for i in range(10):
	anim.step()
	led.update()

led.fillOff()
sleep(5)

anim = Wave(led, Color(0, 0, 100), 4)
for i in range(50):
	anim.step()
	led.update()

led.fillOff()

# #rolling rainbow
# anim = Rainbow(led)
# for i in range(384):
# 	anim.step()
# 	led.update()
#
# led.fillOff()
#
# #evenly distributed rainbow
# anim = RainbowCycle(led)
# for i in range(384*2):
# 	anim.step()
# 	led.update()
#
# led.fillOff()