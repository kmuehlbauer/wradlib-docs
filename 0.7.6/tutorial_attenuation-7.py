import matplotlib.pyplot as plt
import wradlib
filename = "../../examples/data/raa00-dx_10908-0806021655-fbg---bin"
data, attrs = wradlib.io.readDX(filename)
pia_hibo = wradlib.atten.correctAttenuationHB(data, coefficients = dict(a=8.e-5, b=0.731, l=1.0), mode="warn", thrs=59.)
pia_harrison = wradlib.atten.correctAttenuationHB(data, coefficients = dict(a=4.57e-5, b=0.731, l=1.0), mode="warn", thrs=59.)
pia_harrison[pia_harrison>4.8] = 4.8
pia_kraemer = wradlib.atten.correctAttenuationConstrained2(data, a_max=1.67e-4, a_min=2.33e-5, n_a=100, b_max=0.7, b_min=0.65, n_b=6, l=1.,
              constraints=[wradlib.atten.constraint_dBZ], constraint_args=[[59.0]])
pia_mKraemer = wradlib.atten.correctAttenuationConstrained2(data, a_max=1.67e-4, a_min=2.33e-5, n_a=100, b_max=0.7, b_min=0.65, n_b=6, l=1.,
              constraints=[wradlib.atten.constraint_dBZ,wradlib.atten.constraint_pia], constraint_args=[[59.0],[20.0]])

fig = plt.figure(figsize=(10,12))

mybeams = slice(53,56)
labelsize=13

ax = fig.add_subplot(511)
plt.plot(data[53], label="53 deg")
plt.plot(data[54], label="54 deg")
plt.plot(data[55], label="55 deg")
plt.grid()
plt.text(0.99, 0.88, "Reflectivity along beams", horizontalalignment='right', transform = ax.transAxes, fontsize="large")
plt.ylabel("Reflectivity (dBZ)", fontsize="large")
plt.legend(loc="upper left")
ax.tick_params(axis='x', labelsize=labelsize)
ax.tick_params(axis='y', labelsize=labelsize)
plt.xlim(0,128)

ax = fig.add_subplot(512)
plt.plot(pia_hibo[mybeams].T)
plt.grid()
plt.ylim(0,30)
plt.ylabel("PIA (dB)", fontsize="large")
plt.text(0.01, 0.88, "PIA according to Hitschfeld and Bordan", transform = ax.transAxes, fontsize="large")
ax.tick_params(axis='x', labelsize=labelsize)
ax.tick_params(axis='y', labelsize=labelsize)
plt.xlim(0,128)

ax = fig.add_subplot(513)
plt.plot(pia_harrison[mybeams].T)
plt.grid()
plt.ylim(0,30)
plt.ylabel("PIA (dB)", fontsize="large")
plt.text(0.01, 0.88, "PIA according to Harrison", transform = ax.transAxes, fontsize="large")
ax.tick_params(axis='x', labelsize=labelsize)
ax.tick_params(axis='y', labelsize=labelsize)
plt.xlim(0,128)

ax = fig.add_subplot(514)
plt.plot(pia_kraemer[mybeams].T)
plt.grid()
plt.ylim(0,30)
plt.ylabel("PIA (dB)", fontsize="large")
plt.text(0.01, 0.88, "PIA according to Kraemer", transform = ax.transAxes, fontsize="large")
ax.tick_params(axis='x', labelsize=labelsize)
ax.tick_params(axis='y', labelsize=labelsize)
plt.xlim(0,128)

ax = fig.add_subplot(515)
plt.plot(pia_mKraemer[mybeams].T)
plt.grid()
plt.ylim(0,30)
plt.xlabel("range (km)", fontsize="large")
plt.ylabel("PIA (dB)", fontsize="large")
plt.text(0.01, 0.88, "PIA according to modified Kraemer", transform = ax.transAxes, fontsize="large")
ax.tick_params(axis='x', labelsize=labelsize)
ax.tick_params(axis='y', labelsize=labelsize)
plt.xlim(0,128)

plt.show()