import matplotlib.pyplot as plt
import numpy as np
# well, it's a wradlib example
import wradlib
from mpl_toolkits.axisartist.grid_finder import FixedLocator
# reading in data, range and theta arrays from special rhi hdf5 file
file = '../../examples/data/polar_rhi_dBZ_bonn.h5'
data, meta = wradlib.io.from_hdf5(file, dataset='data')
r, meta = wradlib.io.from_hdf5(file, dataset='range')
th, meta = wradlib.io.from_hdf5(file, dataset='theta')
# mask data array for better presentation
mask_ind = np.where(data <= np.nanmin(data))
data[mask_ind] = np.nan
ma = np.ma.array(data, mask=np.isnan(data))
subplots = [221, 222, 223, 224]
for sp in subplots:
    cgax, caax, paax, pm = wradlib.vis.plot_cg_rhi(ma,
                                                   r, th, rf=1e3, autoext=True,
                                                   refrac=False, subplot=sp)
    t = plt.title('CG RHI #%(sp)d' %locals())
    t.set_y(1.1)
    cgax.set_ylim(0, 15)
    cbar = plt.gcf().colorbar(pm, pad=0.125)
    caax.set_xlabel('range [km]')
    caax.set_ylabel('height [km]')
    gh = cgax.get_grid_helper()
    # set theta to some nice values
    gh.grid_finder.grid_locator1 = FixedLocator([0, 5, 10, 15, 20, 30, 40, 60, 90,])
    cbar.set_label('reflectivity [dBZ]')
plt.tight_layout()
plt.draw()
plt.show()