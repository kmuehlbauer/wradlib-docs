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
wradlib.vis.plot_cg_ppi(ma, refrac=False)
t = plt.title('Simple CG PPI')
t.set_y(1.05)
plt.tight_layout()
plt.draw()
plt.show()