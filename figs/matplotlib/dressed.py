import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams['font.size'] = 15

def evals(eAC_v, delta_v=1, omega_v=5, alpha_v=0.01, beta_v=0.1):
    # parameters
    eDC = np.linspace(-50-eAC_v,50+eAC_v,200)
    delta = eDC*0 + delta_v
    omega = eDC*0 + omega_v
    alpha = eDC*0 + alpha_v
    eAC   = eDC*0 + eAC_v
    beta  = eDC*0 + beta_v

    # define the Hamiltonian
    H11 = np.swapaxes([
        [delta-omega-alpha*eAC**2/2-alpha*eDC**2,beta,-alpha*eAC*eDC,0*eDC,-alpha*eAC**2/4,0*eDC],
        [beta,-omega,0*eDC,0*eDC,0*eDC,0*eDC],
        [-alpha*eAC*eDC,0*eDC,delta-alpha*eAC**2/2-alpha*eDC**2,beta,-alpha*eAC*eDC,0*eDC],
        [0*eDC,0*eDC,beta,0*eDC,0*eDC,0*eDC],
        [-alpha*eAC**2/4,0*eDC,-alpha*eAC*eDC,0*eDC,delta+omega-alpha*eAC**2/2-alpha*eDC**2,beta],
        [0*eDC,0*eDC,0*eDC,0*eDC,beta,omega],
    ],0,2)

    # calculate eigencalues
    return eDC, np.linalg.eigvalsh(H11)

fig = plt.figure(figsize=(10,3))
gs1 = GridSpec(1, 4, wspace=0.10, hspace=0.3)
axx = [fig.add_subplot(gs1[0, i]) for i in range(4)]

axx[0].set_ylabel("\$E\$ [\$1/\\delta\$]")
for i in range(len(axx)):
    axx[i].set_xlabel("\$\\epsilon_\\text{\\DC}\$")
    
for i in range(len(axx)-1):
    axx[i+1].get_shared_y_axes().join(axx[i], axx[i+1])
    axx[i+1].set_yticklabels([])

for i,eAC in enumerate([0, 20, 30, 50]):
    eDC, evals_arr = evals(eAC)
    for j in range(evals_arr.shape[1]):
        axx[i].plot(eDC, evals_arr[:,j], color='black')
    axx[i].set_ylim((-6-eAC/2,7));
    axx[i].set_title("\$\\epsilon_\\text{\\AC} = " + str(eAC) + "\$")
    axx[i].grid()

# save to file
plt.savefig('dressed.svg', bbox_inches='tight')
