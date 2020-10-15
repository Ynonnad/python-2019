'''
exc 1
Preencher uma lista com os números pares do número 2 a 20. 
Preencher uma lista com os números de 10 a 19. 
Concatenar e ordenar as listas.
''''

lista3 = []
for i in range (2,20,2):
    lista3.append(i)
lista4 = []
for i in range (10,19):
    lista4.append(i)

lista3.extend(lista4[:])
lista3.sort()
print(lista3[:])
