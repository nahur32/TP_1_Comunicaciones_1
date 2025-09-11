# Importar librerías necesarias
import numpy as np  # Para operaciones matemáticas y manejo de arrays
import matplotlib.pyplot as plt  # Para crear gráficos y visualizaciones

# =============================================================================
# PARÁMETROS DE CONFIGURACIÓN
# =============================================================================
# Definimos los parámetros básicos de la onda cuadrada que vamos a analizar
A = 1.0      # Amplitud de la onda cuadrada
T = 1.0      # Período de la onda en segundos
f0 = 1/T     # Frecuencia fundamental (inversa del período)

# =============================================================================
# GENERACIÓN DE LA ONDA CUADRADA ORIGINAL
# =============================================================================
# Creamos un vector de tiempo que abarca dos períodos completos
t = np.linspace(0, 2*T, 1000)  # 1000 puntos equidistantes entre 0 y 2T

# Generamos la onda cuadrada usando la función signo aplicada a una senoidal
# np.sign() devuelve -1 para valores negativos, 0 para cero y 1 para positivos
square_wave = A * np.sign(np.sin(2*np.pi*f0*t))

# =============================================================================
# CONFIGURACIÓN DE ARMÓNICOS A ANALIZAR
# =============================================================================
# Definimos diferentes cantidades de armónicos para comparar su efecto
harmonics = [1, 3, 5, 10, 20, 50]  # Solo consideramos números impares

# =============================================================================
# FUNCIÓN PARA CALCULAR COEFICIENTES DE FOURIER
# =============================================================================
def fourier_coefficients(n_max):
    """
    Calcula los coeficientes de Fourier para una onda cuadrada.
    
    Para una onda cuadrada, solo los armónicos impares tienen coeficientes no nulos.
    El coeficiente para el armónico n es 4A/(nπ).
    
    Parámetros:
    n_max: Número máximo de armónicos a considerar
    
    Retorna:
    Lista de tuplas (n, coeficiente) para cada armónico impar
    """
    coefficients = []  # Lista vacía para almacenar los coeficientes
    
    # Iteramos solo sobre los números impares desde 1 hasta n_max
    for n in range(1, n_max+1, 2):
        # Fórmula del coeficiente de Fourier para onda cuadrada
        coeff = 4*A/(n*np.pi)
        # Añadimos el par (número de armónico, coeficiente) a la lista
        coefficients.append((n, coeff))
    
    return coefficients

# =============================================================================
# FUNCIÓN PARA RECONSTRUIR SEÑAL CON SERIE DE FOURIER
# =============================================================================
def reconstruct_signal(t, coefficients):
    """
    Reconstruye una señal sumando las contribuciones de los armónicos de Fourier.
    
    Parámetros:
    t: Vector de tiempo
    coefficients: Lista de coeficientes de Fourier (n, coeficiente)
    
    Retorna:
    Señal reconstruida mediante la suma de los términos de la serie
    """
    # Inicializamos un array de ceros con la misma forma que el vector de tiempo
    signal = np.zeros_like(t)
    
    # Para cada armónico y su coeficiente
    for n, coeff in coefficients:
        # Añadimos la contribución de este armónico: coeficiente * sin(2πn f0 t)
        signal += coeff * np.sin(2*np.pi*n*f0*t)
    
    return signal

# =============================================================================
# FUNCIÓN PARA CALCULAR ERROR CUADRÁTICO MEDIO
# =============================================================================
def calculate_mse(original, reconstructed):
    """
    Calcula el Error Cuadrático Medio (MSE) entre la señal original y la reconstruida.
    
    MSE = promedio de (original - reconstruida)^2
    
    Parámetros:
    original: Señal original
    reconstructed: Señal reconstruida
    
    Retorna:
    Valor del error cuadrático medio
    """
    return np.mean((original - reconstructed)**2)

