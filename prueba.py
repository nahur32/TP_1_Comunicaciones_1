import numpy as np
import matplotlib.pyplot as plt

# Fasores en plano complejo
fig, ax = plt.subplots()
ax.quiver(0, 0, 5*np.cos(np.pi/4), 5*np.sin(np.pi/4), angles='xy', scale_units='xy', scale=1, color='r', label='1000 Hz: 5 ∠ 45°')
ax.quiver(0, 0, 3*np.cos(-2*np.pi/3), 3*np.sin(-2*np.pi/3), angles='xy', scale_units='xy', scale=1, color='b', label='1500 Hz: 3 ∠ -120°')
ax.set_xlim(-4, 6)
ax.set_ylim(-4, 6)
ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginario')
ax.legend()
plt.title('Diagrama Fasorial')
plt.grid()
plt.show()