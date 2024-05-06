#36
''' '''
'''
Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
o programa vai perguntar o valor da casa, o salario do comprador e m quantos anos ele vai pagar.
Calcule o valor da prestacao mensal, sabendo que ela nao pode exercer 30% do salario
ou entao o emprestimo sera negado.
'''

#37 - fazer
'''
Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher 
qual sera a base de conversao:
- 1 para bancario
- 2 para octal 
- 3 para hexadecimal
(o py faz isso sozinho)
'''

#38
'''
Escreva um programa que leia dois numeros inteiros e compare--os, mostrando na tela uma mensagem:
- O primeiro numero e maior
- O segundo numero e maior 
- Os dois numeros sao iguais
'''

#39
'''
Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao servico militar
- se e a hora de se alistar
- se ja passou do tempo do alistamento 
o programa tb devera mostrar o tempo que falta ou que passou!
'''

#40
'''
Crie um programa que leia duas notas de um aluno e calcule a media,
mostrando a mensagfem no final, de acordo com a media atingida:
- media abaixo de 5.0 = REPROVADO
- media entre 5.0 e 6.9 = RECUPERACAO
- media 7.0 ou superior = APROVADO
'''

#41
'''
A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:
- ate 9 anos : mirim
- ate 14 anos : infantil
- ate 19 anos : junior
- ate 20 anos : senior
- acima : master
'''

#42
'''
Refaca o desafio#35 dostriangulos acrescentando o recurso de mostrar que 
tipo de triangulo sera formado:
- equilatero
- isoceles
- escaleno
'''

#43
'''
Desenvolva uma logica que leia o peso e a altura de uma pessoa, 
calcule o IMC e mostre seu status abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal 
- 25-30: sobrepeso
- 30-40: obesidade morbida
'''

#44
'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando 
o seu preco normal e condecao de pagamento:
- a vista = 10% de desconto
- avista cartao = 5% de desconto
- em 2x no cartao: preco normal
- 3x ou mais: 20% de juros
'''

#45 - JOGO PEDRA-PAPEL-E-TESOURA
'''
Crie um programa que faca o computador jogar 'jokenpo' com voce:
'''
#pedra > tesouta
#tesoura > papel
#papel > pedra

import random

jogo = ['pedra', 'papel', 'tesoura'] #a.pedra #b.papel #c.tesoura
escolha_automatica = random.choice(jogo)
#print(escolha_automatica)

print(f"\033[3;42mJogo da velha!\033[m")

escolha = str(input('Faca a sua escolha e jogue contra a maquina!\n'
                    'Escolha: \n '
                    '\033[31m(1)\033[m Pedra \n '
                    '\033[31m(2)\033[m Papel \n '
                    '\033[31m(3)\033[m Tesoura \n'                    
                    '\033[47mDigite um numero:\033[m '))
# print(escolha)
if ((escolha_automatica == 'pedra' and escolha == '1') or
        (escolha_automatica == 'papel' and escolha == '2') or
        (escolha_automatica == 'c' and escolha == '3')):
    print('O resultado deu empate!Ambos escolheram {}.'.format(escolha_automatica))
#maquina ganha
elif escolha_automatica == 'pedra' and escolha == '3':
    print(f"A maquina ganhou! O resultado da maquina foi \033[7;29m{escolha_automatica}\033[m.")
elif escolha_automatica == 'papel' and escolha == '1':
    print(f"A maquina ganhou! O resultado da maquina foi \033[7;29m{escolha_automatica}\033[m.")
elif escolha_automatica == 'tesoura' and escolha == '2':
    print(f"A maquina ganhou! O resultado da maquina foi \033[7;29m{escolha_automatica}\033[m.")
#jogador ganha
elif escolha_automatica == 'pedra' and escolha == '2':
    print(f"Voce ganhou!!! O resultado da maquina foi \033[7:29m{escolha_automatica}\033[m.")
elif escolha_automatica == 'papel' and escolha == '3':
    print(f"Voce ganhou!!! O resultado da maquina foi \033[7:29m{escolha_automatica}\033[m.")
elif escolha_automatica == 'tesoura' and escolha == '1':
    print(f"Voce ganhou!!! O resultado da maquina foi \033[7:29m{escolha_automatica}\033[m.")
else:
    print(f"\033[31mResultado invalido. Tente de novo.\033[m ")




























