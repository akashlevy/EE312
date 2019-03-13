import matplotlib.pyplot as plt
import numpy as np
import pandas as pd, pylab
from intersection import intersection

offsets = [-7.302313306441e-01, -7.881100181946e-01, 4.983993902248e-02, -5.585779002449e-01]
cross_names = ['Parasitic NMOS 1', 'Parasitic NMOS 2', 'Normal NMOS S/D', 'Normal NMOS Gate']

for i in range(4):
    # Read in Sentaurus data for final profile and subtract out offset
    sim_f = pd.read_csv('final_profile_%d.csv' % (i+1), header=None, names=['X','As','X2','B'], skiprows=1)
    sim_f = sim_f.drop(columns=['X2'])
    xi = sim_f['X'][0]
    sim_f['X'] -= xi
    print 'B (Sentaurus):', intersection(sim_f['X'], sim_f['B'], sim_f['X'], sim_f['As'])
    
    calc_i = {}
    b_vt_init_fn = lambda x: 1.86204E18 * np.exp(-68.0782 * (-0.296 + x + xi)**2)
    b_isolation_init_fn = lambda x: 8.25967E19 * np.exp(-214.326 * (-0.114 + x + xi)**2)
    as_sd_init_fn = lambda x: 5.24924E20 * np.exp(-2164.13 * (-0.0362 + x + xi - offsets[i])**2)
    calc_i['X'] = np.linspace(-2, 5, 1000)
    calc_i['B_VT'] = b_vt_init_fn(calc_i['X'])
    calc_i['B_iso'] = b_isolation_init_fn(calc_i['X'])
    calc_i['As_SD'] = as_sd_init_fn(calc_i['X'])

    calc_f = {}
    b_vt_final_fn = lambda x: 7.10632E17 * np.exp(-9.91561 * (-0.296 + x + xi)**2)
    b_isolation_final_fn = lambda x: 1.87791E19 * np.exp(-11.079 * (-0.114 + x + xi)**2)
    as_final_fn = lambda x: 4.32491E20 * np.exp(-1469.07 * (-0.0362 + x + xi - offsets[i])**2)
    calc_f['X'] = np.linspace(-2, 5, 1000)
    calc_f['B_VT'] = b_vt_final_fn(calc_f['X'])
    calc_f['B_iso'] = b_isolation_final_fn(calc_f['X'])
    calc_f['As'] = as_final_fn(calc_f['X'])
    print 'B_VT:', intersection(calc_f['X'], calc_f['B_VT'], calc_f['X'], calc_f['As'])
    print 'B:', intersection(calc_f['X'], calc_f['B_VT']+calc_f['B_iso'], calc_f['X'], calc_f['As'])

    # Set the font dictionaries (for plot title and axis titles)
    title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold',
                'verticalalignment':'bottom'} # Bottom vertical alignment for more space
    axis_font = {'fontname':'Arial', 'size':'12'}

    # Plot data
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=True, figsize=(6.5, 9))
    plt.xlim(0, 4)
    plt.ylim(1e9, 1e22)
    plt.xlabel('Depth ($\mu$m)', **axis_font)
    fig.text(0.005, 0.5, '[Dopant] (cm$^{-3}$)', va='center', rotation='vertical', **axis_font)

    if i in [0,1]:
        lines = [None]*10
        ax1.set_title('Diffusion profiles for %s' % cross_names[i], **title_font)
        ax1.set_yscale('log')
        lines[0], = ax1.plot(calc_f['X'], calc_f['B_VT'] + calc_f['B_iso'])
        lines[1], = ax1.plot(calc_f['X'], calc_f['As'])
        lines[2], = ax1.plot(calc_i['X'], calc_i['B_VT'], linestyle=':', linewidth=1)
        lines[3], = ax1.plot(calc_i['X'], calc_i['B_iso'], linestyle=':', linewidth=1)
        lines[4], = ax1.plot(calc_i['X'], calc_i['As_SD'], linestyle=':', linewidth=1)
        ax1.legend(lines[:5], ['[B]$_{final}$ (hand)', '[As]$_{final}$  (hand)', '[B $V_T$ adjust]$_{init}$ (hand)', '[B isolation]$_{init}$  (hand)', '[As S/D]$_{init}$  (hand)'])

        ax2.set_yscale('log')
        lines[5], = ax2.plot(sim_f['X'], sim_f['B'])
        lines[6], = ax2.plot(sim_f['X'], sim_f['As'])
        ax2.legend(lines[5:], ['[B]$_{final}$ (Sentaurus)', '[As]$_{final}$ (Sentaurus)', '[B $V_T$ adjust]$_{init}$ (hand)', '[B isolation]$_{init}$  (hand)', '[As S/D]$_{init}$  (hand)'])
    else:
        lines = [None]*8
        ax1.set_title('Diffusion profiles for %s' % cross_names[i], **title_font)
        ax1.set_yscale('log')
        lines[0], = ax1.plot(calc_f['X'], calc_f['B_VT'])
        lines[1], = ax1.plot(calc_f['X'], calc_f['As'])
        lines[2], = ax1.plot(calc_i['X'], calc_i['B_VT'], linestyle=':', linewidth=1)
        lines[3], = ax1.plot(calc_f['X'], calc_i['As_SD'], linestyle=':', linewidth=1)
        ax1.legend(lines[:4], ['[B]$_{final}$ (hand)', '[As]$_{final}$  (hand)', '[B $V_T$ adjust]$_{init}$ (hand)', '[As S/D]$_{init}$  (hand)'])

        ax2.set_yscale('log')
        lines[4], = ax2.plot(sim_f['X'], sim_f['B'])
        lines[5], = ax2.plot(sim_f['X'], sim_f['As'])
        ax2.legend(lines[4:], ['[B]$_{final}$ (Sentaurus)', '[As]$_{final}$ (Sentaurus)', '[B $V_T$ adjust]$_{init}$ (hand)', '[As S/D]$_{init}$  (hand)'])

    plt.show()
    fig.savefig('output_figure%d.eps' % (i+1), format='eps', dpi=1000)