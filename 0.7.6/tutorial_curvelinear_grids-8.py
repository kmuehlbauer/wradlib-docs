import matplotlib.pyplot as plt
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
#----------------------------------------------------------------
# the simplest call, plot cg rhi in new window
cgax, caax, paax, pm = wradlib.vis.plot_cg_rhi(ma, r=r, th=th, rf=1e3, refrac=False,
                                           subplot=111)
t = plt.title('Decorated CG RHI')
t.set_y(1.05)
cgax.set_ylim(0,12)
cbar = plt.gcf().colorbar(pm, pad=0.05)
cbar.set_label('reflectivity [dBZ]')
caax.set_xlabel('x_range [km]')
caax.set_ylabel('y_range [km]')
plt.text(1.0, 1.05, 'azimuth', transform=caax.transAxes, va='bottom',
    ha='right')
gh = cgax.get_grid_helper()
# set theta to some nice values
#gh.grid_finder.grid_locator1 = FixedLocator([i for i in np.arange(0, 359, 5)])
locs = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14.,
                15., 16., 17., 18., 20., 22., 25., 30., 35.,  40., 50., 60., 70., 80., 90.]
gh.grid_finder.grid_locator1 = FixedLocator(locs)
gh.grid_finder.tick_formatter1 = DictFormatter(dict([(i, r"${0:.0f}^\circ$".format(i)) for i in locs]))
plt.tight_layout()
plt.plot()
plt.show()