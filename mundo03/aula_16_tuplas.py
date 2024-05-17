#interessante
# () = tuplas // ou sem () pode ser tb
# [] = listas
# {} = dicionarios

lanche = ('hamburguer','suco', 'pizza', 'pudim', 'batata frita')

#usando for para cada tupla
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Satisfeito.')
#ou
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Satisfeito.')

#imprime a quantidade
for cont in range(0, len(lanche)):
    print(cont)

#imprime o conteudo
for cont in range(0, len(lanche)):
    print(lanche[cont])

# colocando a comida e a posicao
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')
#outro jeito
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

#ORDENANDO AS TUPLAS

print(sorted(lanche))

#A SOMA DAS TUPLAS JUNTA TUDO COPIANDO
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
#PESQUISANDO DENTRO DA TUPLA
print(c.count(5))
#MOSTRANDO A POSICAO DE MEMORIA NA TUPLA
print(c.index(8)) // print(c.index(2,3))
#APAGANDO UMA TUPLA
del(a)

