# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:18:39 2019

@author: Marc
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
    
Ls = np.array([0.45,0.5,0.75,1,2.5,5,25,100])
clm_lambda = np.array([0.307,0.272,0.247,0.319, 0.351,0.339, 0.316, 0.307])


# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('Channel Length Modulation Parameter at different channel lengths')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('$\lambda$ ($V^{-1}$)', **axis_font)
plt.semilogx(Ls, clm_lambda, '.', markersize=10)
plt.savefig('figures/channel_length_modulation.png', format='png', dpi=1000)
plt.show()