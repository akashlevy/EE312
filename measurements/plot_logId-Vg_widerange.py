import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_loandhiVd.txt', sep='\t')
data = data.drop(columns=['Index'])
data = data.applymap(helper.convert_units)
data_lo = data[data.VD == 0.1]
max_slope = 1E3/np.max(np.gradient(np.log10(data_lo.ID))/np.gradient(data_lo.VG))
print("Subthreshold swing: %s mV/dec" % max_slope)

data_hi = data[data.VD == 1]
max_slope = 1E3/np.max(np.gradient(np.log10(data_hi.ID))/np.gradient(data_hi.VG))
print("Subthreshold swing: %s mV/dec" % max_slope)

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()
plt.title('$I_{DS}$-$V_G$ for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{G}$ (V)', **axis_font)
plt.xlim(0, 5)
ax1.set_ylabel('$I_{DS}$ (uA)', **axis_font)
ax1.set_xlabel('$V_{G}$ (V)', **axis_font)
#ax2.set_ylabel('$I_{DS}$ (uA) for $V_{D}$=1V', **axis_font)
lo_curve, = ax1.semilogy(data_lo.VG, helper.smooth(data_lo.ID, box_pts=3)*1E6, color='red')
hi_curve, = ax1.semilogy(data_hi.VG, helper.smooth(data_hi.ID, box_pts=3)*1E6)
plt.plot([-2,5],[0,0], '--')
plt.legend([lo_curve, hi_curve], ['$V_{D}$=0.1V', '$V_{D}$=1.0V'])
plt.savefig('figures/logId-Vg_W100L100_widerange.png', format='png', dpi=1000)
plt.show()