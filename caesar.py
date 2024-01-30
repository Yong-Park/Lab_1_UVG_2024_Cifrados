abecedario = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')


def caesar_encrypt(word, desplazamiento):
    encripted = []
    word = list(word.upper())
    # print(word)
    for x in word:
        if x in abecedario:
            indice = abecedario.index(x)
            encripted.append(abecedario[(indice+desplazamiento)%len(abecedario)])
        else:
            encripted.append(x)
    # print(encripted)
    encripted = "".join(encripted)
    return encripted

def caesar_desencrtypt(word, desplazamiento):
    encripted = []
    word = list(word.upper())
    for x in word:
        if x in abecedario:
            indice = abecedario.index(x)
            encripted.append(abecedario[(indice-desplazamiento)%len(abecedario)])
        else:
            encripted.append(x)
    encripted = "".join(encripted)
    return encripted

word = ""
desplazamiento = ""
option = ""

while option != "3":
    print("Cifrado de caesar")
    print("[1] encriptar un mensaje")
    print("[2] desencriptar un mensaje")
    print("[3] salir")
    option = input()
    if str(option) == "1":
        print("Ingresa el mensaje que deseas encriptar: ")
        word = input()
        word = list(word.lower())
        word = [letra.replace('á',"aa").replace('é',"ee").replace('í',"ii").replace('ó',"oo").replace('ú',"uu")for letra in word]
        word = "".join(word)
        print("Ingresa la cantidad de desplazamiento: ")
        desplazamiento = input()
        res = caesar_encrypt(word,int(desplazamiento))
        print("[*]Mensaje encryptado: ",res)
    elif str(option) == "2":
        print("Ingresa el mensaje que deseas encriptar: ")
        word = input()
        print("Ingresa la cantidad de desplazamiento: ")
        desplazamiento = input()
        res = caesar_desencrtypt(word,int(desplazamiento))
        print("[*]Mensaje desencryptado: ",res)
    elif str(option) == "3":
        break
    else:
        print("[!] Invalido, ingresa una opcion valida")
