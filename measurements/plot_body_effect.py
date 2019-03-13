import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_loVd.txt', sep='\t')
data = data.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data = data.applymap(helper.convert_units)
print(data)

# Pick gate voltages to sample
Vsubs = np.linspace(0, -2, num=5)

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('Body bias effect for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{G}$ (V)', **axis_font)
plt.ylabel('$I_{DS}$ (A)', **axis_font)
plt.xlim(0, 4)
lines = []
for Vsub in Vsubs:
    dataVg = data[data.Vsubs == Vsub]
    line, = plt.semilogy(dataVg.Vgate, helper.smooth(dataVg.Idrain, box_pts=3))
    lines.append(line)
plt.legend(lines, ['$V_{B}$=%sV' % Vsub for Vsub in Vsubs])
plt.savefig('figures/body.eps', format='eps', dpi=1000)
plt.show()