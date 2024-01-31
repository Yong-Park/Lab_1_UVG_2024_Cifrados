import math

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
list_abcedario = list(alfabeto)

def afin_desencrtypt(word, a_value, b_value):
    decrypted = []
    word = list(word.lower())
    for x in word:
        if x in list_abcedario:
            indice = list_abcedario.index(x)
            if math.gcd(a_value, len(list_abcedario)) == 1:
                a_inverse = pow(a_value, -1, len(list_abcedario))
                position = int((a_inverse * (indice - b_value)) % len(list_abcedario))
            else:
                # Si 'a' no es coprimo, utiliza una lógica diferente
                position = int((a_value * (indice - b_value)) % len(list_abcedario))
            decrypted.append(list_abcedario[position])
        else:
            decrypted.append(x)
    decrypted = "".join(decrypted)
    return decrypted



print("Ingrese la palabra: ")
word = input()

# Comenzar con la fuerza bruta de afines
for a in range(1,27):
    for b in range(27):
        result = afin_desencrtypt(word, a, b)
        print("a:"+str(a) +"|"+ "b:"+str(b) +" : " + result)




