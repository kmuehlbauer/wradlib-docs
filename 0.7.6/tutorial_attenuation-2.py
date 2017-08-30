import matplotlib.pyplot as plt
import wradlib
filename = "../../examples/data/raa00-dx_10908-0806021655-fbg---bin"
data, attrs = wradlib.io.readDX(filename)
mybeams = slice(53,56)
labelsize=13
fig = plt.figure(figsize=(10,3))
ax = fig.add_subplot(111)
plt.plot(data[53], label="53 deg")
plt.plot(data[54], label="54 deg")
plt.plot(data[55], label="55 deg")
plt.grid()
plt.text(0.99, 0.88, "Reflectivity along beams", horizontalalignment='right', transform = ax.transAxes, fontsize="large")
plt.xlabel("range (km)", fontsize="large")
plt.ylabel("Reflectivity (dBZ)", fontsize="large")
plt.legend(loc="upper left")
ax.tick_params(axis='x', labelsize=labelsize)
ax.tick_params(axis='y', labelsize=labelsize)
plt.xlim(0,128)
plt.show()