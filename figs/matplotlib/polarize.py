import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Circle

matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams.update({'font.size': 2})

# numerical parameters
eta = 0.5
lvl = 0.015
scale = 6
N = 1/25
xlim, ylim = 9,15
aspect = 2
ds = 10

# generate data
y, x = np.mgrid[slice(-xlim,xlim+N,N), slice(-ylim,ylim+N,N)]
r = np.sqrt((x/aspect)**2 + y**2)
cos = y / r
psi_s = (1/np.sqrt(4*np.pi)) * 2 * np.exp(-r)
psi_p = (np.sqrt(6/(8*np.pi)) * cos * r * np.exp(-r/2) / (np.sqrt(3) * 2**(3/2)))
psi = (psi_s+eta*psi_p) / (1+eta**2)

# setup axes
fig = plt.figure(figsize=(2,1))
gs = gridspec.GridSpec(1, 3, wspace=0.01)
lw=.7
ypos=12
al=1
axx = []
for i in range(3):
    axx.append(plt.subplot(gs[i]))
    axx[i].set_aspect(aspect)
    axx[i].axis('off')

# limiting shaded area within contour
cutoff = 0.016
psi1 = scale*psi_s
psi1[psi_s < cutoff] = np.nan
psi2 = scale*psi_p
psi2[np.abs(psi_p) < cutoff] = np.nan
psi3 = scale*psi
psi3[np.abs(psi) < cutoff] = np.nan

axx[0].pcolormesh(x, y, psi1, alpha=al, cmap='seismic', vmin=-1, vmax=1, linewidth=0, antialiased=True, rasterized=True)
axx[0].contour(x, y, psi_s, levels=[-1,-lvl,lvl,1], colors="black", linewidths=lw)
axx[0].text(0,ypos-6,"\$\ket{\\text{s}}\$", fontdict={'ha':'center'})
axx[0].scatter(0, 0, s=ds, c='black', marker='.')

axx[1].pcolormesh(x, y, psi2, alpha=al, cmap='seismic', vmin=-1, vmax=1, rasterized=True, antialiased=True)
axx[1].contour(x, y, psi_p, levels=[-1,-lvl,lvl,1], colors="black", linewidths=lw)
axx[1].text(0,ypos-2,"\$\ket{\\text{p}}\$", fontdict={'ha':'center'})
axx[1].text(0,-13,"(b)", fontdict={'ha':'center'})
axx[1].scatter(0, 0, s=ds, c='black', marker='.')

axx[2].pcolormesh(x+.0, y, psi3, alpha=al, cmap='seismic', vmin=-1, vmax=1, rasterized=True)
axx[2].contour(x, y, psi, levels=[-1,-lvl,lvl], colors="black", linewidths=lw)
axx[2].text(0,ypos-4,"\$\ket{\\text{s}}+\eta\ket{\\text{p}}\$", fontdict={'ha':'center'})
axx[2].scatter(0, 0, s=ds, c='black', marker='.')

# save to file
plt.savefig('polarize.svg', bbox_inches='tight', dpi=600)
