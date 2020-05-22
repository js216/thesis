import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.gridspec import GridSpec

matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams['font.size'] = 10
x_font = 8
matplotlib.rcParams['legend.borderpad'] = 1
matplotlib.rcParams['legend.borderaxespad'] = .5
#matplotlib.rcParams['legend.labelspacing'] = 2

def arrow(ax, x0, x1, y0, y1, text, textxy=None, ha=None, va=None):
    # arrow graphics
    ax.annotate(s          = '',
                xy         = (x0, y0),
                xycoords   = 'data',
                xytext     = (x1, y1),
                textcoords = 'data',
                arrowprops = dict(arrowstyle="<->")
            )
    
    # arrow text
    if not textxy:
        textxy  = (((x0+x1)/2), (y0+y1)/2)
    ax.annotate(
        s          = text,
        xy         = textxy,
        xycoords   = 'data',
        fontsize   = matplotlib.rcParams['font.size'],
        textcoords = 'data',
        ha         = 'center' if not ha else ha,
        va         = "bottom" if not va else va
    )

###########################################
### Subplots       ########################
###########################################

# subplots
fig = plt.figure(figsize=(6,3.5))
gs1 = GridSpec(2, 2, wspace=0.05, hspace=0.05, width_ratios=[1,1.25], height_ratios=[.05,1])
axx = [fig.add_subplot(gs1[:, 0]),
       fig.add_subplot(gs1[1, 1]),
       fig.add_subplot(gs1[0, 1])]

#axx[0].get_shared_x_axes().join(axx[0], axx[1])
#axx[0].set_xticklabels([])


# rightmost plots should have ylabels on the right
axx[1].yaxis.tick_right()
axx[1].yaxis.set_label_position("right")

###########################################
### Fields vs time ########################
###########################################

# parameters
T0 = 3
eDCi, eDCf = 20, -20
TriseAC = T0
TfallAC = T0
TfallDC = 15 - TriseAC - TfallAC
eACmax = 12
deltaT = TfallDC
t = np.linspace(0,15,200)

# fields
DC_arr = eDCi*np.heaviside(T0-t,0) + \
            np.heaviside(t-T0,0)*np.heaviside(T0+TfallDC-t,0)*(((eDCf-eDCi)/(TfallDC))*(t-T0)+eDCi) + \
            eDCf*np.heaviside(t-T0-TfallDC,0)
AC_arr = np.heaviside(TriseAC-t,0)*eACmax/TriseAC*t + \
            np.heaviside(t-TriseAC,0)*np.heaviside(T0+deltaT-t,0)*eACmax + \
            np.heaviside(t-T0-deltaT,0)*np.heaviside(T0+deltaT+TfallAC-t,0)*(-eACmax/TfallAC*(t-T0-deltaT)+eACmax)

# plot and labels
axx[0].plot(t, DC_arr, color='black', lw=2, label="DC")
axx[0].plot(t, AC_arr, color='black', lw=1, ls='dashed', label="AC")
axx[0].set_xlabel("time [\$1/\\delta\$]", fontsize=x_font)
axx[0].set_ylabel("field [V/cm]")
axx[0].legend(loc='lower left')
axx[0].grid()

# arrows
a_h = 7
ah2 = 8
arrow(axx[0], 0, TriseAC, a_h, a_h, "\$T_\\text{rise}^\\text{\\,\\AC}\$", textxy=(TriseAC-.25,a_h-.2), ha='left', va='center')
arrow(axx[0], deltaT+TriseAC, deltaT+TfallAC+TriseAC, a_h, a_h, "\$T_\\text{fall}^{\\,\\AC}\$", textxy=(deltaT+TriseAC,a_h), ha='right', va='center')
arrow(axx[0], ah2, ah2, 0, 12, "\$\\epsilon_\\text{max}^\\text{\\AC}\$", ha='center', va='top', textxy=(ah2+2,0))
arrow(axx[0], TriseAC, TriseAC+deltaT, eACmax+2, eACmax+2, "\$\\Delta T\$", ha='center', va='bottom')

###########################################
### 2D plot               #################
###########################################

# get data
data = np.loadtxt("Ptrans2.csv", delimiter=',')

# plot
im = axx[1].imshow(data[::-1,:], cmap='binary', extent=[0,15,0,50], aspect='auto')

# colorbar
cb = plt.colorbar(im, cax=axx[2], orientation='horizontal')
cb.set_label("\$P_\\text{trans}\$", rotation=0)
axx[2].xaxis.set_ticks_position('top')
axx[2].xaxis.set_label_coords(1,2.8)

# labels
axx[1].set_xlabel("\$\\epsilon_\\text{max}^\\text{\\AC}\$ [V/cm]", fontsize=x_font)
axx[1].set_ylabel("\$\\omega\$ [\$\\delta\$]", fontsize=x_font)
axx[1].yaxis.set_label_coords(1.2, .5)

###########################################
### Common things #########################
###########################################

axx[0].xaxis.set_label_coords(.5, -0.16)
axx[1].xaxis.set_label_coords(.5, -0.16)

fig.suptitle("(b) both AC and DC", x=0.35)

#plt.tight_layout()

# save to file
plt.savefig('Ptrans2.svg')#, bbox_inches='tight')
