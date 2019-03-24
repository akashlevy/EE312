import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_loandhiVd.txt', sep='\t')
data = data.drop(columns=['Index'])
data = data.applymap(helper.convert_units)
data_lo = data[data.VD == 0.1]
slope = np.gradient(data_lo.ID)/np.gradient(data_lo.VG)
max_slope_i, max_slope = np.argmax(slope), np.max(slope)

data_hi = data[data.VD == 1]
slope_hi = np.gradient(data_hi.ID)/np.gradient(data_hi.VG)
max_slope_hi_i, max_slope_hi = np.argmax(slope_hi), np.max(slope_hi)


## Find max transconductance
#max_gm_i, max_gm = np.argmax(data_lo.gm), np.max(data_lo.gm)
#max_gm_vg = data_lo.Vgate[max_gm_i]
#
#max_gm_hi_i, max_gm_hi = np.argmax(data_hi.gm), np.max(data_hi.gm)
#max_gm_hi_vg = data_lo.Vgate[max_gm_i]

print("max gm at low Vd: %s S" % max_slope)
print("max gm at high Vd: %s S" % max_slope_hi)

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('Transconductance for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{G}$ (V)', **axis_font)
ax1.set_ylabel('$g_m$ (uS) for $V_{D}=0.1V$', **axis_font)
ax1.set_xlabel('$V_{G}$ (V)', **axis_font)
ax2.set_ylabel('$g_m$ (uS) for $V_{D}=1V$', **axis_font)
lo_curve, = ax1.plot(data_lo.VG, slope*1E6, color='red')
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', colors='red')
hi_curve, = ax2.plot(data_hi.VG, slope_hi*1E6, color='blue')
ax2.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', colors='blue')
plt.legend([lo_curve, hi_curve], ['$V_{D}$=0.1V', '$V_{D}$=1.0V'])
plt.savefig('figures/gm_W100L100_widerange.png', format='png', dpi=1000)
plt.show()
