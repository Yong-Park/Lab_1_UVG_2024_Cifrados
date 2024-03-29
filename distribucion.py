from prettytable import PrettyTable

lista = {'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01,
         'h': 0.70, 'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15,
         'n': 6.71, 'ñ': 0.31, 'o': 8.68, 'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98,
         't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.01, 'x': 0.22, 'y': 0.90, 'z': 0.52}

def calcular_distribucion(palabra):
    palabra = palabra.lower()
    conteo_letras = {}
    total_letras = 0

    for letra in palabra:
        if letra.isalpha():
            total_letras += 1
            if letra in conteo_letras:
                conteo_letras[letra] += 1
            else:
                conteo_letras[letra] = 1

    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    for letra in alfabeto:
        if letra not in conteo_letras:
            conteo_letras[letra] = 0

    distribucion_letras = {}
    for letra in sorted(conteo_letras):
        cantidad = conteo_letras[letra]
        porcentaje = (cantidad / total_letras) * 100 if total_letras > 0 else 0
        distribucion_letras[letra] = porcentaje

    return distribucion_letras

print("Ingrese la palabra: ")
word = input()
distribucion_calculada = calcular_distribucion(word)

# Crear tabla para la distribución calculada
tabla_calculada = PrettyTable()
tabla_calculada.field_names = ["Letra", "Distribución Calculada"]

# Ordenar por la distribución calculada de mayor a menor
for letra in sorted(distribucion_calculada, key=distribucion_calculada.get, reverse=True):
    porcentaje_calculado = distribucion_calculada[letra]
    tabla_calculada.add_row([letra, f"{porcentaje_calculado:.2f}%"])

# Crear tabla para la distribución de la lista
tabla_lista = PrettyTable()
tabla_lista.field_names = ["Letra", "Distribución Lista"]

# Ordenar por la distribución de la lista de mayor a menor
for letra in sorted(lista, key=lista.get, reverse=True):
    porcentaje_lista = lista[letra]
    tabla_lista.add_row([letra, f"{porcentaje_lista:.2f}%"])

# Imprimir las tablas
print("Distribución Calculada:")
print(tabla_calculada)

print("\nDistribución Lista:")
print(tabla_lista)
