import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_loVd.txt', sep='\t')
data = data.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data = data.applymap(helper.convert_units)
data = data[data.Vsubs == 0]
slope = np.gradient(data.Idrain)/np.gradient(data.Vgate)
max_slope_i, max_slope = np.argmax(slope), np.max(slope)
Vt = data.Vgate[max_slope_i]-data.Idrain[max_slope_i]/max_slope
fit_curve = max_slope*(data.Vgate - Vt)
print("x,y=", data.Vgate[max_slope_i], max_slope)
print(Vt)

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('$I_{DS}$-$V_G$ for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{G}$ (V)', **axis_font)
plt.ylabel('$I_{DS}$ (uA)', **axis_font)
plt.xlim(0, 4)
plt.ylim(-0.1, 2)
plt.plot(data.Vgate, helper.smooth(data.Idrain, box_pts=3)*1E6)
plt.plot(data.Vgate, fit_curve*1E6, '--')
plt.plot([-2,5],[0,0], '--')
plt.savefig('figures/Id-Vg.eps', format='eps', dpi=1000)
plt.show()