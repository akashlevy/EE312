import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data_lo = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_loVd.txt', sep='\t')
data_lo = data_lo.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data_lo = data_lo.applymap(helper.convert_units)
data_lo = data_lo[data_lo.Vsubs == 0]
max_slope = 1E3/np.max(np.gradient(np.log10(data_lo.Idrain[51:]))/np.gradient(data_lo.Vgate[51:]))
print("Subthreshold slope: %s mV/dec" % max_slope)

data_hi = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_hiVd.txt', sep='\t')
data_hi = data_hi.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data_hi = data_hi.applymap(helper.convert_units)
data_hi = data_hi[data_hi.Vsubs == 0]
max_slope = 1E3/np.max(np.gradient(np.log10(data_hi.Idrain[51:]))/np.gradient(data_hi.Vgate[51:]))
print("Subthreshold slope: %s mV/dec" % max_slope)

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('$I_{DS}$-$V_G$ for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{G}$ (V)', **axis_font)
plt.xlim(0, 5)
ax1.set_ylabel('$I_{DS}$ (uA) for $V_{D}$=0.01V', **axis_font)
ax1.set_xlabel('$V_{G}$ (V)', **axis_font)
ax2.set_ylabel('$I_{DS}$ (uA) for $V_{D}$=2V', **axis_font)
lo_curve, = ax1.semilogy(data_lo.Vgate, helper.smooth(data_lo.Idrain, box_pts=3)*1E6, color='red')
hi_curve, = ax2.semilogy(data_hi.Vgate, helper.smooth(data_hi.Idrain, box_pts=3)*1E6)
plt.plot([-2,5],[0,0], '--')
plt.legend([lo_curve, hi_curve], ['$V_{D}$=0.01V', '$V_{D}$=2V'])
plt.savefig('figures/logId-Vg_W100L100.png', format='png', dpi=1000)
plt.show()


####Second Device

## Read in data and remove unnecessary columns+units
#data_lo = pd.read_csv('data/W1_D1_W100_L1_NMOS_VgId_loVd.txt', sep='\t')
#data_lo = data_lo.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
#data_lo = data_lo.applymap(helper.convert_units)
#data_lo = data_lo[data_lo.Vsubs == 0]
#max_slope = 1E3/np.max(np.gradient(np.log10(data_lo.Idrain[51:]))/np.gradient(data_lo.Vgate[51:]))
#print("Subthreshold slope: %s mV/dec" % max_slope)
#
#data_hi = pd.read_csv('data/W1_D1_W100_L1_NMOS_VgId_hiVd.txt', sep='\t')
#data_hi = data_hi.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
#data_hi = data_hi.applymap(helper.convert_units)
#data_hi = data_hi[data_hi.Vsubs == 0]
#max_slope = 1E3/np.max(np.gradient(np.log10(data_hi.Idrain[51:]))/np.gradient(data_hi.Vgate[51:]))
#print("Subthreshold slope: %s mV/dec" % max_slope)
#
## Set the font dictionaries (for plot title and axis titles)
#title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
#axis_font = {'fontname':'Arial', 'size':'12'}
#
## Plot data
#fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()
#plt.title('$I_{DS}$-$V_G$ for L=1um W=100um nMOS transistor')
#plt.xlabel('$V_{G}$ (V)', **axis_font)
#plt.xlim(0, 5)
#ax1.set_ylabel('$I_{DS}$ (uA) for $V_{D}$=0.01V', **axis_font)
#ax2.set_ylabel('$I_{DS}$ (uA) for $V_{D}$=2V', **axis_font)
#lo_curve, = ax1.semilogy(data_lo.Vgate, helper.smooth(data_lo.Idrain, box_pts=3)*1E6, color='red')
#hi_curve, = ax2.semilogy(data_hi.Vgate, helper.smooth(data_hi.Idrain, box_pts=3)*1E6)
#plt.plot([-2,5],[0,0], '--')
#plt.legend([lo_curve, hi_curve], ['$V_{D}$=0.01V', '$V_{D}$=2V'])
#plt.savefig('figures/logId-Vg_W100L1.png', format='png', dpi=1000)
#plt.show()