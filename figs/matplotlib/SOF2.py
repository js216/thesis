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
data2 = np.loadtxt("SOF2.csv", delimiter=",")
df    = data2[0]
sof1  = data2[1]
sof2  = data2[2]
sof3  = data2[3]
sof4  = data2[4]

# setup figure
fig, axx = plt.subplots(nrows=1, ncols=2, figsize=(12,5), gridspec_kw={'width_ratios': [3,1]})

# left plot
axx[0].plot(df, sof1, color="gray", lw=4, label="\$l=1\cm\$")
axx[0].plot(df, sof2, color="black", lw=2, label="\$l=10\cm\$")
axx[0].set_ylabel("\${S_{\\gls{SOF}}}\$")
axx[0].set_title("(a)")
axx[0].xaxis.set_major_locator(MultipleLocator(200))
axx[0].xaxis.set_minor_locator(AutoMinorLocator(4))

# right plot
axx[1].plot(df, sof4, color="gray", lw=7, label="\$l=1\cm\$")
axx[1].plot(df, sof3, color="black", lw=2, label="\$l=10\cm\$")
axx[1].set_ylabel("\$\\ex{\widetilde P_{p,q}}_\\text{BG}\$")
axx[1].set_title("(b)")
axx[1].set_xlim((-50,50))
axx[1].yaxis.set_label_position("right")
axx[1].yaxis.tick_right();
axx[1].xaxis.set_major_locator(MultipleLocator(50))
axx[1].xaxis.set_minor_locator(AutoMinorLocator(5))

for i in range(2):
    axx[i].set_xlabel("\$\\Delta f\$ [Hz]")
    #axx[i].legend(fontsize=16)
    axx[i].axvline(x=0, color='k', lw=2)
    axx[i].yaxis.set_major_locator(MultipleLocator(.5))
    axx[i].yaxis.set_minor_locator(AutoMinorLocator(5))
    axx[i].grid(which='minor', alpha=0.6, color="black", ls=":")
    axx[i].grid(which='major', alpha=0.8, color="black", ls="-")

# save to file
plt.savefig('SOF2.svg', bbox_inches='tight')
