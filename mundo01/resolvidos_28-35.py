#28
"""
import math
import random
adivinhar = [1, 2, 3, 4, 5] #o resultado vai sair em str, caso coloque '1'
adivinhar_numero = random.choice(adivinhar)
print(adivinhar_numero)
numero = int(input('Tente adivinhar qual o numero escolhido pela maquima.'
                   'Digite um numero entre 1 e 5:'))
diferenca = 1 - (adivinhar_numero - numero)
if adivinhar_numero == numero:
    print('PARABENS! Voce acertou o numero!')
elif diferenca <= 1:
    print('Quase!!! O numero escolhido pelo computador foi: {}. '.format(adivinhar_numero))
elif diferenca <= -1:
    print('Quase!!! O numero escolhido pelo computador foi: {}. '.format(adivinhar_numero))
else:
    print('Infelizmente voce errou. O numero escolhido pelo computador foi: {}. '.format(adivinhar_numero))
"""

#29
'''
print('Sistema de multas.')
velocidade = int(input('Digite a velicidade:'))
diferenca = velocidade - 80
multa = diferenca*7
if velocidade < 80:
    print('UFA!!! Voce nao ultrapassou o limite. Nao precisa se preocupar!')
elif velocidade == 80:
    print('Voce passou no limite! Gracas a isso nao precisara se preocupar.')
else:
    print('Voce ultrapassou o limite. A diferenca foi de {}K/h. Sua multa sera de R$ {}.00! '.format(diferenca, multa))
'''

#30
'''
#resto = %
numero = int(input('Digite um numero:'))
resto = numero % 2
if resto == 0:
    print('O numero e par!')
else:
    print('O numero e impar.')
'''

#31
'''
distancia = int(input('Para calcular seu destino digite a distancia, em Km, aqui: '))
if distancia == 0:
    print('Toma vergonha, po! Tem nem 1km de distancia!')
elif distancia <= 200:
    valor_passagem = float(distancia*(0.5))
    print('O valor da passagem ficou R${:.2f}.'.format(valor_passagem))
else:
    valor_da_passagem = float(distancia*(0.45))
    print('O valor da passagem ficou R${:.2f}.'.format(valor_da_passagem))
'''

#32
# da pra fazer por 2 jeitos!
#com a contal logica normal
'''
ano = int(input('Digite o ano que voce nasceu: '))

if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 ==0):
    print('Eita! O ano {} e bissexto. '.format(ano))
else:
    print('O ano {}, e so mais um ano comum. '.format(ano))
'''
#com o 'calendar'
'''
import calendar

ano = int(input("Digite o ano que deseja verificar: "))
if calendar.isleap(ano):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
'''

#33
''' 
numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

#numero 1 e 2
if (numero1 > numero2) and (numero1 > numero3) and (numero2 < numero3):
    print('O numero {} foi o maior e o numero {} foi o menor!'.format(numero1, numero2))
    print('cmp1')
#numero 1 e 3
elif (numero1 > numero2) and (numero1 > numero3) and (numero3 < numero2):
    print('O numero {} foi o maior e o numero {} foi o menor!'.format(numero1, numero3))
    print('cmp2')
#numero 2 e 3
elif (numero2 > numero1) and (numero2 > numero3) and (numero3 < numero1):
    print('O numero {} foi o maior e o numero {} foi o menor!'.format(numero2, numero3))
    print('cmp3')
#numero 2 e 1
elif (numero2 > numero1) and (numero2 > numero3) and (numero1 < numero3):
    print('O numero {} foi o maior e o numero {} foi o menor!'.format(numero2, numero1))
    print('cmp4')
#numero 3 e 1
elif (numero3 > numero1) and (numero3 > numero2) and (numero1 < numero2):
    print('O numero {} foi o maior e o numero {} foi o menor!'.format(numero3, numero1))
    print('cmp5')
#numero 3 e 2
elif (numero3 > numero1) and (numero3 > numero2) and (numero2 < numero1):
    print('O numero {} foi o maior e o numero {} foi o menor!'.format(numero3, numero2))
    print('cmp6')
else:
    print('Vamos tentar de novo, sem colocar numeros iguais. Aperte: Ctrl+f5.')

print('Comparacao feita!')
'''

#34
'''
salario = float(input('O valor nao precisa de ponto. '
                      'Digite seu salario: '))
if salario == 0:
    print('Valor nao aceitavel. ')
elif salario <= 1250:
    aumento_inferior = salario*1.15
    print('Seu salario teve um aumento! Ficou R${:.2f}. '.format(aumento_inferior))
elif salario >= 1250:
    aumento_superior = salario*1.10
    print('Seu salario teve um aumento! Ficou R${:.2f}. '.format(aumento_superior))
'''

#35
'''
reta1 = int(input('Qual o valor da primeira reta? Digite: '))
reta2 = int(input('Qual o valor da segunda reta? Digite: '))
reta3 = int(input('Qual o valor da terceira reta? Digite: '))
# triangulo = hipotenusa**2 = cateto_a**2 + cateto_a**2
if reta1**2 == (reta2**2 + reta3**2):
    print('Com o valor obtido da para fazer um triangulo!')
elif reta2**2 == (reta1**2 + reta3**2):
    print('Com o valor obtido da para fazer um triangulo!')
elif reta3**2 == (reta1**2 + reta2**2):
    print('Com o valor obtido da para fazer um triangulo!')
else:
    print('O valor das retas nao formam um triangulo! ')
'''







