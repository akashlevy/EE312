import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
from glob import glob

Ls = np.array([0.45,0.5,0.75,1,2.5,5,25,100])
gm_peak_lo = np.array([1.58E-03,1.92E-03,1.76E-03,1.25E-03,3.93E-04,1.88E-04,3.58E-05,8.70E-06])
gm_peak_hi = np.array([7.71E-03,8.58E-03,7.94E-03,7.13E-03,3.29E-03,1.69E-03,3.32E-04,8.98E-05])

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
fig, ax1 = plt.subplots()
plt.title('Peak transconductance ($g_m$) at different channel lengths')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('$g_m$ (S)', **axis_font)
lo_vd, = ax1.loglog(Ls, gm_peak_lo, '.', markersize=10, color='red')
hi_vd, = ax1.loglog(Ls, gm_peak_hi, '.', markersize=10, color='blue')
plt.legend([lo_vd, hi_vd], ['$V_{D}$=0.1V', '$V_{D}$=1.0V'])
plt.savefig('figures/short_channel_gm_peak_100mVd_1Vd.png', format='png', dpi=1000)
plt.show()