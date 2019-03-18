import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import re
import helper
from glob import glob

# Regex for filenames
fname_re = re.compile('data/W1_D.*_W(.*)_L(.*)_NMOS.*')

# Read in data and remove unnecessary columns+units
Ws, Ls, peak_gms = [], [], []
for f in glob('data/W1_D1_W*_L*_NMOS_VgId_hiVd.txt'):
    matches = fname_re.search(f)
    Ws.append(float(matches.group(1)))
    Ls.append(float(matches.group(2)))
    data = pd.read_csv(f, sep='\t')
    data = data.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
    data = data.applymap(helper.convert_units)
    data = data[data.Vsubs == 0]
    peak_gm = np.max(data.gm)
    peak_gms.append(peak_gm)

    # Set the font dictionaries (for plot title and axis titles)
    title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom'}
    axis_font = {'fontname':'Arial', 'size':'12'}

# Plot data
plt.title('Peak transconductance ($g_m$) at different channel lengths')
plt.xlabel('Channel Length $L$ (um)', **axis_font)
plt.ylabel('$g_m$ (S)', **axis_font)
#plt.ylim(0,2)
plt.semilogx(Ls, peak_gms, '.', markersize=10)
plt.savefig('figures/short_channel_gm_peak.eps', format='eps', dpi=1000)
plt.show()