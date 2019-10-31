'''
exc 6
Armazenar em listas distintas, Nomes e Notas P1 e P2 de 6 alunos. 
Calcular a média de cada aluno e imprimir aprovado se a média for maior ou igual a 6 e reprovado se média for menor que 6. 
OBS.: 2 listas para as notas, 1 lista para os nomes. 1 lista para a média e 1 lista para situação.
'''
nomes = []
notas1 = []
notas2 = []
media = 0
medias = []
situacao = []

for i in range(6):
    x = input("Insira o nome dos alunos:")
    nomes.append(x)

for i in range(6):
    y = int(input("Insira a 1º nota do aluno {}:".format(nomes[i])))
    if y<0 or y>10:
            y = int(input("Insira uma nota entre 0 e 10:"))
    notas1.append(y)

for i in range(6):
    z = int(input("Insira a 2º nota do aluno {}:".format(nomes[i])))
    if z<0 or z>10:
            z = int(input("Insira uma nota entre 0 e 10:"))
    notas2.append(z)

for i in range(6):
    media = (notas1[i]+notas2[i])/2
    medias.append(media)
    media = 0

for i in range(6):
    if (medias[i]>6):
        sit = 'aprovado'
        situacao.append(sit)
    else:
        sit = 'reprovado'
        situacao.append(sit)
print('='*30)

for i in range(6):
    print ('''

    Aluno: {}
    média: {}
    situação: {}

    '''.format(nomes[i],medias[i],situacao[i]))
