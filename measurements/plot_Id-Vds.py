import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data = pd.read_csv('data/W1_D1_W100_L100_NMOS_VdId_Vgsweep.txt', sep='\t')
data = data.drop(columns=['Index','IdrainPerWg'])
data = data.applymap(helper.convert_units)

# Pick gate voltages to sample
Vgates = np.linspace(0, 3, num=7)

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('$I_{DS}$-$V_{DS}$ characteristics for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{DS}$ (V)', **axis_font)
plt.ylabel('$I_{DS}$ (uA)', **axis_font)
lines = []
for Vgate in Vgates:
    dataVg = data[data.Vgate == Vgate]
    line, = plt.plot(dataVg.Vdrain, helper.smooth(dataVg.Idrain)*1E6)
    lines.append(line)
plt.legend(lines, ['$V_{G}$=%sV' % Vgate for Vgate in Vgates])
plt.savefig('figures/Id-Vds.eps', format='eps', dpi=1000)
plt.show()