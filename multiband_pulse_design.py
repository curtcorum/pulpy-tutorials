import numpy as np

import pulpy as pp
import pulpy.rf as rf

import sigpy.plot as pl
import scipy.signal as signal
import matplotlib.pyplot as pyplot

tb = 8
tb = 8
N = 512
d1 = 0.01
d2 = 0.01
p_type = 'ex'
f_type = 'ls'

sl_sep = 3 # cm
sl_thick = 0.3 # cm
g_max = 4 # gauss/cm
g_slew = 18000 # gauss/cm/s
dt = 4e-6 # seconds, dwell time
b1_max = 0.18 # gauss
[rf_pins, g_pins] = rf.multiband.dz_pins(tb, sl_sep, sl_thick, g_max, g_slew, dt, b1_max, p_type, f_type, d1, d2)

t = np.arange(0, np.size(rf_pins)) * dt
pyplot.figure()
pyplot.plot(t * 1000, np.real(rf_pins))
pyplot.ylabel('Gauss')
pyplot.xlabel('milliseconds')
pyplot.show()

pyplot.figure()
pyplot.plot(t * 1000, g_pins)
pyplot.ylabel('Gauss/cm')
pyplot.xlabel('milliseconds')
pyplot.show()

