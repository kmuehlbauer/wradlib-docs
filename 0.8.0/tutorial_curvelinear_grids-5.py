import matplotlib.pyplot as plt
import numpy as np
import wradlib
from mpl_toolkits.axisartist.grid_finder import FixedLocator, DictFormatter
import mpl_toolkits.axisartist.angle_helper as angle_helper
# load a polar scan and create range and azimuth arrays accordingly
data = np.loadtxt('../../examples/data/polar_dBZ_tur.gz')
r = np.arange(0, data.shape[1])
az = np.arange(0, data.shape[0])
# mask data array for better presentation
mask_ind = np.where(data <= np.nanmin(data))
data[mask_ind] = np.nan
ma = np.ma.array(data, mask=np.isnan(data))
cgax, caax, paax, pm = wradlib.vis.plot_cg_ppi(ma[200:250, 40:80],
                                           r[40:81], az[200:251],
                                           autoext=False,
                                           refrac=False)
t = plt.title('Decorated Sector CG PPI')
t.set_y(1.05)
cbar = plt.gcf().colorbar(pm, pad=0.075)
caax.set_xlabel('x_range [km]')
caax.set_ylabel('y_range [km]')
plt.text(1.0, 1.05, 'azimuth', transform=caax.transAxes, va='bottom',
    ha='right')
cbar.set_label('reflectivity [dBZ]')
gh = cgax.get_grid_helper()
# set azimuth resolution to 15deg
locs = [i for i in np.arange(0., 359., 5.)]
gh.grid_finder.grid_locator1 = FixedLocator(locs)
gh.grid_finder.tick_formatter1 = DictFormatter(dict([(i, r"${0:.0f}^\circ$".format(i)) for i in locs]))
gh.grid_finder.grid_locator2._nbins = 30
gh.grid_finder.grid_locator2._steps = [1, 1.5, 2, 2.5, 5, 10]
cgax.axis["lat"] = cgax.new_floating_axis(0, 240)
cgax.axis["lat"].set_ticklabel_direction('-')
cgax.axis["lat"].label.set_text("range [km]")
cgax.axis["lat"].label.set_rotation(180)
cgax.axis["lat"].label.set_pad(10)
plt.tight_layout()
plt.draw()
plt.show()