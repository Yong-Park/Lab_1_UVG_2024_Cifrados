from prettytable import PrettyTable

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
list_abcedario = list(alfabeto)
lista = {'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01,
         'h': 0.70, 'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15,
         'n': 6.71, 'ñ': 0.31, 'o': 8.68, 'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98,
         't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.01, 'x': 0.22, 'y': 0.90, 'z': 0.52}

def caesar_desencrtypt(word, desplazamiento):
    encripted = []
    word = list(word.lower())
    for x in word:
        if x in list_abcedario:
            indice = list_abcedario.index(x)
            encripted.append(list_abcedario[(indice-desplazamiento)%len(list_abcedario)])
        else:
            encripted.append(x)
    encripted = "".join(encripted)
    return encripted

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
tabla_calculada_letter = []

# Ordenar por la distribución calculada de mayor a menor
for letra in sorted(distribucion_calculada, key=distribucion_calculada.get, reverse=True):
    porcentaje_calculado = distribucion_calculada[letra]
    tabla_calculada.add_row([letra, f"{porcentaje_calculado:.2f}%"])
    tabla_calculada_letter.append(letra)

# Crear tabla para la distribución de la lista
tabla_lista = PrettyTable()
tabla_lista.field_names = ["Letra", "Distribución Lista"]
tabla_lista_letter = []

# Ordenar por la distribución de la lista de mayor a menor
for letra in sorted(lista, key=lista.get, reverse=True):
    porcentaje_lista = lista[letra]
    tabla_lista.add_row([letra, f"{porcentaje_lista:.2f}%"])
    tabla_lista_letter.append(letra)

# Imprimir las tablas
print("Distribución Calculada:")
print(tabla_calculada)

print("\nDistribución Lista:")
print(tabla_lista)
print("_______________________________")

# print(tabla_calculada_letter)
# print(tabla_lista_letter)

# Buscar el indice de cada uno
calculado_index = list_abcedario.index(str(tabla_calculada_letter[0]))
lista_index = list_abcedario.index(str(tabla_lista_letter[0]))

# Obtener el indice incial con el cual inicial
new_index = abs((calculado_index - lista_index)-1) 
# print(new_index)

# Comenzar con la fuerza bruta de caesar
for _ in range(len(list_abcedario)):
    result = caesar_desencrtypt(word, new_index)
    print(str(new_index % len(list_abcedario)) + " : " + result)
    new_index = new_index + 1

