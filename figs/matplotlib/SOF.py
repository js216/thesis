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
data = np.loadtxt("SOF.csv", delimiter=",")
d    = data[0]
SOF1 = data[1]
SOF2 = data[2]
Rabi = data[3]

# setup figure
fig, axx = plt.subplots(nrows=1, ncols=2, figsize=(12,5))

# plot the data
axx[0].plot(d, SOF1, color="black", lw=3, label="\\gls{SOF}")
axx[0].plot(d, Rabi, color="black", lw=2, ls="dashed", label="Rabi")
axx[1].plot(d, SOF2, color="black", lw=3, label="\$\\phi=\\pi/2\$")

for i in range(2):
    axx[i].set_xlabel("\$\\delta\$ [\$\\pi\\alpha/2l\$]")
    axx[i].set_xlim((-2,2))
    axx[i].set_ylim((0,1))
    axx[i].axvline(x=0, color='k', lw=2)

    # grid
    axx[i].xaxis.set_major_locator(MultipleLocator(2))
    axx[i].yaxis.set_major_locator(MultipleLocator(.5))
    axx[i].xaxis.set_minor_locator(AutoMinorLocator(4))
    axx[i].yaxis.set_minor_locator(AutoMinorLocator(5))
    axx[i].grid(which='minor', alpha=0.6, color="black", ls=":")
    axx[i].grid(which='major', alpha=0.8, color="black", ls="-")

fs = 16
axx[0].legend(fontsize=fs,)
axx[1].legend(fontsize=fs,)

axx[0].set_ylabel("\$\\ex{P_{p,q}}\$")

axx[0].set_title("(a)")
axx[1].set_title("(b)")

axx[1].yaxis.set_label_position("right")
axx[1].yaxis.tick_right();

# save to file
plt.savefig('SOF.svg', bbox_inches='tight')
