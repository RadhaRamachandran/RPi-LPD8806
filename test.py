#!/usr/bin/python

from bootstrap import *

# anim = Wave(led, Color(255, 0, 0), 4)
# for i in range(10):
# 	anim.step()
# 	led.update()
#
# led.fillOff()
# sleep(5)
#
# anim = Wave(led, Color(0, 0, 100), 4)
# for i in range(50):
# 	anim.step()
# 	led.update()
#
# led.fillOff()


# #rolling rainbow
# anim = Rainbow(led)
# for i in range(50):
# 	anim.step()
# 	led.update()
#
# led.fillOff()
#
#
# print 'case 2'
# #rolling rainbow
# anim = Rainbow(led)
# for i in range(384):
# 	anim.step()
# 	led.update()
#
# led.fillOff()

# #evenly distributed rainbow
# anim = RainbowCycle(led)
# for i in range(384*2):
# 	anim.step()
# 	led.update()
#
# led.fillOff()

colors = [
	(255.0,0.0,0.0), #red
	(0.0,255.0,0.0), #green
	(0.0,0.0,255.0), #blue
	(255.0,255.0,255.0), #white
]

for color in colors:
    list = []
    list.append(Color(color))

anim = PartyMode(led, list)
for i in range(20):
    anim.step()
    led.update()
led.fillOff()


FireFlies(led, list)
for i in range(20):
    anim.step()
    led.update()
led.fillOff()