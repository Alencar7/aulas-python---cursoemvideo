#AULA 08

import emoji
print(emoji.emojize("hellow, word :sunglasses:", use_aliases=True))
print(":sunglasses:")


import math
#poderia ser mais especifico tb
# from math import sqrt,ceil

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(' A raiz de {} e {}.'.format(num, raiz))

#caso queria arredondar p/ cima
print(' A raiz de {} e {}.'.format(num, math.ceil(raiz))) #math.ceil() para ser especifico

#caso queria arredondar p/ cima
''' 
print(' A raiz de {} e {}.'.format(num, ceil(raiz)))
'''