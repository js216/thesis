import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams['axes.titlepad'] = 10
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['legend.borderpad'] = 1
matplotlib.rcParams['legend.borderaxespad'] = .5
matplotlib.rcParams['legend.labelspacing'] = 2

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
        fontsize   = 12.0,
        textcoords = 'data',
        ha         = 'center' if not ha else ha,
        va         = "bottom" if not va else va
    )

# subplots
fig = plt.figure(figsize=(5,3))
gs1 = GridSpec(2, 2, wspace=0.05, hspace=0.02, width_ratios=[1,1.25])
axx = [fig.add_subplot(gs1[0, 0]),
       fig.add_subplot(gs1[1, 0]),
       fig.add_subplot(gs1[:, 1])]

axx[0].get_shared_x_axes().join(axx[0], axx[1])
axx[0].set_xticklabels([])

y_bot = -.4
axx[1].xaxis.set_label_coords(.5, y_bot)
axx[2].xaxis.set_label_coords(.5, y_bot/2)

###########################################
### Fields vs time ########################
###########################################

# parameters
T0 = 3
eDCi, eDCf = 20, -20
TfallDC = 9
t = np.linspace(0,15,200)

# fields
DC_arr = eDCi*np.heaviside(T0-t,0) + \
           np.heaviside(t-T0,0)*np.heaviside(T0+TfallDC-t,0)*(((eDCf-eDCi)/(TfallDC))*(t-T0)+eDCi) + \
           eDCf*np.heaviside(t-T0-TfallDC,0)

# plot and labels
axx[0].plot(t, DC_arr, color='black', lw=2)
# axx[0].set_xlabel("time [\$1/\\delta\$]")
axx[0].set_ylabel("field [V/cm]")
# axx[0].set_title("Fields")

# arrows
arrow(axx[0], 0, T0, 17, 17, "\$T_0\$", va='top', textxy=(T0/2,14))
arrow(axx[0], T0, T0+TfallDC, 0, 0, "\$T_\\text{fall}^\\text{\,\\DC}\$", ha='left', va='bottom', textxy=((T0+TfallDC)/2+1,2))
hp = 13
arrow(axx[0], hp, hp,  20, 0, "\$\\epsilon_{i}^\\text{\\DC}\$", ha='left', va='center', textxy=(hp+.15,10))
arrow(axx[0], hp, hp, -20, 0, "\$\\epsilon_{f}^\\text{\\DC}\$", ha='left', va='center', textxy=(hp+.15,-10))

###########################################
### Eigenenergies vs time #################
###########################################

# eigenstates
alpha, beta, delta = 0.01, 0.1, 1
Ep_arr = .5*(delta-alpha*DC_arr**2+np.sqrt(4*beta**2+delta**2-2*alpha*delta*DC_arr**2+alpha**2*DC_arr**4))
Em_arr = .5*(delta-alpha*DC_arr**2-np.sqrt(4*beta**2+delta**2-2*alpha*delta*DC_arr**2+alpha**2*DC_arr**4))

# plot
axx[1].plot(t, Ep_arr, color='black', lw=1)
axx[1].plot(t, Em_arr, color='black', lw=1)
# axx[1].set_xlim((T0-.2,T0+TfallDC+.2))

# labels
axx[1].set_ylabel("energies [\$\\delta\$]")
axx[1].set_xlabel("time [\$1/\\delta\$]")
# axx[1].set_title("Eigenenergies")

###########################################
### Transition probability ################
###########################################

data = np.loadtxt("Ptrans1.csv", delimiter=',')
axx[2].plot(np.linspace(0.001,600,len(data)), data, color='black', lw=.7)

# labels
axx[2].set_xlabel("\$T_\\text{fall}^\\text{\,\\DC}\$ [\$1/\\delta\$]")
axx[2].set_ylabel("transition probability [\\%]")
axx[2].yaxis.tick_right()
axx[2].yaxis.set_label_coords(1.35,.5)

###########################################
### Common things #########################
###########################################

fig.suptitle("(a) DC only", y=1.00)

for i in range(3):
    axx[i].grid()

plt.tight_layout()

# save to file
plt.savefig('Ptrans1.svg', bbox_inches='tight')
