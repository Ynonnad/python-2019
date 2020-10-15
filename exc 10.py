'''
exc 10
Preencher uma lista com os números 10 a 20, e depois mostrar os elementos ímpares da lista.
'''
lista16 = []
impares = []

for i in range(10,21):
    lista16.append(i)

for i in range(10):
    if (lista16[i]%2 != 0):
        impares.append(lista16[i])

print(impares[:])
