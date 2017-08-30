import wradlib as wrl
import numpy as np
import matplotlib.pyplot as pl
# load radolan files
rw_filename = '../../examples/data/radolan/raa01-rw_10000-1408102050-dwd---bin.gz'
rwdata, rwattrs = wrl.io.read_RADOLAN_composite(rw_filename)
# print the available attributes
print("RW Attributes:", rwattrs)
# do some masking
sec = rwattrs['secondary']
rwdata.flat[sec] = -9999
rwdata = np.ma.masked_equal(rwdata, -9999)
# Get coordinates
radolan_grid_xy = wrl.georef.get_radolan_grid(900,900)
x = radolan_grid_xy[:,:,0]
y = radolan_grid_xy[:,:,1]
pl.pcolormesh(x, y, rwdata, cmap="spectral")
# add colorbar and title
cb = pl.colorbar(shrink=0.75)
cb.set_label("mm/h")
pl.title('RADOLAN RW Product Polar Stereo \n' + rwattrs['datetime'].isoformat())
pl.grid(color='r')