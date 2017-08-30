import matplotlib.pyplot as plt
import wradlib
filename = "../../examples/data/raa00-dx_10908-0806021655-fbg---bin"
data, attrs = wradlib.io.readDX(filename)
ax, cf = wradlib.vis.plot_ppi(data, cmap="spectral")
plt.xlabel("Easting from radar (km)")
plt.ylabel("Northing from radar (km)")
plt.title("Radar Feldberg, 2008-06-02 16:55 UTC")
cb = plt.colorbar(cf, shrink=0.8)
cb.set_label("dBZ")
plt.plot([0,105.6],[0,73.4],"-", color="white", lw=2)
plt.xlim(-128,128)
plt.ylim(-128,128)
plt.grid(color="grey")

plt.show()