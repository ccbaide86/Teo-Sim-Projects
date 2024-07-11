# Lanzamiento de Dados: Numeros Aleatoreos con Python 

import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2, dado1 + dado2

def contar_suma_11(num_lanzamientos):
    conteo = 0
    for _ in range(num_lanzamientos):
        resultado = lanzar_dados()
        if resultado[2] == 11:
            conteo += 1
    return conteo

num_lanzamientos = 1000
resultado = contar_suma_11(num_lanzamientos)
print(f"Después de lanzar los dados {num_lanzamientos} veces, la cantidad de veces que la suma de los dados da 11 es: {resultado}")
