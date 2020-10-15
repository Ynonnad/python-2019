'''
exc 12
Preencher uma lista com os números 10 a 20, e depois mostrar os elementos pares da lista de trás para frente. 
E também mostrar os números ímpares.
'''

lista18 = []
lista19 = []

for i in range(10,21,2):
    lista18.append(i)

for i in range(10,21):
    if (i%2 != 0):
        lista19.append(i)

lista18.reverse()
lista19.reverse()

print('='*30)

print('''
nºs pares: {}
nºs ímpares: {}
'''.format(lista18[:],lista19[:])
