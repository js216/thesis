import numpy as np
import matplotlib
import matplotlib.pyplot as plt

##############################
## Figure setup ##############
##############################

matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams.update({'font.size': 20})

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,5))

##############################
## Plot           ############
##############################

# load from file
data = np.loadtxt("Bmot_data.csv")

# plot data
for i,d in enumerate(data[1:]):
    ax.plot(1e3*data[0], 1e6*d, color='black', lw=.5)

# plot labels
ax.set_ylabel("\\$\Delta f_0\\$ [mHz]", labelpad=15)
ax.set_xlabel("\\$B_\\text{res}\\$ [mG]", labelpad=15)
ax.text(20,4.25,"\\$m_\\text{F}\\$ or \\$m_J,m_\\text{Tl}\\$",rotation=25)
ax.text(35,4.80,"\\$m_J\\$ or \\$m_\\text{Tl},m_\\text{F}\\$",rotation=20)
ax.text(32,2.25,"\\$m_\\text{Tl}\\$ or \\$m_J,m_\\text{F}\\$",rotation=10)

# plot format
ax.grid()

##############################
## Save to file ##############
##############################

plt.tight_layout()
plt.savefig('Bmot.svg', bbox_inches='tight', dpi=600)
