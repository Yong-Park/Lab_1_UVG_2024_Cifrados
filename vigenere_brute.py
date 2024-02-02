from tabla import *

vigenere_table = tabla.tabla_vigenere

def vigenere_desencrypt(mensaje, clave):
    mensaje_list = list(mensaje.upper())
    clave_list = list(clave.upper())
    new_clave_list = []
    desencrypt_messaje = []
    i = 0
    for _ in range(len(mensaje_list)):
        if i >= len(clave_list):
            i = 0
        new_clave_list.append(clave_list[i])
        i += 1

    for j in range(len(mensaje_list)):
        for k in range(len(vigenere_table)):
            if new_clave_list[j] in vigenere_table[0]:
                if new_clave_list[j] == vigenere_table[k][0]:
                    for l in range(len(vigenere_table[k])):
                        if mensaje_list[j] == vigenere_table[k][l]:
                            desencrypt_messaje.append(vigenere_table[0][l])
            else:
                desencrypt_messaje.append(mensaje_list[j])

    desencrypt_messaje = "".join(desencrypt_messaje)

    return desencrypt_messaje

def generate_combinations(try_wordlist, length, file):
    if len(try_wordlist) == length:
        wordlist = "".join(try_wordlist)
        decrypted_message = vigenere_desencrypt(word, wordlist)
        output = f'Try Wordlist: {wordlist}, Decrypted Message: {decrypted_message}\n'
        print(output)
        file.write(output)
        return

    for char in range(ord('a'), ord('z') + 1):
        try_wordlist.append(chr(char))
        generate_combinations(try_wordlist, length, file)
        try_wordlist.pop()

try_wordlist = ['s']

print("Ingrese la palabra: ")
word = input()

with open('output.txt', 'w') as file:
    # Iniciar con la lista try_wordlist [s, a, a, a] y generar combinaciones
    for length in range(4, 5):
        generate_combinations(try_wordlist, length, file)
