# Desafio 84
'''
Faça um programa que leia o nome e o peso de varias pessoas,
guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves

- while = varias pessoas
'''
# Resolucao 84

lista = list()
dados = list()
contador = 0
while True:
    condicao = input('Para cadastrar [1].\n'
                         'Para encerrar [0].\n'
                         '>>>')
    if condicao == '1':
        print('Vamos comecar!')
        dados.append(str(input('Nome: '))) #dados[0][0]
        dados.append(int(input('Peso: '))) #dados[0][1]
        lista.append(dados[:])
        dados.clear()
        contador += 1

    elif condicao == '0':
        print('Dados salvos.')
        print('Programa encerrado.')
        break
    else:
        print('Resposta invalida. Tente novamente.\n')

print(lista)
print(contador)

#a) Quantas pessoas foram cadastradas?
print(f'A quantidade de pessoas cadastradas foi de {contador}.')

#b) Uma listagem com as pessoas mais pesadas ?
#------->decidi que a media seria o parametro

print(f'A ordem das pessoas mais pesadas:\n')
media = 0
for item in lista:
    nome, peso = item
    media += peso
print(media, contador)
print('Os mais pesados sao:')
for pp in lista:
    if pp[1] >= (media/contador):
        print(f'> {pp[0]}')
        
#c) Uma listagem com as pessoas mais leves
print(f'A ordem das pessoas mais leves:\n')
print('Os mais magors sao:')
for p in lista:
    if p[1] <= (media/contador):
        print(f'> {p[0]}')
        


# Desafio 85
'''
Crie um programa onde o usuário possa digitar sete valres numericos
e cadastre-os em uma lista unica que mantenha separados os valores 
pares e impares. No final, mostre os valores 
pares e impares em ordem crescente.

- for = 7 valores
'''
#rascunho
'''
lista = list()
par = list()
impar = list()

for c in range(0,7):
    numero = (int(input('Digite um numero:')))
    if numero%2 == 0:
        numero_par = numero
        par.append(numero_par)
        #lista.append(par[:]) -----> vai colar todo valor 1 por 1
    else:
        numero_impar = numero
        impar.append(numero_impar)
        #lista.append(impar[:]) ---> vai colocar todo valor 1 por 1

lista.append(par[:])
lista.append(impar[:])
print(f'LISTA COMPLETA: {lista}')
print(f'LISTA IMPARES: {impar}')
print(F'LISTA PARES: {par}')
'''
#Resolucao 85


lista = [[],[]]
valor = 0

for c in range(0,7):
    numero = (int(input('Digite um numero:')))
    if numero%2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

print(f'LISTA COMPLETA: {lista}')
lista[0].sort()
print(F'LISTA PARES: {lista[0]}')
lista[1].sort()
print(f'LISTA IMPARES: {lista[1]}')



# Desafio 86 -> relativamente facil -> depois que aprende fica facil msm :)
'''
Crie um programa que crie uma matriz de dimensão 3x3 com valores 
lidos pelo teclado. No final, mostre a matris na tela, com a formatação correta.
ex: 
[1][2][3]
[4][5][6]
[7][8][9]
'''
#Resolucao 86

matriz = [[0,0,0],[0,0,0],[0,0,0]]
#matriz = [[lista],[coluna],[var]]

for linha in range(0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero para [{linha},{coluna}]:'))
        
#para imprimir a matriz agora? 
for linha in range(0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print() # esse print vai quebrar a linha



# Desafio 87 -> depende do 86
'''
Aprimorar o desafio anterior, mostrando no final:
a) a soma de todos os valores digitados
b) a soma dos valores da 3 coluna
c) o maior valor da segunda linha
'''
#Resolucao 87

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero para [{linha},{coluna}]:'))

# para imprimir a matriz agora?
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()  # esse print vai quebrar a linha

# matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
#a) a soma de todos os valores digitados
total = 0
for lin in matriz: #ler as linhas
    for item in lin: # ler cada valor dentro das linhas
        total += item
print(total)

#b) a soma dos valores da 3 coluna
total_coluna = 0
for z in matriz[2]:
    total_coluna += z
print(total_coluna)

#c) o maior valor da segunda linha
matriz[1].sort()
linha2 = matriz[1]
print(linha2[-1])
#outro jeito
maximo = matriz[1]
valorr = max(maximo)
print(valorr)



# Desafio 88
'''
Faça um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros,
entre 1 e 60, para cada jogo, cadastrando tudo em uma lista.

ex: n numeros 
jogo 1: [4,5,6,7,8,9]
jogo n: ...
'''
#Resolucao 88

import random
jogos = []
numero_sort = list()

var = int(input('Digite quantas tabelas de jogos voce quer sortear:\n > '))
for n in range(0,var):
    #no comeco do loop deve zerar o 'jogos' para sempre ter um novo valor a cada loop
    jogos.clear()
    # logica da tabela de jogos
    for c in range(6):
        num = random.randint(1,60)
        numero_sort.append(num)
        jogos.append(numero_sort[:])
        numero_sort.clear()
    print(f'Jogo {n + 1}: {jogos}')



# Desafio 89
'''
Crie um programa que leia nome e duas notas de varios alunos e guarde em uma 
lista composta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.

ex:
- if
    |-> entrar

    --- while -> dados de varios alunos
        |-> continuar?
        |-> break

    -- print(nomes, media)

    --- while -> mostrar notas?
        |-> print(nome do aluno, media, notas separadas)
        |-> break
- exit
'''
# Resolucao 89

lista = []
dados = list()
contador = 0

#questionario
while True:
    ent = str(input('Deseja cadastrar? \n [S/N] > '))
    entrar = ent.upper()
    if entrar == 'S':
        contador += 1
        dados.append(str(input('Nome: ')))  # dados[0][0]
        dados.append(int(input('Nota 1: ')))  # dados[0][1]
        dados.append(int(input('Nota 2: ')))
        #nome.append(notas)
        lista.append(dados[:])
        dados.clear()
    elif entrar == 'N':
        print('Saindo.')
        break

#boletim
print('-'*35)
print('Boletim do(s) aluno(s):')
linha = 0
for nn in lista:
    media = (lista[linha][1] + lista[linha][2]) / 2
    nome = lista[linha][0]
    nota_1 = lista[linha][1]
    nota_2 = lista[linha][2]
    print(f'- Aluno: {nome} \n'
          f'- Notas: {nota_1} e {nota_2} \n'
          f'- Media: {media} ')
    linha += 1
    print('-' * 35)


