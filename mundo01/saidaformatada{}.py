print('olá, mundo')
nome = input('digite seu nome: ')
# print('É um prazer lhe conhecer, !',nome) #saina normal
print('É um prazer te conhecer, {}!'.format(nome)) # saida formatada

nome2 = input('digite seu nome: ')
print('É um prazer te conhecer, {:10}!'.format(nome))
# : = caracteres
print('É um prazer te conhecer, {:>10}!'.format(nome))
# : = caracteres p/ direita
print('É um prazer te conhecer, {:^10}!'.format(nome))
# : = caracteres centralizado

print('É um prazer te conhecer, {:=^10}!'.format(nome))
# : = caracteres centralizado