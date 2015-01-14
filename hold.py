
# #!/usr/bin/python
#
# from bootstrap import *
# import numpy as np
#
# inst_data = np.genfromtxt('inst_data.csv',delimiter=',', usecols = 3)
#
# red = Color()
#
# for i in inst_data:
#     print i
#     if i == 1:
#         print 'good'
#         level = 0.2
#         step = 0.1
#         dir = step
#         while level >= 0.2:
#             led.fill(Color(0.0, 255.0, 0.0, level))
#             led.update()
#             if(level >= 0.8):
#                 dir = -step
#             level += dir
#         led.fillOff()
#     elif i == 2:
#         print 'okay'
#         anim = Rainbow(led)
#         for i in range(10):
#             anim.step()
#             led.update()
#         led.fillOff()
#     elif i == 3:
#         print 'bad'
#         anim = ColorWipe(led, C)
#
# 	for i in range(num):
# 		anim.step()
# 		led.update()
#         led.fillOff()
#
#
#     else:
#         print 'UGLY'
#         anim = PartyMode(led, [Color(255.0,0.0,0.0), Color(255.0,255.0,255.0)])
#         for i in range(10):
#             anim.step()
#             led.update()
#         led.fillOff()
#
# led.all_off()


#!/usr/bin/python

from bootstrap import *
import numpy as np

inst_data = np.genfromtxt('inst_data.csv',delimiter=',', usecols = 3)

#green pulse

for i in inst_data:
    print i
    if i == 1:
        level = 0.4
        step = 0.05
        dir = step
        while level >= 0.4:
            led.fill(Color(0.0, 255.0, 0.0, level))
            led.update()
            if(level >= 0.7):
                dir = -step
            level += dir
    else:
        led.fill(Color(0.0, 0.0, 255.0, .2))

#led.all_off()