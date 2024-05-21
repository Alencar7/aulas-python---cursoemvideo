#EXERCICIO 78
'''
Faca um programa que leia 5 valores numericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista.
'''
#Resolucao 78
'''

#apenas valores positivos// pra nao gastar tempo

lista = []
for c in range(0, 5):
    lista.append(int(input('Digite o numero:')))
print(f'Aqui esta a lia {lista}')
sorted(lista)
print(f'O maior valor foi {lista[-1]} e o menor foi {lista[0]}')
'''

#EXERCICIO 79
'''
Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. 
Caso o numero ja exista la dentro, ele nao sera adicionado.
No final, serao exibidos todos os valores unicos digitados, em ordem crescente.
'''
#Resolucao 79
''' 
lista = []

while True:
    num = int(input('Digite um valor: '))
    if num == 0:
        break
    if num not in lista:
        lista.append(num)

print(sorted(lista))
'''

#EXERCICIO 80
'''
Crie um programa onde o usuario possa digitart cinco valores numericos e cadastre-os em uma lista, 
ja na posicao correta de insencao( sem usar o `sort()` ).
No final, mostre a lista ordenada na tela.
'''
#Resolucao 80 - RESOLUCAO ATIPICA
'''  
lista = []
for c in range(0,5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
                posicao += 1
print(lista)
'''

#EXERCICIO 81
'''
Crie um programa que vai ler varios numero e colocar em uma lista.
Depois disso, mostre: 
a) Quantos numeros foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e se esta,ou nao, na lista.
'''
#Resolucao 81
'''
lista = []
while True:
    numero = int(input('Digite um valor: '))
    if numero == 0:
        break
    else:
        lista.append(numero)
#print(lista)
#a)
print(len(lista))
#b)
print(lista.sort(reverse=True))
#c)

if 5 in lista:
    print('O numero 5 esta na lista.')
else:
    print('O numero 5 nao esta na lista.')
'''

#EXERCICIO 82
'''
Crie um programa que vai ler varios numeros e colocar em uma lista.,
Depos disso, crie duas listas que vao conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteudo das tres listas geradas.
ex:
lista comp[]
lista de pares []
lista de impares []
'''
#Resolucao 82
'''
listaComp = []
listaPares = []
listaImpares = []

while True:
    numero = int(input('Digite um numero:'))
    if numero == -1:
        break
    #vou fazer de um jeito mais facil e simples
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)
listaComp = listaPares + listaImpares
print(listaPares)
print(listaImpares)
print(sorted(listaComp))
'''

#EXERCICIO 83
'''
Crie um programa onde o usuario digite uma expressao qualquer que use parenteses. 
Seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.
ex:
 ((a+b)*c) -> valido
 ((a+b)*c -> invalido
'''
#Resolucao 83
''' 
cont1 = 0
cont2 = 0
parentese1 = '('
parentese2 = ')'
lista = []
calculo = str(input('Digite a expressao: '))
for c in calculo:
    if parentese1 in c:
        cont1 += 1
    if parentese2 in c:
        cont2 +=1

condicao = (cont1+cont2) % 2
if condicao == 0:
    print('A expressao esta correta!')
    lista.append(calculo)
    print(lista)
else:
    print('A expressao esta incorreta!')

'''



