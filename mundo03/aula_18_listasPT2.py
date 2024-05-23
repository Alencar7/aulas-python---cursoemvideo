teste = list()
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste) #adicionou uma lista dentro de outra lista.
teste[0] = 'adriano'
teste[1] = '23'
galera.append(teste) #adicionou uma lista alterada(n salva o antigo) dentro de outra lista.
print(galera) #vai ter o 2 testes repetidos!
# 1 lista com duas listas iguais

# para nao ficar nesse erro se coloca o [:]
# o [:] ele vai copiar o ultimo valor/valor +atualizado da lista sempre

testes = list()
testes.append('gustavo')
testes.append(40)
galeras = list()
galeras.append(testes[:])#add o primeiro valor
testes[0] = 'adriano'
testes[1] = '23'
galeras.append(testes[:])#add o 2 valor
print(galeras)
# 1 lista com 2 listas diferentes

# TESTES
galerass = [['adriano', 23], ['pedro', 29], ['joao',12], ['lucas',19]]
print(galerass[0])
print(galerass[0][0])

for p in galerass: #mostrar cada nome e idade
    print(p)

for p in galerass: #mostrar as idades
    print(p[0][0])

#usando o nome e a idade
for p in galerass:
    print(f'O {p[0]} tem {p[0][1]} anos de idade!')


#NA PRATICA ISSO AI FICA COMO???

pessoas = list()
dados = list()
totmax = totmin = 0

#LENDO OS DADOS E ARMAZENANDO

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    dados.append(int(input('CPF: ')))
    pessoas.append(dados[:]) #copia oque foi lido em dados e salva em outra lista
    dados.clear() # dados . clear reseta tudo. o () quer dizer self

print(pessoas)
#FILTRANDO OS DADOS E EXECUlTANDO

for p in pessoas:
    if p[1] >= 21:
        #condicao para maior de idade
        print(f'{p[0]} é maior de idade. ')
        #contador
        totmax += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmin +=0

print(f'Temos um total de {totmax} maiores e {totmin} menores de idade')




















