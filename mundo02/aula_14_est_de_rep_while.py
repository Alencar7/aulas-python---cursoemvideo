# QUANDO NAO SE SABE O LIMITE
'''
for c in range(0, 10):
    print(C)
print('\nFim\n')
######################COMANDOS IGUAIS########################
c = 1
while c<10:
    print(c)
    c += 1 # c = c + 1
print('\nFim\n')
'''
''' 
#################### COMANDO BASICO 1.0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))

#################### COMANDO BASICO 1.2
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] \n')).upper()
print('fim.')
'''
#################### COMANDO 1.3
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Voce digitou {par} numeros pares e {impar} numeros impares! \n")
