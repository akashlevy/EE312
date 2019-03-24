# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:34:46 2019

@author: Marc
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data = pd.read_csv('data/W1_D1_W100_L1_NMOS_VdId.txt', sep='\t')
data = data.drop(columns=['Index','IdrainPerWg'])
data = data.applymap(helper.convert_units)
data_smoothed = helper.smooth(data.Idrain, box_pts=3)
data_out = np.column_stack((data.Vdrain,data_smoothed))

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('$I_{DS}$-$V_DS$')
plt.xlabel('$V_{DS}$ (V)', **axis_font)
plt.ylabel('$I_{DS}$ (uA)', **axis_font)
#plt.xlim(0, 4)
#plt.ylim(-0.1, 2)
plt.plot(data.Vdrain, helper.smooth(data.Idrain, box_pts=3)*1E6)
#plt.yscale('log')
#plt.plot([-2,5],[0,0], '--')
#plt.savefig('figures/Id-Vg.png', format='png', dpi=1000)
plt.show()
