num = [2,5,9,1]
#add a lista
print(num.append(7))
#ordenar -1
print(num.sort(reverse=True))
#contador
print(num)
#add valor
print(num.insert(2,0))
#remover valores
print(num.remove(2))

#ex
if 5 in num:
    num.remove(5)
else:
    print('nao achei o numero 5')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end = '')

for c, v in enumerate(valores):
    print(f'na posicao {c} o valor e {v}.')

# ADICIONANDO VALORES DIRETO PARA A LISTA
valor = list()
for cont in range(0,5):
    valor.append(int(input('Digite um valor')))

# CUIDADO NAS LIGACOES DE LISTA
a = [1,2,3,4]
b = a
# b = a -------> igualando as listas! ESTA SENDO FEITA UMA LIGACAO E NAO UMA COPIA
b[2] = 8
print(a)
print(b)

#FAZENDO UMA COPIA!
aa = [1,2,3,4]
bb = aa[:] #COPIANDO aa EM bb
bb[2] = 8
print(aa)
print(bb)
