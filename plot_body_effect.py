import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
import helper

# Read in data and remove unnecessary columns+units
data = pd.read_csv('data/W1_D1_W100_L100_NMOS_VgId_Vd100m_bodysweep.txt', sep='\t')
data = data.drop(columns=['Index','IdrainPerWg','IsubsPerWg','gmPerWg'])
data = data.applymap(helper.convert_units)
#print(data)

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
Vts = np.zeros(shape=(1,5))
sqrtVbs = np.zeros(shape=(1,5))
i=0
for Vsub in Vsubs:
    dataVg = data[data.Vsubs == Vsub]
    slope = np.gradient(dataVg.Idrain)/np.gradient(dataVg.Vgate)
    max_slope_i, max_slope = np.argmax(slope), np.max(slope)
    Vt = dataVg.Vgate[max_slope_i+np.size(dataVg,0)*i]-dataVg.Idrain[max_slope_i+np.size(dataVg,0)*i]/max_slope
    Vts[0,i] = Vt
    sqrtVbs[0,i]=(np.sqrt(-1*Vsub))
    line, = plt.semilogy(dataVg.Vgate, helper.smooth(dataVg.Idrain, box_pts=3))
    lines.append(line)
    i+=1

plt.legend(lines, ['$V_{B}$=%sV' % Vsub for Vsub in Vsubs])
plt.savefig('figures/body_effect.png', format='png', dpi=1000)
plt.show()
print("Body Vts: ", Vts)
print("Body sqrtVbs: ", sqrtVbs)


# Finding gamma by either the mean of each gamma, or curve fitting
deltaVt = Vts-Vts[0,0]
gamma = deltaVt[0,1:]/sqrtVbs[0,1:]
gamma_avg = np.mean(gamma)
gamma_polyfit = np.polyfit(sqrtVbs[0,:], deltaVt[0,:], 1)

plt.figure(2)
plt.title('Body Effect Parameter Extraction')
plt.xlabel('$\sqrt{V_{sb}}$ ($V^{-1/2}$)', **axis_font)
plt.ylabel('$\Delta V_{th}$ ($V^{-1}$)', **axis_font)
plt.plot(sqrtVbs[0,:], deltaVt[0,:], '.',markersize=10)
fitplot=gamma_polyfit[0]*sqrtVbs[0,:]+gamma_polyfit[1]
plt.plot(sqrtVbs[0,:],fitplot, '--',markersize=10)
plt.savefig('figures/gamma_plotting.png', format='png', dpi=1000)
plt.show()


print("gammas: ", gamma)
print("gamma_avg: ", gamma_avg)
print("gamma_polyfit: ", gamma_polyfit)