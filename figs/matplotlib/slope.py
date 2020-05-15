import numpy as np
import matplotlib
import matplotlib.pyplot as plt

##############################
## Figure setup ##############
##############################

matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams.update({'font.size': 16})

fig, axx = plt.subplots(ncols=2, figsize=(10,5))
axx[1].yaxis.set_label_position("right")
axx[1].yaxis.tick_right()

fs_legend = 7
fs_title = 20
fs_xlabel = 20
fs_ylabel = 20

##############################
## Electric field ############
##############################

# load data
slope = np.loadtxt("slope.csv")
labels = 2*["ej/hk/ek/hj", "eg/hf/ef/hg", "fj/gk/fk/gj", ]
labels = ["\\footnotesize "+x for x in labels]
lw_list = [4,2,1]

# plot data
for i in range(3):
    # new c3 term
    axx[0].plot(slope[0], slope[2*i+1], color="black", label=labels[i], lw=lw_list[i])
    
    # old c3 term
    axx[0].plot(slope[0], slope[2*i+2], color="black", ls='--', lw=lw_list[i])

# plot labels
axx[0].set_title("(a) Slope vs \$E_z\$", fontsize=fs_title)
axx[0].set_xlabel("\$E_z\$ [kV/cm]", fontsize=fs_xlabel)
axx[0].set_ylabel("\$\\d f_0/\\d E_z\$ [mHz/(V/cm)]", fontsize=fs_ylabel)
axx[0].legend(fontsize=fs_legend, labelspacing=2.5, borderpad=2)

# plot format
axx[0].grid()

##############################
## Magnetic field ############
##############################

# load data
s = np.loadtxt("all_B_slopes.csv")
labels = 2*["ej/hk/ek/hj", "eg/hf/ef/hg", "fj/gk/fk/gj", ]
lw_list = [4,2,1]
numbers = [[10,7,11,6], [10,9,11,8], [10,8,11,9],    [10,6,11,7], [8,7,9,6], [8,6,9,7],  ]
colors  = ["black",     "black",     "black",        "black",     "black",   "black"]
lw_list = 6*[1]
ls_list = ["solid",    "solid",     "solid",       "solid",     "solid",  "solid"]
labels  = ["\$m_\\text{Tl}\$",  "\$m_\\text{F}\$",     "\$m_J,m_\\text{Tl}\$", "\$m_J,m_\\text{F}\$", "\$m_J\$",   "\$m_\\text{Tl},m_\\text{F}\$"]
angles  = [-40,         -40,         -30,            -30,         -10,       1]
y_list  = [-68,         -64,         -50,            -47,         -18,       -5]
x_list  = [7,           8.5,         7,              8.5,           8,         6]
x_list = 0.9*np.array(x_list)
y_list = 1.3*np.array(y_list)

# plot data
for i in range(6):
    axx[1].plot(1e6*s[0], 1e6*s[i+1], label=labels[i], lw=lw_list[i], ls=ls_list[i], color="black")

# plot labels
axx[1].set_title("(b) Sensitivity to \$B_{ext}\$", fontsize=fs_title)
axx[1].set_xlabel("\$B_z\$ [\$\\mu\$G]", fontsize=fs_xlabel)
axx[1].set_ylabel("\$\Delta f_0\$ [mHz]", fontsize=fs_ylabel)
for x,y,l,a in zip(x_list,y_list,labels,angles):
    axx[1].text(x,y,l,rotation=a)

# plot format
axx[1].grid()

##############################
## Save to file ##############
##############################

plt.tight_layout()
plt.savefig('slope.svg', bbox_inches='tight', dpi=600)
