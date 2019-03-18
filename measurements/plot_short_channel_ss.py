import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
from glob import glob

# Regex for filenames
fname_re = re.compile('data/W1_D.*_W(.*)_L(.*)_NMOS.*')

# Read in data and remove unnecessary columns+units
Ws, Ls, sss = [], [], []
for f in glob('data/W1_D1_W*_L*_NMOS_VgId_hiVd.txt'):
    matches = fname_re.search(f)
    Ws.append(float(matches.group(1)))
    Ls.append(float(matches.group(2)))
    data = pd.read_csv(f, sep='\t')
    data = data.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
    data = data.applymap(helper.convert_units)
    data = data[data.Vsubs == 0]
    ss = 1E3/np.max(np.gradient(helper.smooth(np.log10(data.Idrain), box_pts=3))/np.gradient(data.Vgate))
    sss.append(ss)

    # Set the font dictionaries (for plot title and axis titles)
    title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
    axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('Subthreshold swing at different channel lengths')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('Subthreshold swing (mV/dec)', **axis_font)
#plt.ylim(0,250)
plt.loglog(Ls, sss, '.', markersize=10)
plt.savefig('figures/short_channel_ss.eps', format='eps', dpi=1000)
plt.show()