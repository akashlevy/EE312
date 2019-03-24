import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
    
Ls = np.array([0.45,0.5,0.75,1,2.5,5,25,100])
Vt_lo = np.array([1.22,1.08,1.42,1.5,1.53,1.52,1.58,1.63])
Vt_hi = np.array([0.77,0.69,1.15,1.39,1.59,1.66,1.74,1.86])

# Find DIBL
dibl_mv = 1000*np.absolute(Vt_hi-Vt_lo)/(0.9)
print("DIBL: %s mv/V " % dibl_mv)


# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
fig, ax1 = plt.subplots()
plt.title('Threshold voltage ($V_T$) at different channel lengths')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('$V_T$ (V)', **axis_font)
plt.ylim(0,2)
lo_vd, = ax1.semilogx(Ls, Vt_lo, '.', markersize=10, color='red')
hi_vd, = ax1.semilogx(Ls, Vt_hi, '.', markersize=10, color='blue')
plt.legend([lo_vd, hi_vd], ['$V_{D}$=0.1V', '$V_{D}$=1.0V'])
plt.savefig('figures/short_channel_100mVd_1Vd.png', format='png', dpi=1000)
plt.show()

plt.figure(2)
plt.title('DIBL at different channel lengths')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('$\Delta V_{th}/V_{DS}$ (mV/V)', **axis_font)
plt.semilogx(Ls, dibl_mv, '.', markersize=10)
plt.savefig('figures/short_channel_DIBL.png', format='png', dpi=1000)
plt.show()