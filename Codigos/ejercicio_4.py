import numpy as np
from collections import Counter
from scipy.stats import entropy

# -------------------------
# a) Texto en español
# -------------------------
print("------------------------- \n Texto en español \n-------------------------")

texto = "El rapido zorro marron salta sobre el perro perezoso"
texto = texto.lower()
print("\n",texto)
conteo = Counter(texto)
total = sum(conteo.values())
probs = np.array([c/total for c in conteo.values()]) #
H = entropy(probs, base=2)
print(f"\nEntropía texto en español: {H:.4f} bits/caracter")



# -------------------------
# b) Texto en ingles
# -------------------------
print("\n-------------------------\n Texto en ingles \n-------------------------")

texto_en = "The quick brown fox jumps over the lazy dog"
texto_en = texto_en.lower()
print("\n",texto_en)

conteo_en = Counter(texto_en)
total_en = sum(conteo_en.values())
probs_en = np.array([c/total_en for c in conteo_en.values()])
H_en = entropy(probs_en, base=2)
print(f"\nEntropía texto en inglés: {H_en:.4f} bits/caracter")

# -------------------------
# c) Proceso aleatorio discreto simple
# Ejemplo: dado de 6 caras
# -------------------------
print("\n-------------------------\n Dado 6 caras \n-------------------------")

caras = [1,2,3,4,5,6]
prob_dado = np.array([1/6]*6)  # dado justo
H_dado = entropy(prob_dado, base=2)
print(f"\nEntropía dado 6 caras: {H_dado:.4f} bits/tiro")

print("\n-------------------------\n Dado 20 caras \n-------------------------")

# Ejemplo: dado de 20 caras
prob_d20 = np.array([1/20]*20)
H_d20 = entropy(prob_d20, base=2)
print(f"Entropía dado 20 caras: {H_d20:.4f} bits/tiro")

# -------------------------
# d) Sismógrafo
# Evento: sismo >= 4  "sismo", otro caso "no sismo"
# Supongamos 30 segundos al año
# -------------------------

print("\n-------------------------\n Sismografo \n-------------------------")

p_sismo = 150/31536000  # por ejemplo, 5 eventos mayores a 4 por año de 30seg
p_no_sismo = 1 - p_sismo
probs_sismo = np.array([p_sismo, p_no_sismo])
H_sismo = entropy(probs_sismo, base=2)
print(f"\nEntropía evento sismo: {H_sismo:.8f} bits/evento")

print(f"\nProbabilidad de sismo por segundo: {p_sismo:.8f}") 
print(f"Probabilidad de no sismo por segundo: {p_no_sismo:.8f}")