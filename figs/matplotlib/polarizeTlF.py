import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams['axes.titlepad'] = 10
matplotlib.rcParams['font.size'] = 27
matplotlib.rcParams['legend.borderpad'] = 1
matplotlib.rcParams['legend.borderaxespad'] = .5
matplotlib.rcParams['legend.labelspacing'] = 2

# import data
P_arr = np.loadtxt("P_arr.csv")
Ez_arr = np.loadtxt("Ez_arr.csv")

# setup figure
fig, axx = plt.subplots(nrows=1, ncols=2, figsize=(12,5))

axx[0].plot(Ez_arr/1e3, 100*P_arr[:,0],  color="black", lw=2, label="\$(0,0)\$")
axx[0].plot(Ez_arr/1e3, 100*P_arr[:,4],  color="black", lw=4, ls="-", label="\$(1,\pm1)\$")
axx[0].plot(Ez_arr/1e3, 100*P_arr[:,12], color="black", lw=4, ls=":", label="\$(1,0)\$")

axx[1].plot(Ez_arr/1e3, 100*P_arr[:,16],  color="black", lw=2, label="\$(2,\pm2)\$")
axx[1].plot(Ez_arr/1e3, 100*P_arr[:,24],  color="black", lw=4, ls="-", label="\$(2,\pm1)\$")
axx[1].plot(Ez_arr/1e3, 100*P_arr[:,32], color="black", lw=4, ls=":", label="\$(2,0)\$")
 
for i in range(2):
    axx[i].set_xlabel("\\small \$E\$ [kV/cm]")
    axx[i].set_xlim((0,50))
    axx[i].set_ylim((-35,90))

    # grid
    axx[i].xaxis.set_major_locator(MultipleLocator(15))
    axx[i].yaxis.set_major_locator(MultipleLocator(25))
    axx[i].xaxis.set_minor_locator(AutoMinorLocator(3))
    axx[i].yaxis.set_minor_locator(AutoMinorLocator(5))
    axx[i].grid(which='minor', alpha=0.6, color="black", ls=":")
    axx[i].grid(which='major', alpha=0.6, color="black", ls="-")

fs = 13
axx[0].legend(fontsize=fs, loc='lower right')
axx[1].legend(fontsize=fs, loc='upper left')

axx[0].set_title("\\small\$J \leq 1\$")
axx[0].set_ylabel("\\small polarization [\%]")

axx[1].set_title("\\small\$J = 2\$")
axx[1].yaxis.set_label_position("right")
axx[1].yaxis.tick_right();

# save to file
plt.savefig('polarizeTlF.svg', bbox_inches='tight')
