import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data_lo = pd.read_csv('data/W1_D9_ParasiticNMOS1_VgId.txt', sep='\t')
data_lo = data_lo.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data_lo = data_lo.applymap(helper.convert_units)
data_lo = data_lo[data_lo.Vsubs == 0]
slope = np.gradient(data_lo.Idrain)/np.gradient(data_lo.Vgate)
max_slope_i, max_slope = np.argmax(slope), np.max(slope)
Vt = data_lo.Vgate[max_slope_i]-data_lo.Idrain[max_slope_i]/max_slope
fit_curve_lo = max_slope*(data_lo.Vgate - Vt)
print("lo: x,y=", data_lo.Vgate[max_slope_i], max_slope)
print("lo: ", Vt)

data_hi = pd.read_csv('data/W1_D9_ParasiticNMOS2_VgId.txt', sep='\t')
data_hi = data_hi.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data_hi = data_hi.applymap(helper.convert_units)
data_hi = data_hi[data_hi.Vsubs == 0]
slope = np.gradient(data_hi.Idrain)/np.gradient(data_hi.Vgate)
max_slope_i, max_slope = np.argmax(slope), np.max(slope)
Vt = data_hi.Vgate[max_slope_i]-data_hi.Idrain[max_slope_i]/max_slope
fit_curve_hi = max_slope*(data_hi.Vgate - Vt)
print("hi: x,y=", data_hi.Vgate[max_slope_i], max_slope)
print("hi: ", Vt)

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('$I_{DS}$-$V_G$ for Parasitic NMOS Devices')
plt.xlabel('$V_{G}$ (V)', **axis_font)
plt.xlim(-5, 5)
ax1.set_ylabel('$I_{DS}$ (pA) for Parasitic NMOS 1', **axis_font)
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', colors='red')
ax1.set_xlabel('$V_{G}$ (V)', **axis_font)
ax2.set_ylabel('$I_{DS}$ (uA) for Parasitic NMOS 2', **axis_font)
ax2.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', colors='blue')
#ax1.set_ylim(-0.1, 3)
#ax2.set_ylim(-10, 300)
lo_curve, = ax1.plot(data_lo.Vgate, helper.smooth(data_lo.Idrain, box_pts=3)*1E12, color='red')
hi_curve, = ax2.plot(data_hi.Vgate, helper.smooth(data_hi.Idrain, box_pts=3)*1E6)
plt.legend([lo_curve, hi_curve], ['Parasitic NMOS 1', 'Parasitic NMOS 2'])
plt.savefig('figures/Id-Vg-Parasitics.png', format='png', dpi=1000)
plt.show()
