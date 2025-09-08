import numpy as np
import matplotlib.pyplot as plt

# Configuración
plt.figure(figsize=(8, 8))
ax = plt.subplot(111)

# Fasores
fasor1 = {'amp': 5, 'fase': np.pi/4, 'color': 'red', 'label': '5∠π/4'}
fasor2 = {'amp': 3, 'fase': -2*np.pi/3, 'color': 'blue', 'label': '3∠-2π/3'}

# Convertir a coordenadas cartesianas
def polar_a_cartesiano(amp, fase):
    x = amp * np.cos(fase)
    y = amp * np.sin(fase)
    return x, y

# Dibujar ejes
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

# Dibujar fasores
for fasor in [fasor1, fasor2]:
    x, y = polar_a_cartesiano(fasor['amp'], fasor['fase'])
    
    # Dibujar flecha
    ax.quiver(0, 0, x, y, color=fasor['color'], width=0.005, 
              scale=1, angles='xy', scale_units='xy')
    
    # Etiqueta con magnitud y ángulo
    angulo_grados = np.degrees(fasor['fase'])
    ax.text(x*1.1, y*1.1, f'{fasor["amp"]}∠{angulo_grados:.1f}°', 
            color=fasor['color'], fontsize=12, ha='center', va='center')

# Configurar ejes
ax.set_xlabel('Eje Real', fontsize=12)
ax.set_ylabel('Eje Imaginario', fontsize=12)
ax.set_title('Diagrama Fasorial', fontsize=14, pad=20)
ax.grid(True, alpha=0.5)
ax.set_aspect('equal')

# Cuadrícula circular
circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--', alpha=0.3)
ax.add_patch(circle)
circle = plt.Circle((0, 0), 3, fill=False, color='gray', linestyle='--', alpha=0.3)
ax.add_patch(circle)
circle = plt.Circle((0, 0), 5, fill=False, color='gray', linestyle='--', alpha=0.3)
ax.add_patch(circle)

plt.tight_layout()
plt.show()