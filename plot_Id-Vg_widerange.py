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
Vt = data_lo.VG[max_slope_i]-data_lo.ID[max_slope_i]/max_slope
fit_curve_lo = max_slope*(data_lo.VG - Vt)
print("lo: x,y=", data_lo.VG[max_slope_i], max_slope)
print("lo: ", Vt)

data_hi = data[data.VD == 1]
slope = np.gradient(data_hi.ID)/np.gradient(data_hi.VG)
max_slope_i, max_slope = np.argmax(slope), np.max(slope)
Vt = data_hi.VG[max_slope_i+data_lo.shape[0]]-data_hi.ID[max_slope_i+data_lo.shape[0]]/max_slope
fit_curve_hi = max_slope*(data_hi.VG - Vt)
print("hi: x,y=", data_hi.VG[max_slope_i+data_lo.shape[0]], max_slope)
print("hi: ", Vt)

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('$I_{DS}$-$V_G$ for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{G}$ (V)', **axis_font)
plt.xlim(-2, 10)
ax1.set_ylabel('$I_{DS}$ (uA) for $V_{D}$=0.1V', **axis_font)
ax1.set_xlabel('$V_{G}$ (V)', **axis_font)
ax2.set_ylabel('$I_{DS}$ (uA) for $V_{D}$=1.0V', **axis_font)
ax1.set_ylim(-2, 35)
ax2.set_ylim(-20, 350)
lo_curve, = ax1.plot(data_lo.VG, helper.smooth(data_lo.ID, box_pts=3)*1E6, color='red')
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', colors='red')
ax1.plot(data_lo.VG, fit_curve_lo*1E6, '--', color='violet')
hi_curve, = ax2.plot(data_hi.VG, helper.smooth(data_hi.ID, box_pts=3)*1E6)
ax2.plot(data_hi.VG, fit_curve_hi*1E6, '--')
ax2.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', colors='blue')
plt.plot([-2,10],[0,0], '--')
plt.legend([lo_curve, hi_curve], ['$V_{D}$=0.1V', '$V_{D}$=1.0V'])
plt.savefig('figures/Id-Vg_widerange.png', format='png', dpi=1000)
plt.show()
