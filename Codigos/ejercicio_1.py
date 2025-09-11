import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Parámetros
fs = 1000  # Frecuencia de muestreo (Hz)
T = 1.0    # Duración (segundos)
t = np.linspace(0, T, int(fs * T), endpoint=False)

# Frecuencias, amplitudes y fases
f1, A1, phi1 = 50, 1.0, np.pi/2
f2, A2, phi2 = 120, 0.5, np.pi/2
f3, A3, phi3 = 200, 0.3, np.pi/2

# Señal compuesta
signal = (A1 * np.sin(2 * np.pi * f1 * t + phi1) +
          A2 * np.sin(2 * np.pi * f2 * t + phi2) +
          A3 * np.sin(2 * np.pi * f3 * t + phi3))

# Calcular FFT
N = len(signal)
fft_values = fft(signal)
freq = fftfreq(N, 1/fs)
magnitude = 2 * np.abs(fft_values) / N  # Magnitud normalizada

# Frecuencias positivas y magnitudes
positive_freq = freq[:N//2]
positive_mag = magnitude[:N//2]

# Espectro teórico
theoretical_freqs = [f1, f2, f3]
theoretical_amps = [A1, A2, A3]

# Graficar señal compuesta y espectros
fig, axs = plt.subplots(3, 1, figsize=(12, 7))

# Señal compuesta en el tiempo
axs[0].plot(t, signal, color='k')
axs[0].set_title('Señal Compuesta', fontsize=12, pad=12)
axs[0].set_xlabel('Tiempo (s)', fontsize=11, labelpad=8)
axs[0].set_ylabel('Amplitud', fontsize=11)
axs[0].grid(True)

# Espectro FFT
axs[1].stem(positive_freq, positive_mag, linefmt='b-', markerfmt='bo', basefmt='r-')
axs[1].set_title('Espectro de Magnitud (FFT)', fontsize=12, pad=12)
axs[1].set_xlabel('Frecuencia (Hz)', fontsize=11, labelpad=8)
axs[1].set_ylabel('Magnitud', fontsize=11)
axs[1].set_xlim(0, 250)
axs[1].grid(True)

# Espectro Teórico
axs[2].stem(theoretical_freqs, theoretical_amps, linefmt='r-', markerfmt='ro', basefmt='r-')
axs[2].set_title('Espectro Teórico (Ideal)', fontsize=12, pad=12)
axs[2].set_xlabel('Frecuencia (Hz)', fontsize=11, labelpad=8)
axs[2].set_ylabel('Amplitud', fontsize=11)
axs[2].set_xlim(0, 250)
axs[2].grid(True)

#plt.tight_layout(rect=[0, 0, 1, 0.96])  # Más espacio arriba para el título general
plt.subplots_adjust(hspace=1)         # Más espacio entre subplots
plt.show()

###################################################################################
################## Análisis de espectros individuales y su suma ###################
###################################################################################

# Señales individuales
s1 = A1 * np.sin(2 * np.pi * f1 * t + phi1)
s2 = A2 * np.sin(2 * np.pi * f2 * t + phi2)
s3 = A3 * np.sin(2 * np.pi * f3 * t + phi3)

# FFT de cada señal individual
fft_s1 = fft(s1)
fft_s2 = fft(s2)
fft_s3 = fft(s3)

mag_s1 = 2 * np.abs(fft_s1) / N
mag_s2 = 2 * np.abs(fft_s2) / N
mag_s3 = 2 * np.abs(fft_s3) / N

mag_s1_pos = mag_s1[:N//2]
mag_s2_pos = mag_s2[:N//2]
mag_s3_pos = mag_s3[:N//2]

# Suma de los espectros individuales
mag_sum = mag_s1_pos + mag_s2_pos + mag_s3_pos

# Graficar espectros individuales y suma en una cuadrícula 2x2
fig2, axs2 = plt.subplots(2, 2, figsize=(14, 8))
#fig2.suptitle('Espectros individuales y suma de espectros', fontsize=15, y=1.03)

axs2[0, 0].stem(positive_freq, mag_s1_pos, linefmt='b-', markerfmt='bo', basefmt='r-')
axs2[0, 0].set_title('Espectro de señal de 50 Hz', fontsize=12, pad=10)
axs2[0, 0].set_xlabel('Frecuencia (Hz)', fontsize=11)
axs2[0, 0].set_ylabel('Magnitud', fontsize=11)
axs2[0, 0].set_xlim(0, 250)
axs2[0, 0].grid(True)

axs2[0, 1].stem(positive_freq, mag_s2_pos, linefmt='g-', markerfmt='go', basefmt='r-')
axs2[0, 1].set_title('Espectro de señal de 120 Hz', fontsize=12, pad=10)
axs2[0, 1].set_xlabel('Frecuencia (Hz)', fontsize=11)
axs2[0, 1].set_ylabel('Magnitud', fontsize=11)
axs2[0, 1].set_xlim(0, 250)
axs2[0, 1].grid(True)

axs2[1, 0].stem(positive_freq, mag_s3_pos, linefmt='r-', markerfmt='ro', basefmt='r-')
axs2[1, 0].set_title('Espectro de señal de 200 Hz', fontsize=12, pad=10)
axs2[1, 0].set_xlabel('Frecuencia (Hz)', fontsize=11)
axs2[1, 0].set_ylabel('Magnitud', fontsize=11)
axs2[1, 0].set_xlim(0, 250)
axs2[1, 0].grid(True)

axs2[1, 1].stem(positive_freq, mag_sum, linefmt='m-', markerfmt='mo', basefmt='r-')
axs2[1, 1].set_title('Suma de los tres espectros individuales', fontsize=12, pad=10)
axs2[1, 1].set_xlabel('Frecuencia (Hz)', fontsize=11)
axs2[1, 1].set_ylabel('Magnitud', fontsize=11)
axs2[1, 1].set_xlim(0, 250)
axs2[1, 1].grid(True)

#plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()