import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
from glob import glob

# Regex for filenames
fname_re = re.compile('data/W1_D.*_W(.*)_L(.*)_NMOS.*')

# Read in data and remove unnecessary columns+units
Ws, Ls, Vts = [], [], []
for f in glob('data/W1_D4_W*_L*_NMOS_VgId_loVd.txt'):
    matches = fname_re.search(f)
    Ws.append(float(matches.group(1)))
    Ls.append(float(matches.group(2)))
    data = pd.read_csv(f, sep='\t')
    data = data.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
    data = data.applymap(helper.convert_units)
    data = data[data.Vsubs == 0]
    slope = np.gradient(data.Idrain)/np.gradient(data.Vgate)
    max_slope_i, max_slope = np.argmax(slope), np.max(slope)
    Vt = data.Vgate[max_slope_i]-data.Idrain[max_slope_i]/max_slope
    Vts.append(Vt)

    # Set the font dictionaries (for plot title and axis titles)
    title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
    axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('Threshold voltage ($V_T$) at small channel lengths (W=4um)')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('$V_T$ (V)', **axis_font)
plt.semilogx(Ls, Vts, '.', markersize=10)
plt.savefig('figures/min_size.eps', format='eps', dpi=1000)
plt.show()