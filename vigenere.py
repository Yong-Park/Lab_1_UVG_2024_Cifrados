from tabla import *

vigenere_table = tabla.tabla_vigenere


def vigenere_encrypt(mensaje,clave):
    #convertir en lista el mensaje
    mensaje_list = list(mensaje.upper())
    clave_list = list(clave.upper())
    new_clave_list = []
    encrypt_messaje = []
    i = 0
    for _ in range(len(mensaje_list)):
        if i >= len(clave_list):
            i = 0
        new_clave_list.append(clave_list[i])
        i += 1
        
    #comenzar a encriptar
    for j in range(len(mensaje_list)):
        for k in range(len(vigenere_table)):
            if mensaje_list[j] == vigenere_table[k][0]:
                # print("mensaje_list[j]: ",mensaje_list[j])
                # print("vigenere_table[k][0]: ",vigenere_table[k][0])
                # print("")
                for l in range(len(vigenere_table[k])):
                    if new_clave_list[j] == vigenere_table[0][l]:
                        # print("new_clave_list[j]: ", new_clave_list[j])
                        # print("vigenere_table[k][l]: ",vigenere_table[k][l])
                        # print("===============================")
                        encrypt_messaje.append(vigenere_table[k][l])
            else:
                encrypt_messaje.append(mensaje_list[j])
                        
    # print(mensaje_list)
    # print(new_clave_list)
    # print(encrypt_messaje)
    encrypt_messaje = "".join(encrypt_messaje)
    
    return encrypt_messaje

def vigenere_desencrypt(mensaje,clave):
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
        
    #comenzar a desencriptar
    for j in range(len(mensaje_list)):
        for k in range(len(vigenere_table)):
            if new_clave_list[j] == vigenere_table[k][0]:
                # print("new_clave_list[j]: ",new_clave_list[j])
                # print("vigenere_table[k][0]: ",vigenere_table[k][0])
                # print("")
                for l in range(len(vigenere_table[k])):
                    if mensaje_list[j] == vigenere_table[k][l]:
                        # print("vigenere_table[k]: ", vigenere_table[k])
                        # print("mensaje_list[j]: ", mensaje_list[j])
                        # print("vigenere_table[k][l]: ",vigenere_table[k][l])
                        # print("===============================")
                        desencrypt_messaje.append(vigenere_table[0][l])
            else:
                desencrypt_messaje.append(mensaje_list[j])
                        
    desencrypt_messaje = "".join(desencrypt_messaje)
    
    return desencrypt_messaje

mensaje = ""
clave = ""
option = 0

while option != 3:
    print("Cifrado de vigenere")
    print("[1] encriptar un mensaje")
    print("[2] desencriptar un mensaje")
    print("[3] salir")
    option = input()
    if str(option) == "1":
        print("Ingresa el mensaje que deseas encriptar: ")
        mensaje = input()
        mensaje = list(mensaje.lower())
        mensaje = [letra.replace('á',"aa").replace('é',"ee").replace('í',"ii").replace('ó',"oo").replace('ú',"uu")for letra in mensaje]
        mensaje = "".join(mensaje)
        print("Ingresa la clave con el cual lo vas a encriptar: ")
        clave = input()
        res = vigenere_encrypt(mensaje,clave)
        print("[*]Mensaje encryptado: ",res)
    elif str(option) == "2":
        print("Ingresa el mensaje que deseas encriptar: ")
        mensaje = input()
        print("Ingresa la clave con el cual lo vas a encriptar: ")
        clave = input()
        res = vigenere_desencrypt(mensaje,clave)
        print("[*]Mensaje desencryptado: ",res)
    elif str(option) == "3":
        break
    else:
        print("[!] Invalido, ingresa una opcion valida")
