
#16
"""
from math import floor
#ceil arredanoda para cima!
#floor para baixo!

numb = float(input('Digite um numero'))
redondo = int(floor(numb))
print('A porcao inteira do numero {}.'.format(numb))
print('A parte arredondada e {}'.format(redondo))
"""
from typing import List

#17
''' 
import math              #usei o import math, pois precisaria de 2 funcoes 
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
cato2 = pow(cato, 2)
cata2 = cata**2
hipotenusa = float(math.sqrt(cato2+cata2))
print('A resposta, para a hipotenusa com {} e {} '
      'como catetos e: {}'.format(cato, cata, hipotenusa))
      
'''

#18
#.a (2 jeitos)
#jeito mais longo (9 linhas)
''' 
from math import sin
from math import cos
from math import tan
from math import radians

numb = float(input('Digite o valor do angulo para achar o seno, o cosseno e a tangente, do mesmo: '))
seno = sin(radians(numb))
consseno = cos(radians(numb))
tangente = tan(radians(numb))
#valor que vai dar o numero em inteiros!
# print(seno, consseno, tangente)
print(seno, consseno, tangente)

'''

#.b
#jeito mais curto (6 linhas)
''' 
import math
numb = float(input('Digite o valor do angulo para achar o seno, o cosseno e a tangente, do mesmo: '))
seno = math.sin(math.radians(numb))
consseno = math.cos(math.radians(numb))
tangente = math.tan(math.radians(numb))
print(f"Seno: {seno:.2f}, Cosseno: {consseno:.2f} e Tangente: {tangente:.2f}.") 
#{:.2f} formatar valor com ponto flutuante

'''

#19
''' 
import random
#from random import choice
print('Programa de sorteio!! ')
a1 = str(input('Digite o nome do 1 aluno: '))
a2 = str(input('Digite o nome do 2 aluno: '))
a3 = str(input('Digite o nome do 3 aluno: '))
a4 = str(input('Digite o nome do 4 aluno: '))

#nao consegui utilizar com a string, assi substitui po utras avriaveis a [pasta]
a = a1
b = a2
c = a3
d = a4

pasta = ['a', 'b', 'c', 'd']

resultado = random.choice(pasta)
#print(resultado)
if resultado == 'a':
    print('O escolhido foi: {}'.format(a1))
elif resultado == 'b':
    print('O escolhido foi: {}'.format(a2))
elif resultado == 'c':
    print('O escolhido foi: {}'.format(a3))
elif resultado == 'd':
    print('O escolhido foi: {}'.format(a4))
    
'''

#20
'''
#QUESTAO PARECIDA COM A ANTERIOR, POREM PEDE O SORTEIO E UMA ORDEM DE 1 A ULTIMO
# para esse sorteio com ordem a biblioteca random tem o 'SHUFFLES'// embaralhar a ordem
#import random
from random import shuffle
a = input('Digite o 1 nome: ')
b = input('Digite o 2 nome: ')
c = input('Digite o 3 nome: ')
d = input('Digite o 4 nome: ')

lista = [a, b, c, d]

# shuffle(lista) ---- embaralhar a ordem(mas nao tanto. precisaria de algo a+

embaralhar = 777

#laco criado para embaralhar mais vezes
for _ in range(embaralhar):
    shuffle(lista)

print('O primeiro foi: ',lista[0],'.')
print('O segundo foi: ',lista[1],'.')
print('O terceiro foi: ',lista[2],'.')
print('O quarto foi:',lista[3], '.')
print('.')

'''

#21
#nao sabia essa
'''
import pygame

# Inicializar o pygame
pygame.init()

# Carregar o arquivo MP3
pygame.mixer.music.load('.mp3')

# Iniciar a reprodução
pygame.mixer.music.play()

# Aguardar até que a música termine de tocar
pygame.time.Clock().tick(10)  # Valor arbitrário

# Finalizar o pygame
pygame.quit()
'''
