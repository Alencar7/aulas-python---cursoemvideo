'''
'''

#57
'''
Faca um programa que leia o sexo de uma pessoa, mas so aceite 'M' ou 'F'.
Caso esteja errado peca a digitacao novamente, ate ter um valor correto.
'''

'''
import time

p = True
while p == p:
    sex = str(input('Qual seu sexo?\nResponda com [M/F]:'))
    sexo = sex.upper()
    print(sexo)
    if sexo =='F':
        print('salvando...')
        time.sleep(1)
        print('salvo!\n')
        time.sleep(3)
        print(f'feminino:{sexo}')
    elif sexo =='M':
        print('salvando...')
        time.sleep(1)
        print('salvo!\n')
        time.sleep(3)
        print(f'maculino:{sexo}')
    else:
        print('Responsta invalida...')
        time.sleep(2)
        print('Tente de novo!\n')
'''

#58 #JOGO_028
'''
Melhore o jogo 028 onde o computador vai 'pensar' em um numero entre 0 e 10.
So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites 
foram necessarios para ele acertar.
'''
                                                                                       #58 FEITO    `
''' 
import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
adivinhar_numero = random.choice(lista)

print(adivinhar_numero)

# numero = int(input('Tente adivinhar o numero de 0 a 10:'))
tentativa = 1 #importante colocar o valor como 1, pois ja comeca a contar da 1 tentativa!

while True:
    numero = int(input('Tente adivinhar o numero de 0 a 10:'))

    if numero != adivinhar_numero:
        print('Quase! Tente de novo!')
        tentativa += 1

    elif adivinhar_numero == numero:
        print(f'Voce acertou! O numero eh {adivinhar_numero}')
        print(f'Voce tentou por {tentativa} vezes! ')
        break
   # print(f'Voce tentou por {tentativa} vezes! ')
'''
#59  #MENU
'''
Crie um programa que leia 2 valores e mostre um menu na tela:
(1) somar
(2) multiplicar
(3) maior
(4) novos numeros
(5) sair do programa
Seu programa devera realizar a operaca solicitada em cada caso.

#LER 2 VALORES
'''

#60
'''
Faca um programa que leia um numero qualquer e mostre seu fatorial.
ex: 5! = 5x4x3x2x1 = 120
'''

#61
'''
Refaca o desafio 051, lendo o primeiro termo e a razao de uma PA, 
mostrando os 10 primeiros termos da progressao usando a estrutura 'whlie'
'''

#62
'''
Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

#63
'''
Escreva um programa que leia um numero 'n' inteiro qualquer e mostre na tela os 
'n' primeiros elementos da uma sequencia de fibonacci.
ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
https://www.youtube.com/watch?v=w7yn1_Mfu0E&t=367s
'''
#TENTATIVA hehe
'''
lista = [0,1]
lista2 = []
#lista[0] = 0
n = 1
c = int(input('Digite um numero limite para a sequencia de fibonacci: '))

print('A sequencia e:')
#a logica e sempre colocar 1 numero e o proximo numero e ele + ele
if c > 0:
    for c in range(0, c-2):
        print(f' {n}, ', end='')
        if True:
            n += lista2[n-2] + lista2[-1]
            lista2.append(n)

lista.extend(lista2)
'''
#RESOLUCAO GPT
'''
lista_de_fibonacci = [0,1]

n = (int(input('Digite o numero: ')))

while len(lista_de_fibonacci) < n:
    fibonacci = lista_de_fibonacci[-1] + lista_de_fibonacci[-2]
    lista_de_fibonacci.append(fibonacci)
print(f'A sequencia de fibonacci vai ate {lista_de_fibonacci[-1]} e a sequencia completa e {lista_de_fibonacci}')
'''
#TEM COMO CHAMAR A FUCAO DE UMA BILBIOTECA QUE JA VEM PRONTA!
'''

def fibonacci_recursivo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_lista = fibonacci_recursivo(n - 1)
        fibonacci_lista.append(fibonacci_lista[-1] + fibonacci_lista[-2])
        return fibonacci_lista

# Exemplo de uso: gerar os 10 primeiros números da sequência de Fibonacci
n = 10
resultado = fibonacci_recursivo(n)
print(resultado)  # Saída: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

'''




#64
'''
Crie um programa que leia varios numeros inteiros pelo teclado. O programa
so vai parar quando o usuario digitar o valor 999, que e a condicao de parada.
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)

#valor final
#quantidade de numeros digitados 
'''

#65
'''
Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao,
mostre a media entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar os valores.

# media dos valores
# menor valor
# maior valor
'''













