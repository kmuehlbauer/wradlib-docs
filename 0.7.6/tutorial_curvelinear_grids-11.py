import numpy as np
import matplotlib.pyplot as plt
import wradlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import NullFormatter, FuncFormatter, MaxNLocator

def mip_formatter(x, pos):
    x = x / 1000.
    fmt_str = '{:g}'.format(x)
    if np.abs(x) > 0 and np.abs(x) < 1:
        return fmt_str.replace("0", "", 1)
    else:
        return fmt_str

# angle of *cut* through ppi and scan elev.
angle = 0.0
elev = 0.0

data = np.loadtxt('../../examples/data/polar_dBZ_tur.gz')
# we need to have meter here for the georef function inside mip
d1 = np.arange(data.shape[1], dtype=np.float) * 1000
d2 = np.arange(data.shape[0], dtype=np.float)
data = np.roll(data, (d2 >= angle).nonzero()[0][0], axis=0)

# calculate max intensity proj
xs, ys, mip1 = wradlib.util.maximum_intensity_projection(data, r=d1, az=d2, angle=angle, elev=elev)
xs, ys, mip2 = wradlib.util.maximum_intensity_projection(data, r=d1, az=d2, angle=90+angle, elev=elev)

# normal cg plot
cgax, caax, paax, pm = wradlib.vis.plot_cg_ppi(data, r=d1, az=d2, refrac=True)
cgax.set_xlim(-np.max(d1),np.max(d1))
cgax.set_ylim(-np.max(d1),np.max(d1))
caax.xaxis.set_major_formatter(FuncFormatter(mip_formatter))
caax.yaxis.set_major_formatter(FuncFormatter(mip_formatter))
caax.set_xlabel('x_range [km]')
caax.set_ylabel('y_range [km]')

# axes divider section
divider = make_axes_locatable(cgax)
axMipX = divider.append_axes("top", size=1.2, pad=0.1, sharex=cgax)
axMipY = divider.append_axes("right", size=1.2, pad=0.1, sharey=cgax)

# special handling for labels etc.
cgax.axis["right"].major_ticklabels.set_visible(False)
cgax.axis["top"].major_ticklabels.set_visible(False)
axMipX.xaxis.set_major_formatter(NullFormatter())
axMipX.yaxis.set_major_formatter(FuncFormatter(mip_formatter))
axMipX.yaxis.set_major_locator(MaxNLocator(5))
axMipY.yaxis.set_major_formatter(NullFormatter())
axMipY.xaxis.set_major_formatter(FuncFormatter(mip_formatter))
axMipY.xaxis.set_major_locator(MaxNLocator(5))

# plot max intensity proj
ma = np.ma.array(mip1, mask=np.isnan(mip1))
axMipX.pcolormesh(xs, ys, ma)
ma = np.ma.array(mip2, mask=np.isnan(mip2))
axMipY.pcolormesh(ys.T, xs.T, ma.T)

# set labels, limits etc
axMipX.set_xlim(-np.max(d1),np.max(d1))
axMipX.set_ylim(0, wradlib.georef.beam_height_n(d1[-2], elev))
axMipY.set_xlim(0, wradlib.georef.beam_height_n(d1[-2], elev))
axMipY.set_ylim(-np.max(d1),np.max(d1))
axMipX.set_ylabel('height [km]')
axMipY.set_xlabel('height [km]')
axMipX.grid(True)
axMipY.grid(True)
t = plt.gcf().suptitle('AxesDivider CG-MIP Example')

plt.draw()
plt.show()