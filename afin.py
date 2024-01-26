abecedario = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')


def afin_encrypt(word, a_value, b_value):
    encripted = []
    word = list(word.upper())
    # print(word)
    for x in word:
        if x in abecedario:
            indice = abecedario.index(x)
            position = (a_value*indice) + b_value
            position = position % len(abecedario) 
            encripted.append(abecedario[position])
        else:
            encripted.append(x)
    # print(encripted)
    encripted = "".join(encripted)
    return encripted

def afin_desencrtypt(word, a_value, b_value):
    encripted = []
    word = list(word.upper())
    for x in word:
        if x in abecedario:
            indice = abecedario.index(x)
            print("avalue: ", a_value)
            # a_inverse = (a_value**-1) % len(abecedario)
            a_inverse = pow(a_value, -1, len(abecedario))
            print("ainverse: ", a_inverse)
            print()
            position = (a_inverse * (indice - b_value)) % len(abecedario) 
            encripted.append(abecedario[position])
        else:
            encripted.append(x)
    encripted = "".join(encripted)
    return encripted

word = ""
a_value = ""
b_value = ""
option = ""

while option != "3":
    print("Cifrado de afines")
    print("[1] encriptar un mensaje")
    print("[2] desencriptar un mensaje")
    print("[3] salir")
    option = input()
    if str(option) == "1":
        print("Ingresa el mensaje que deseas encriptar: ")
        word = input()
        word = list(word.lower())
        word = [letra.replace(' ', '').replace('á',"aa").replace('é',"ee").replace('í',"ii").replace('ó',"oo").replace('ú',"uu")for letra in word]
        word = "".join(word)
        print("Ingresa el valor de a: ")
        a_value = input()
        print("Ingresa el valor de b: ")
        b_value = input()
        res = afin_encrypt(word,int(a_value),int(b_value))
        print("[*]Mensaje encryptado: ",res)
    elif str(option) == "2":
        print("Ingresa el mensaje que deseas encriptar: ")
        word = input()
        print("Ingresa el valor de a: ")
        a_value = input()
        print("Ingresa el valor de b: ")
        b_value = input()
        res = afin_desencrtypt(word,int(a_value),int(b_value))
        print("[*]Mensaje desencryptado: ",res)
    elif str(option) == "3":
        break
    else:
        print("[!] Invalido, ingresa una opcion valida")
