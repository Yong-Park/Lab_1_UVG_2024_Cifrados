from prettytable import PrettyTable

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
list_abcedario = list(alfabeto)

def afin_desencrtypt(word, a_value, b_value):
    encripted = []
    word = list(word.lower())
    for x in word:
        if x in list_abcedario:
            indice = list_abcedario.index(x)
            # print("avalue: ", a_value)
            a_inverse = (a_value**-1) % len(list_abcedario)
            # a_inverse = pow(a_value, -1)%len(list_abcedario)
            # print("ainverse: ", a_inverse)
            # print()
            position = int((a_inverse * (indice - b_value)) % len(list_abcedario) )
            encripted.append(list_abcedario[position])
        else:
            encripted.append(x)
    encripted = "".join(encripted)
    return encripted

print("Ingrese la palabra: ")
word = input()

# Comenzar con la fuerza bruta de afines
for a in range(1,27):
    for b in range(27):
        result = afin_desencrtypt(word, a, b)
        print("a:"+str(a) +"|"+ "b:"+str(b) +" : " + result)



