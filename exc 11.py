'''
exc 11
Preencher uma lista com os números 10 a 20, e depois mostrar os elementos pares da lista de trás para frente.
'''
lista17 = []

for i in range(10,21,2):
    lista17.append(i)

lista17.reverse()

print(lista17[:])