# =============================================================================
# CÁLCULO DE RECONSTRUCCIONES Y ERRORES
# =============================================================================
# Listas para almacenar los resultados
mse_values = []        # Almacenará los errores cuadráticos medios
reconstructions = []   # Almacenará las señales reconstruidas

# Para cada cantidad de armónicos en nuestra lista
for N in harmonics:
    # 1. Calcular los coeficientes de Fourier para hasta N armónicos
    coeffs = fourier_coefficients(N)
    
    # 2. Reconstruir la señal usando estos coeficientes
    reconstructed = reconstruct_signal(t, coeffs)
    
    # 3. Almacenar la reconstrucción en la lista
    reconstructions.append(reconstructed)
    
    # 4. Calcular el error entre la señal original y la reconstruida
    mse = calculate_mse(square_wave, reconstructed)
    mse_values.append(mse)
    
    # 5. Imprimir el resultado para este número de armónicos
    print(f"N={N} armónicos, MSE={mse:.6f}")

# =============================================================================
# VISUALIZACIÓN DE RESULTADOS
# =============================================================================
# Configuramos colores diferentes para cada reconstrucción
colors = ['r', 'g', 'b', 'c', 'm', 'y']

# GRÁFICO 1: COMPARACIÓN DE RECONSTRUCCIONES
plt.figure(figsize=(12, 8))

# Subgráfico 1: Señal original y reconstrucciones
plt.subplot(2, 1, 1)
# Dibujamos la onda cuadrada original (línea negra continua)
plt.plot(t, square_wave, 'k-', linewidth=2, label='Onda cuadrada original')

# Dibujamos cada reconstrucción con un color diferente
for i, N in enumerate(harmonics):
    plt.plot(t, reconstructions[i], colors[i] + '--', 
             linewidth=1, label=f'{N} armónicos')

# Añadimos etiquetas, título y leyenda
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Reconstrucción de onda cuadrada con Series de Fourier')
plt.legend()
plt.grid(True)

# GRÁFICO 2: ERROR CUADRÁTICO MEDIO VS NÚMERO DE ARMÓNICOS
plt.subplot(2, 1, 2)
# Dibujamos el error como función del número de armónicos
plt.plot(harmonics, mse_values, 'bo-', linewidth=2)
plt.xlabel('Número de armónicos')
plt.ylabel('Error Cuadrático Medio (MSE)')
plt.title('Error de reconstrucción vs Número de armónicos')
plt.grid(True)
plt.yscale('log')  # Usamos escala logarítmica para mejor visualización del error

# Ajustamos el espaciado entre subgráficos y mostramos la figura
plt.tight_layout()
plt.show()

# GRÁFICO 3: ZOOM PARA MOSTRAR EL FENÓMENO DE GIBBS
plt.figure(figsize=(10, 6))
# Seleccionamos un intervalo de tiempo cerca de una discontinuidad (entre 0.4 y 0.6 segundos)
zoom_idx = (t > 0.4) & (t < 0.6)

# Dibujamos la onda original en el intervalo de zoom
plt.plot(t[zoom_idx], square_wave[zoom_idx], 'k-', linewidth=3, 
         label='Onda cuadrada original')

# Dibujamos solo las últimas 3 reconstrucciones (las más precisas) para mayor claridad
for i, N in enumerate(harmonics[-3:]):
    plt.plot(t[zoom_idx], reconstructions[-3+i][zoom_idx], 
             colors[-3+i] + '--', linewidth=2, label=f'{N} armónicos')

# Añadimos etiquetas, título y leyenda
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Fenómeno de Gibbs cerca de una discontinuidad')
plt.legend()
plt.grid(True)

# Mostramos el gráfico
plt.show()

# GRÁFICO EXTRA: ONDA CUADRADA ORIGINAL
plt.figure(figsize=(8, 4))
plt.plot(t, square_wave, 'k-', linewidth=2)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Onda cuadrada original')
plt.grid(True)
plt.show()