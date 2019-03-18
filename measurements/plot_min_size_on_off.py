import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
from glob import glob

# Regex for filenames
fname_re = re.compile('data/W1_D.*_W(.*)_L(.*)_NMOS.*')

# Read in data and remove unnecessary columns+units
Ws, Ls, oors = [], [], []
for f in glob('data/W1_D4_W*_L*_NMOS_VgId_hiVd.txt'):
    matches = fname_re.search(f)
    Ws.append(float(matches.group(1)))
    Ls.append(float(matches.group(2)))
    data = pd.read_csv(f, sep='\t')
    data = data.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
    data = data.applymap(helper.convert_units)
    data = data[data.Vsubs == 0]
    oor = data.Idrain[len(data.Idrain)-10]/data.Idrain[10]
    oors.append(oor)

    # Set the font dictionaries (for plot title and axis titles)
    title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
    axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('On/off ratio at small channel lengths (W=4um, $V_D$=2V)')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('On/off ratio', **axis_font)
plt.loglog(Ls, oors, '.', markersize=10)
plt.savefig('figures/min_size_on_off_ratio.eps', format='eps', dpi=1000)
plt.show()