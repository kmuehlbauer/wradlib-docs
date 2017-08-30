import matplotlib.pyplot as plt
import numpy as np
import wradlib
# load a polar scan and create range and azimuth arrays accordingly
data = np.loadtxt('../../examples/data/polar_dBZ_tur.gz')
r = np.arange(0, data.shape[1])
az = np.arange(0, data.shape[0])
# mask data array for better presentation
mask_ind = np.where(data <= np.nanmin(data))
data[mask_ind] = np.nan
ma = np.ma.array(data, mask=np.isnan(data))
cgax, caax, paax, pm = wradlib.vis.plot_cg_ppi(ma, r, az, autoext=True,
                                           refrac=False)
t = plt.title('Decorated CG PPI')
t.set_y(1.05)
cbar = plt.gcf().colorbar(pm, pad=0.075)
caax.set_xlabel('x_range [km]')
caax.set_ylabel('y_range [km]')
plt.text(1.0, 1.05, 'azimuth', transform=caax.transAxes, va='bottom',
    ha='right')
cbar.set_label('reflectivity [dBZ]')
plt.tight_layout()
plt.draw()
plt.show()