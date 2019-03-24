import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
from glob import glob

# Read in data and remove unnecessary columns+units
Ls, Idrains = [1,0.8,0.65,0.55,0.45], [0]*5
for f in glob('data/K4_Center_D4_*_IdVg_Vd100m.txt'):
    data = pd.read_csv(f, sep='\t')
    data = data.drop(columns=['Index'])
    data = data.applymap(helper.convert_units)
    data = data[data.Vsubs == 0]
    idx = int(f[18])
    Vgate = data['Vgate']
    Idrains[idx-1] = data['Idrain']

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('$I_D$-$V_G$ at small channel lengths (W=4um, $V_D$=100mV)')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('$I_D$ (A)', **axis_font)
curves = []
for Idrain in Idrains:
    curve, = plt.semilogy(Vgate, Idrain)
    curves.append(curve)
plt.legend(curves, ['$L$=%s um' % L for L in Ls])
plt.savefig('figures/min_size_Id-Vg.eps', format='eps', dpi=1000)
plt.show()