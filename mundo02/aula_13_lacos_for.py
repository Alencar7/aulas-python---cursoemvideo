#SE USA QUANDO SE SABE O LIMITE :)
''' '''
'''
for comando in range(0, 10):
    print('Oi')
print('\nFim\n')

####################################################################
for contagem_normal in range(0, 10):
    print(contagem_normal)
print('\nFim\n')

####################################################################
for contando_p_tras in range(10, 0, -1):
    print(contando_p_tras)
print('\nFim\n')

####################################################################
for contando_de_2_em_2 in range(0, 10, 2):
    print(contando_de_2_em_2)
print('\nFim\n')

###################################################################
numero = int(input('Digite um numero: '))
for c in range(0, numero):
    print(c)
print('\nFIM\n')

###################################################################
inicio = int(input('Digite o inicio: \n'))
fim = int(input('Digite o fim: \n'))
pular = int(input('Digite o quanto quer pular: '))
for cc in range(inicio, fim+1, pular):
    print(cc)
print('\nFim!\n')
'''

s = 0
for laco in range(0,3):
    n = int(input('Digite um valor: '))
    s = s + n  #somatorio de valores
print(f"O somatorio dos valores foi {s}")
print('\nFIm!\n')