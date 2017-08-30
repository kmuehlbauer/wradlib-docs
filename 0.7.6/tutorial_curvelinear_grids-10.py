import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
# well, it's a wradlib example
import wradlib
from mpl_toolkits.axisartist.grid_finder import FixedLocator, DictFormatter
# reading in data, range and theta arrays from special rhi hdf5 file
file = '../../examples/data/polar_rhi_dBZ_bonn.h5'
data, meta = wradlib.io.from_hdf5(file, dataset='data')
r, meta = wradlib.io.from_hdf5(file, dataset='range')
th, meta = wradlib.io.from_hdf5(file, dataset='theta')
# mask data array for better presentation
mask_ind = np.where(data <= np.nanmin(data))
data[mask_ind] = np.nan
ma = np.ma.array(data, mask=np.isnan(data))
gs = gridspec.GridSpec(3, 3)
subplots = [gs[0, :], gs[1, :-1], gs[1:, -1], gs[-1, 0], gs[-1, -2]]
cbarpad = [0.05, 0.075, 0.2, 0.2, 0.2]
labelpad = [1.25, 1.25, 1.1, 1.25, 1.25]
for i, sp in enumerate(subplots):
    cgax, caax, paax, pm = wradlib.vis.plot_cg_rhi(ma,
                                                   r, th, rf=1e3, autoext=True,
                                                   refrac=False, subplot=sp)
    t = plt.title('CG RHI #%(i)d' %locals())
    t.set_y(labelpad[i])
    cgax.set_ylim(0, 15)
    cbar = plt.gcf().colorbar(pm, pad=cbarpad[i])
    caax.set_xlabel('range [km]')
    caax.set_ylabel('height [km]')
    gh = cgax.get_grid_helper()
    # set theta to some nice values
    locs = [0., 5., 10., 15., 20., 30., 40., 60., 90.]
    gh.grid_finder.grid_locator1 = FixedLocator(locs)
    gh.grid_finder.tick_formatter1 = DictFormatter(dict([(i, r"${0:.0f}^\circ$".format(i)) for i in locs]))
    cbar.set_label('reflectivity [dBZ]')
plt.tight_layout()
plt.draw()
plt.show()