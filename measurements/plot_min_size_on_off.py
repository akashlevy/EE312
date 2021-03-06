import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
from glob import glob

# Read in data and remove unnecessary columns+units
Ls, oors = [1,0.8,0.65,0.55,0.45], [0]*5
for f in glob('data/K4_Center_D4_*_IdVg_Vd100m.txt'):
    data = pd.read_csv(f, sep='\t')
    data = data.drop(columns=['Index'])
    data = data.applymap(helper.convert_units)
    data = data[data.Vsubs == 0]
    print(data.Idrain[-2:])
    print(data.Idrain[:2])
    oor = np.mean(data.Idrain[-2:])/np.mean(data.Idrain[:2])
    print(np.mean(data.Idrain[-2:]))
    print(np.mean(data.Idrain[:2]))
    print(oor)
    idx = int(f[18])
    print(idx)
    print()
    oors[idx-1] = oor

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('On/off ratio at small channel lengths (W=4um, $V_D$=100mV)')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('On/off ratio', **axis_font)
plt.semilogy(Ls, oors, '.', markersize=10)
plt.savefig('figures/min_size_on_off_ratio.eps', format='eps', dpi=1000)
plt.show()