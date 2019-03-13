import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_loVd.txt', sep='\t')
data = data.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data = data.applymap(helper.convert_units)
data = data[data.Vsubs == 0]

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('Transconductance for L=100um W=100um nMOS transistor')
plt.xlabel('$V_{G}$ (V)', **axis_font)
plt.ylabel('$g_m$ (uS)', **axis_font)
plt.plot(data.Vgate, data.Idrain*1E6)
plt.savefig('figures/gm.eps', format='eps', dpi=1000)
plt.show()