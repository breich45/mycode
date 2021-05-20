#!/usr/bin/env python3
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

t = np.arange(0.0, 0.3, 0.4, 0.6) #LAN length of outage (mins)
    #t = np.arange(20.0, 35.0, 30.0, 35.0) #LAN length of outage (mins)
s = 1 + np.sin(2 * np.pi * t)
    #t2 = np.arange(25, 32, 34, 20) #WAN length of outage (min)
    
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='QTR (s)', ylabel='minutes',
    title='About as simple as it gets, folks')
ax.grid()
fig.savefig("test.png")
plt.show()    


