# the fundamental sigpy imports: numpy, sigpy (here as submodules)
import numpy as np
import pulpy.rf as rf
import sigpy.plot as pl
import scipy.io as sio
import matplotlib.pyplot as pyplot

dim = 40  # size of the b1 matrix loaded
n_spokes = 5
fov = 20  # cm
dx_max = 2  # cm
gts = 4E-6
sl_thick = 5  # slice thickness, mm
tbw = 4
dgdtmax = 18000  # g/cm/s
gmax = 2  # g/cm
# load masked complex sensitivities - a 4 channel system
sens_file = sio.loadmat('data/b1maps_40.mat')
sens = np.transpose(sens_file['b1'], (2, 0, 1))  # transpose to Nc dim dim conv
pl.ImagePlot(sens, title='Sensitivity profiles')

target = sens_file['mask'].astype(complex)
[pulses, g] = rf.ptx.stspk(target, sens, n_spokes, fov, dx_max, gts, sl_thick, tbw,
                 dgdtmax, gmax, alpha=1)

pyplot.plot(np.real(pulses.T))
pyplot.title('Spokes real(RF)')
pyplot.ylabel('a.u.')
pyplot.xlabel('sample #')
pyplot.show()
pyplot.plot(np.real(g.T))
pyplot.legend(['Gx', 'Gy','Gz'])
pyplot.title('Spokes gradients')
pyplot.ylabel('G/cm')
pyplot.xlabel('sample #')
pyplot.show()

