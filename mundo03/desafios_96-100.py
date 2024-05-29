#Desafio 96
'''
Faca um programa que tenha uma funcao chamada area(), que receba as dimencoes
de um terreno retangular(larg*comp) e mostre a area do terreno.
'''
def area(l, c):
    area = l * c
    print(f'A area total do terreno {l}x{c} deu {area} metros quadrados.')


l = int(input('Digite a largura: '))
c = int(input('Digite a area: '))
area(l,c)


#Desafio 97
'''
Faca um programa que tenha uma funcao chamada escreva(), que receba um texto
qualquer como parametro e mostre uma mensagem com tamanha adaptavel.
(a linha deve acompanhar o tamanho da msg)
ex:
> escreva('ola, mundo')
saida
> -------------
   ola, mundo
  -------------
'''
#Resolucao 97 REVER
def escreva(msg):
    contagem = len(mensagem)
    i = mensagem
    if True:
        print('-'*contagem)
        print(i)
        print('-'*contagem)


mensagem = str(input('Digite a mensagem: '))
escreva(mensagem)

#Desafio 98
'''
Faca um programa que tenha uma funcao chamada contador(), que receba tres parametros:
inicio, fim e passo; e realize a contagem.
Seu programa tem que realizar tres contagens atraves da funcao criada:
a) de 1 ate 10, de 1 em 1
b) de 10 ate 0, de 2 em 2
c) uma contagem personalizada
'''
import time
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    time.sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='')
            time.sleep(0.5)
        print('Acavou.')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='')
            cont -= p
        print('Acavou.')


contador(1,10,1)
contador(10,0,2)
print('+='*17)
inicio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(inicio, fim, passo)

#Desafio 99 (desempacotamento de parametros)
'''
Faca um programa que tenha uma funcao chamada maior(), que receba varios
parametros com valores inteiros.
Seu programa tem que analizar todos os valores e dizer qual deles e o maior.
ex:
> 3,4,5
>>> foram informados 3 valores. 3,4,5
>>> o maior valor foi 5
'''
def maior(i):
    #i = var
    #i.sort(reverse=True)
    i = sorted(var, reverse=True)
    print(f'Os valores foram {i}')
    print(f'O maior valor foi {i[0]}')


var = []
print('para parar digite 0')
while True:
    #print('para parar digite 0')
    numero = int(input('Digite um numero.'))
    if numero == 0:
        break
    else:
        var.append(numero)
maior(var)


#Desafio 100
'''
Faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas
sorteia() e somaPar(). A primeira funcao vai sortear 5 numeros e vai coloca-los
dentro da lista e a segunda funcao vai mostrar a soma entre todos os valores PARES 
sorteados pela funcao anterior.
'''
import random

num = []

def sorteia(): # SORTEAR 5 NUMEROS -> COLOCAR DENTRO DA LISTA
    for c in range(1,7):
        n = random.randint(1,100)
        num.append(n)
    print(f'Lista criada com valores: {num}')
    somaPar()


def somaPar(): # SOMA ENTRE TODOS OS VALORES PARES SORTEADOS DA DEF SORTEIA(i)
    somaPar = 0
    somaImpar = 0
    for c in num:
        if c % 2 == 0:
            somaPar += c
        else:
            somaImpar += c

    print(f'A soma deu {somaPar}')
    print(f'A soma deu {somaImpar}')


sorteia()
