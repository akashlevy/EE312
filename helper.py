import numpy as np

'''Remove units from text cell'''
def convert_units(data):
    try:
        num, units = data.split()
    except ValueError:
        _, num, units = data.split()
    if units in ['A','V','S']:
        return float(num)
    elif units in ['mA', 'mV', 'mS']:
        return float(num) / 1E3
    elif units in ['uA', 'uV', 'uS']:
        return float(num) / 1E6
    elif units in ['nA', 'nV', 'nS']:
        return float(num) / 1E9
    elif units in ['pA', 'pV', 'pS']:
        return float(num) / 1E12
    elif units in ['fA', 'fV', 'fS']:
        return float(num) / 1E15
    else:
        raise Exception('Bad units: %s in %s' % (units, data))

'''Smooth using filter'''
def smooth(y, box_pts=7):
    box = np.ones(box_pts) / box_pts
    return np.concatenate((y[:box_pts/2], np.convolve(y, box, mode='valid'), y[-box_pts/2+1:]))
