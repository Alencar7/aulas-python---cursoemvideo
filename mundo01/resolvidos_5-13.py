#desafio 05
'''
number = int(input('Digite um numero: '))
ant = (number - 1)
suc = (number + 1)
print('Aqui está seu número {}.'.format(number))
print('O antecessor {} e o sucessor {} do seu número {}'.format( ant, suc, number))
'''

#desafio 06
'''
number = int(input('Digite um numero: '))
trip = number*3
dobro = number*2
raiz = number**2
print('Aqui está seu número {}.'.format(number))
print('O triplo do seu numero( {} ) é {},'
      ' o dobro é {} e '
      'a raiz quadrada é {}'.format( number, trip, dobro, raiz))
'''

#desafio 07
'''
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
print('A media das suas notas(nota 1= {} e 
nota 2= {} ) deu: {}'.format(nota1, nota2, media))
'''

#desafio 08
'''
valor = float(input('Digite o valor em metros: '))
cm = valor*100
mm = valor*1000
print('A medida passada foi de {}. '
      'O valor em centimetros foi {} cm e 
      o valor em milimetros deu {} mm'.format(valor, cm, mm))
'''

#desafio 09
'''
nu = int(input('Digite um numero: '))
tab = nu*1, nu*2, nu*3, nu*4, nu*5, nu*6, nu*7, nu*8, nu*9, nu*10
print('A tabuada do numero({}) e: {}'.format(nu, tab))
'''

#desafio 10
'''
real = float(input('Digite o valor desejado: '))
cambio = 3.27
dol = real/cambio

print(' Voce pode comprar {:.3f} dolares. Com seu(s) {} reais.'.format(dol, real))

### Neste código, :.3f irá formatar o número para ter até 3 casas decimais.
# saber a diferenca entre um numero em 'float'(13.5534) e em 'tuple'(23,3234)
# nao se usa ',' e sim '.' para separar os decimais.
'''

#desafio 11
'''
lar = float(input(' Digite a largura(em metros) da parede: '))
alt = float(input(' Agora digite a largura, em metros, da parede: '))
area = lar*alt
metro2 = area/2**2
print(' A area da parede foi de {:.2f} metros quadrados. '
      'A quantidade de tinta sera {:.2f} litro(s)'.format(area, metro2))
#nao sei como colocar o m2 em cima. o bing disse que era alt+(numero)
'''

#desafio 12
'''
preco = float(input('Digite o valor do produto: '))
desc = preco*0.95
print('O valor final, com 5% de desconto foi de {:.2f} real(is).'.format(desc))
'''

#desafio 13
'''
sal = float(input('Digite o valor do seu salario: '))
aum = sal*1.1
print('O valor final, com 10% de aumento foi de {:.2f} real(is).'.format(aum))
'''




























