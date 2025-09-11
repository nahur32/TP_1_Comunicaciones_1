import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def hilbert_transform_fft(x):
    """
    Calcula la Transformada de Hilbert usando FFT
    """
    N = len(x)
    X = np.fft.fft(x)
    
    # Crear el filtro de Hilbert: -j * sign(f)
    frequencies = np.fft.fftfreq(N)
    hilbert_filter = -1j * np.sign(frequencies)
    
    # Aplicar el filtro en el dominio de la frecuencia
    X_hat = X * hilbert_filter
    
    # Transformada inversa para obtener la señal en tiempo
    x_hat = np.fft.ifft(X_hat)
    
    return np.real(x_hat)

def señal_analítica(x):
    """
    Calcula la señal analítica: x(t) + j * Hilbert(x(t))
    """
    x_hat = hilbert_transform_fft(x)
    return x + 1j * x_hat

def envolvente_compleja(x_analitica):
    """
    Calcula la envolvente compleja (valor absoluto de la señal analítica)
    """
    return np.abs(x_analitica)

# Parámetros de las señales de prueba
fs = 1000  # Frecuencia de muestreo
t = np.linspace(0, 1, fs, endpoint=False)

# 3.2a) Señal sinusoidal pura
f_sin = 10  # Hz
senal_sin = np.sin(2 * np.pi * f_sin * t)
# ---
# Análisis:
# La señal original es una onda sinusoidal suave y periódica.
# La Transformada de Hilbert debería ser una onda cosenoidal desplazada 90°.
# La envolvente compleja es constante, indicando amplitud constante.
# ---

# 3.2b) Pulso rectangular único
pulso_rect = np.zeros_like(t)
pulso_rect[400:600] = 1  # Pulso de 200 ms
# ---
# Análisis:
# El pulso tiene bordes abruptos, por lo que la Transformada de Hilbert muestra picos en los bordes.
# La envolvente compleja tiene máximos en las transiciones, mostrando concentración de energía.
# ---

# 3.2c) Producto de los casos anteriores
senal_producto = senal_sin * pulso_rect
# ---
# Análisis:
# La señal es sinusoidal solo durante el pulso.
# La Transformada de Hilbert muestra distorsiones en los bordes por la ventana.
# La envolvente compleja varía y se concentra donde existe el pulso.
# ---

# Lista de señales para analizar
senales = [senal_sin, pulso_rect, senal_producto]
nombres = ['Señal Sinusoidal', 'Pulso Rectangular', 'Producto Seno × Pulso']

# Análisis para cada señal
for i, (x, nombre) in enumerate(zip(senales, nombres)):
    print(f"\nAnalizando: {nombre}")
    
    # Calcular Transformada de Hilbert
    x_hat = hilbert_transform_fft(x)
    
    # Calcular señal analítica
    x_analitica = señal_analítica(x)
    
    # Calcular envolvente compleja
    envolvente = envolvente_compleja(x_analitica)
    
    # 3.3) Graficar resultados
    plt.figure(figsize=(15, 8))
    
    # Señal original
    plt.subplot(3, 1, 1)
    plt.plot(t, x, 'b-', linewidth=2, label='Señal original')
    plt.title(f'{nombre} - Señal Original')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    # ---
    # Interpretación:
    # Muestra la forma de la señal en el tiempo.
    # ---
    
    # Transformada de Hilbert
    plt.subplot(3, 1, 2)
    plt.plot(t, x_hat, 'r-', linewidth=2, label='Transformada de Hilbert')
    plt.title('Transformada de Hilbert')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    # ---
    # Interpretación:
    # Permite observar el desfase y los efectos de los bordes en cada señal.
    # ---
    
    # Señal analítica y envolvente
    plt.subplot(3, 1, 3)
    plt.plot(t, np.real(x_analitica), 'b-', linewidth=1, label='Parte real')
    plt.plot(t, np.imag(x_analitica), 'g-', linewidth=1, label='Parte imaginaria')
    plt.plot(t, envolvente, 'k--', linewidth=2, label='Envolvente compleja')
    plt.title('Señal Analítica y Envolvente Compleja')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    # ---
    # Interpretación:
    # La parte real es la señal original, la imaginaria es la transformada de Hilbert.
    # La envolvente muestra la amplitud instantánea de la señal.
    # ---
    
    plt.tight_layout()
    plt.show()
    
    # Análisis adicional para la señal sinusoidal
    if i == 0:
        print("\nAnálisis para señal sinusoidal:")
        print(f"La Transformada de Hilbert de sin(2πft) debería ser -cos(2πft)")
        print(f"Error RMS: {np.sqrt(np.mean((x_hat + np.cos(2*np.pi*f_sin*t))**2)):.6f}")
        # ---
        # Interpretación:
        # El error RMS indica qué tan precisa es la implementación respecto al resultado teórico.
        # ---

