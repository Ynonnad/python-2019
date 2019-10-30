'''
exc 2
Preencher uma lista de 8 elementos inteiros. 
Mostrar o vetor e informar quantos números são maiores que 30.
Somar todos os números.
'''
lista5 = []
n = 0
for i in range(8):
    x = int(input("Digite um valor inteiro:"))
    lista5.append(x)

lista5.sort()
print(lista5[:])

for c in range(8):
    if (lista5[c]>30):
        n = n + 1
print ("Há {0} números maiores que 30.".format(n))
