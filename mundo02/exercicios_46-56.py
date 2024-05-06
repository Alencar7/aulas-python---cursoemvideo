''''''

#46
''' 
Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
indo de 10 ate 0, com uma pausa de 1 segundo entre eles.

#biblioteca de espera de tempo
#emoji de fogos estourando
'''
                                                                                                          #RESOLUCAO 46
'''
import emoji
import time
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print('Acabou! Veja os fogos!')
fogos_emoji = emoji.emojize(":fireworks:")
for tempo in range(0,7):
    print(f"{fogos_emoji}")
    time.sleep(0.5)
'''

#47 ver depois!
'''
Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50.
'''
                                                                                                          #RESOLUCAO 47
'''
for numero_par in range(2, 51, 2):
    print(numero_par)
'''

#or

''' 
numeros_pares = [numero for numero in range(1, 51) if numero % 2 == 0]

for numero in numeros_pares:
    print(numero)
'''

#48
'''
Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3
e que se entcontram no intervalo de 1 a 500.
#impares
#multiplo de 3 
#soma
'''
                                                                                                          #RESOLVIDO 48
'''
#comando_impar_3_soma = [lista for lista in range(1,501, 2) ]
#print(comando_impar_3_soma)
numero = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        numero += c
print(numero)
'''

#49
'''
Refaca o desafio 9, mostrando a tabuada de um numero que o usuario escolher, so que 
agora utilizando 'for'.
'''
                                                                                                          #RESOLUCAO 49
''' 
recebe_numero = int(input('Digite o numero: '))
for c in range(0,11):
    if recebe_numero != 0:
        tabuada = recebe_numero*c
        print(f"{recebe_numero}x{c} = {tabuada} \n")
'''


#50
'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas 
daqueles que forem pares!
Se o valor for imp[ar desconsidere-o.
'''
                                                                                                          #RESOLUCAO 50
'''
numero_par = 0
for c in range(0,6):
    numero = int(input(f"({c})Digite o numero: "))
    if numero % 2 == 0:
        numero_par += numero
print(f"\nA soma dos numeros pares, da sequencia acima, deu: {numero_par}")
'''

#51
'''
Desenvolva um programa que leia o primeiro termo e a razao de uma PA. 
No final, mostre os 10 primeiros termos dessa progressao. 
'''
                                                                                                          #RESOLUCAO 51
'''
#PA => an = a1 + (n-1) * r
numero_a1 = int(input('Digite um numero: '))
razao = int(input('Digite um numero, para ser a razao: '))
for c in range(1, 11):
    formula = numero_a1 + (c-1) * razao
    print(f"({c}) - Resultado: {formula}")
'''


#52
'''
Faca m programa que leia um numero inteiro e diga se ele e ou nao um numero primo.
'''
                                                                                                          #RESOLUCAO 52
'''
p = recebe_numero = int(input('Digite um numero: \n'))

if recebe_numero <= 1:
    print(f"O {recebe_numero} não é primo!")
else:
    # se de 2 ate n-1 nao houver nenhum numero que possa dividir o numero 'n', ele é primo!
    for c in range(2, recebe_numero):
        if recebe_numero % c == 0:
            print(f"{recebe_numero} não é primo")
            break
        else:
            print(f"{recebe_numero} é primo!")
print('Fim')
'''


#53
'''
Crie um programa que leia uma frase qualquer e diga se ela e um PALIDROMO, 
desconsiderando os espacos. 
#sem espacos
ex: - apos a sopa
    - a sacada da casa
    - a torre da derrota
    - anotaram a data da maratona
'''
                                                                                                    #RESOLUÇÃO 53 - UAU

#NAO E TAO DIFICIL COMO PARECE!
#A LOGICA E TRANSFORMAR A FRASE EM UMA CADEIA DE CARACT E JOGAR 2 VARIAVEIS 
#(VAR 1. +1  & VAR 2. -1) DEPOIS COMPARAR AS VARIAVEIS ou frase 1 e frase -1
'''
frase = str(input('Qual a frase: '))
frase_simp = frase.lower().replace(" ","").replace(".","").replace("!","")
#palidromo == frase_simp == frase_simp[ : :-1]
#if palidromo == True:
if frase_simp == frase_simp[ : :-1]:
    print(f"A frase '{frase}' é um palidromo!")
else:
    print(f"A frase não é um palidromo!")

'''

#54
'''
Crie um programa que leia o ano de nascimento de 7 pessoas. No final, 
mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
#maioridade = 21 anos
'''
                                                                                                          #RESOLUCAO 54
'''
contagem = 0
for c in range(0, 8):
    ano = int(input(f"{c}. Qual o ano do nascimento? \n"))
    if ano <= 2003:
        true = 1
        contagem += true

menor = c - contagem

print(f"O numero de pessoas maiores de idade é {contagem} e as que sao menores de idade {menor}")
'''

#55
'''
Faca um programa que leia o peso de 5 pessoas. No final, mostre qual foi 
o maior e o menos peso lidos.
'''
                                                                                                          #RESOLUCAO 55

#organizar em ordem decrescente a lista ja ajuda! -> sort() -> reverse=True
'''
lista = []
for c in range(1,6):
    pesos = int(input(f"Digite o peso da pessoa {c}:"))
    lista.append(pesos)
lista.sort(reverse=True)
print(f"O maior peso foi {lista[0]} e o menor peso foi {lista[-1]}")
'''

#OUTRA MANEIRA

'''
Inicializa as variáveis para o maior e menor peso
maior_peso = 0
menor_peso = float('inf')

Loop para ler o peso de 5 pessoas
for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i} em kg: "))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

Imprime o maior e o menor peso
print("O maior peso lido foi:", maior_peso, "kg")
print("O menor peso lido foi:", menor_peso, "kg")
'''


#56
'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    - A media de idade do grupo
    - Qual e o homem mais velho
    - Quantas mulheres tem menos de 20 anos
'''

lista_homem = []
idade_homem = []
lista_mulher = []
idade_mulher = []

lista_idade_ = []

for c in range(1, 5):
    recebe = int(input(f"Pergunta {c}.\nDigite (1) para Homem e (2) para Mulher:"))

    if recebe == 1:
        homem_nome = str(input('Qual e o seu nome?\n'))
        lista_homem.append(homem_nome)
        homem_idade = int(input('Qual e a sua idade?\n'))
        idade_homem.append(homem_idade)

        lista_idade_.append(idade_homem)

    elif recebe == 2:
        mulher_nome = str(input('Qual e o seu nome?\n'))
        lista_mulher.append(mulher_nome)
        mulher_idade = int(input('Qual sua idade:\n'))
        idade_mulher.append(mulher_idade)

        lista_idade_.append(idade_mulher)
    else:
        print('Tente de novo.')

print(lista_idade_)

idade_homem.sort(reverse=True)
print(f"A idade do homem mais velho e {idade_homem[0]}")
media = (sum(idade_homem) + sum(idade_mulher)) / len(lista_idade_)
print(f"A media de idade do grupo e {media}")































