#cont = 1
#while cont <= 10:
#   print(cont, ' > ', end='')
#    cont += 1
#print('Acabou!')

'''
loop infinito
'''
''' 
cont = 1
while True:
    print(cont, ' > ', end='')
    cont += 1
print('Acabou!')
'''
#condicao while com FLAG
n = 0
while n != 999:
    n = int(input('Digite um numero: '))

#GAMBIARRA PARA SOMAR VALORES, POREM COM FLAGS
n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    s += n
    s -= 999 #GAMBIARRA
print(f"A soma dos valores deu: {s}")

#COMO FAZER SEM ESSA GAMBIARRA?

n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n == 999: #CONDICAO, PARA NAO FAZER GAMBIARRAS :)
        break
    s += n
print(f'A soma dos valores deu: {s}')


