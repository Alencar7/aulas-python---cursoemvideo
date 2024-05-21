#Exercicio 72
'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero ate vinte.
Seu programa devera ler um numero pelo teclado e mostra-lo por extenso.

ex: 10 -> voce escreveu o numero Dez
'''
#Resolucao 72
'''
numeroExt = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze','Treze',
             'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
var = int(input('Digite um numero de 0 a 20:\n'
                '> '))
print(f'O numero {var} escrito e {numeroExt[var]}.\n')
'''
#Exercicio 73
'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro, na ordem de colocacao.
Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os ultimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabetica
d) Em que posicao ta na tabela o time do Palmeiras
'''
#Resolucao 73
'''
tabela_brasileirao_2024 = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo','Athletico-PR',
                           'Fluminense', 'Fortaleza', 'Internacional', 'São Paulo', 'Cuiabá', 'Corinthians',
                           'Cruzeiro', 'Vasco','Bahia', 'Bragantino', 'Juventude', 'Criciúma', 'Vitória', 'Atlético-GO')

#a)
print(f'> Os 5 primeiros times da tabela sao: {tabela_brasileirao_2024[:5]}')
#b)
print(f'> Os 4 ultimos times da tabela sao: {tabela_brasileirao_2024[4:]}')
#c)
ordemTabela = tuple(sorted(tabela_brasileirao_2024)) #o comando tuple ajuda a colocar os '()'
print(f'> A tabela em ordem alfabetica e: {ordemTabela}')
#d)
if True:
    posicao = tabela_brasileirao_2024.index('Palmeiras') + 1
    print(f'> A posicao do Palmeiras no comapeonato e {posicao}. ')
'''

#Exercicio 74
'''
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla.
'''
#Resolucao 74
'''
from random import randint
tupla = (randint(1,99),randint(1,99),
         randint(1,99),randint(1,99),randint(1,99))
print(tupla)
print(tupla[0], tupla[-1])
print(f'O maior valor foi {max(tupla)} e o menor foi {min(tupla)}')
'''
#da pra fazer jogando para uma lista tb... porem a tupla tem seus beneficios de max e min ;)
'''
import random
numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
embaralhado = list(numeros)
random.shuffle(embaralhado)
print(embaralhado[:5])
'''

#Exercicio 75
'''
Desenvola um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posicao foi digitado o primeiro valor 3.
c) Quais foram os numeros pares. (valor que nao existe da erro)
'''
#Resolucao 75
'''
tupla = (
    int(input('Digite um numero: ')), int(input('Digite um numero: ')),
    int(input('Digite um numero: ')), int(input('Digite um numero: '))
    )
print(tupla)
#a)
print(f'O numero 9 apareceu {tupla.count(9)} vezes!')
#b)
print(f' o valor 3 apareceu na poosicao {tupla.index(3) + 1}')
#c)
for pares in tupla:
    if pares % 2 == 0:
        print(f'Os numeros pares sao: {pares}')
'''

#Exercicio 76
'''
Crie um programa que leia uma tupla unica com nomes de produtos e seus respectivos precos na sequencia.
No final, mostre uma listagem de precos, organizando os dados em forma tabular.(somente uma tupla)

(ex:
---------------------------------
Listagem de precos
---------------------------------
lapis ....................R$ 1.75
caneta ...................R$ 3.00
--------------------------------
)
'''
#Resolucao 76
''' 
produtos = ('caneta', 7,
            'lapizeira', 4.5,
            'borracha', 3,
            'caderno', 10,
            'caderneta', 25,
            'corretivo', 4.5,
            'estojo', 7,
            'lapis',10
            )
print('-'*50)
print(f'{"TABELA DE PRODUTOS":-^50}\n')

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<42}', end='')
    else:
        print(f'R$ {produtos[posicao]:>5.2f}')
print('-'*50)
'''

#Exercicio 77
'''
Crie um programa que tenha uma tupla com varias palavras(nao usar acentos).
Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais.

ex:
aprender - a, e, e
'''
#Resolucao 77
'''
palavrasTupla = ('Adriano', 'Ari', 'isis', 'Tulio', 'Ingrid', 'Ivis', 'Kaka','Dona Ceica')

for palavra in palavrasTupla:
    print(f'\nA palavra {palavra.upper()} tem: ', end='') #o < end='' > tem a funcao de nao pular linha e de continuacao 
    for vogais in palavra:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')

'''
