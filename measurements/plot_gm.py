import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data_lo = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_loVd.txt', sep='\t')
data_lo = data_lo.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data_lo = data_lo.applymap(helper.convert_units)
data_lo = data_lo[data_lo.Vsubs == 0]

data_hi = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_hiVd.txt', sep='\t')
data_hi = data_hi.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data_hi = data_hi.applymap(helper.convert_units)
data_hi = data_hi[data_hi.Vsubs == 0]

# Find max transconductance
max_gm_i, max_gm = np.argmax(data_lo.gm), np.max(data_lo.gm)
max_gm_vg = data_lo.Vgate[max_gm_i]

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('Transconductance for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{G}$ (V)', **axis_font)
ax1.set_ylabel('$g_m$ (uS) for $V_{D}=0.01V$', **axis_font)
ax2.set_ylabel('$g_m$ (uS) for $V_{D}=2V$', **axis_font)
lo_curve, = ax1.plot(data_lo.Vgate, data_lo.gm*1E6)
hi_curve, = ax2.plot(data_hi.Vgate, data_hi.gm*1E6, color='orange')
plt.legend([lo_curve, hi_curve], ['$V_{D}$=0.01V', '$V_{D}$=2V'])
plt.savefig('figures/gm.eps', format='eps', dpi=1000)
plt.show()