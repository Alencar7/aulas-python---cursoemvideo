#22
'''
var = input(' Digite seu nome: ')
#a #maiusculo
NOME = var.upper()
print(NOME)
#b #minusculo
nome = var.lower()
print(nome)

#c #contar caracteres, sem contar com os espacos
'''
''' atencao no len(), pois e uma funcao embutida. 
Nao uma string(tipo o 'strip()' )'''
''' 
# sem_espaco = var.strip() --------> nao funcionou

#usei o replace, substituindo o espaco por vazio!

sem_espaco = var.replace(" ","")
quantidade = len(sem_espaco)
print(quantidade)
# print('O numero de caracteres deu {}.'.format(quantidade))
'''

#23
'''
#descobri que tem uma linha de raciocinio a qual transforma em string e separa por cadeias
dig = int(input('Digite um numero entre 0 e 9999: '))
#e necessario transformar para string, para obter a precisao e trabalhar de forma unica com cada um
dig_str = str(dig)
uni = int(dig_str[-1]) # o sinal de `-` e usado para pegar a str da direita para a esquerda
dez = int(dig_str[-2]) if len(dig_str) > 1 else 0     # se len [-2] for maior que 1, volta o valor
cen = int(dig_str[-3]) if len(dig_str) > 2 else 0    # se len [-3] for maior que 2, volta o valor
mil = int(dig_str[-4]) if len(dig_str) > 3 else 0     # se len [-4] for maior que 3, volta o valor

print(' O numero foi separado em unidade, dezena, centena e milhar.')
print(' - unidade: {} '.format(uni))
print(' - dezena: {} '.format(dez))
print(' - centena: {} '.format(cen))
print(' - milhar: {} '.format(mil))

'''

#24
#tentativa.01 --- COMPLETAMENTE ERRADA, MAS TAPA BURACO
'''
cidade = str(input('Qual a cidade: '))
nome = str(cidade.upper())
condicao = 'SANTO' in nome
if condicao == True:
    print('A cidade ecrita comeca com `Santo`. ')
elif condicao == False:
    print('A cidade nao comeca com `Santo`.')
'''

#tentativa.02 /// #25
''' 
cidade = str(input('Qual a cidade: '))
nome = cidade.upper()
print(nome)
condicao = nome.find('SANTO')
print(condicao)
print('O resultado: ')
if condicao == 0: #COMECA COM 0
    print('A cidade {} comeca com `Santo`. '.format(cidade))
elif condicao > 0:
    print('A cidade {} nao comeca com `Santo`, Entretanto e composta por Santo. '.format(cidade))
else:
    print('A cidade {} nao comeca com `Santo`. '.format(cidade))
'''

#26
'''
frase = str(input('Escreva uma frase qualquer: '))
quantidade_total = len(frase)
print('A frase: "{}".'
      ' Possui {} caracteres.'.format(frase,quantidade_total))
quantidade_a = frase.count('a')
print('Na frase acima, a letra "a" '
      'se repete {} vezes.'.format(quantidade_a))
a0 = frase.find('a')
print('A primeira vez que a letra "a" apareceu foi no caractere "{}".'.format(a0))
a1 = frase.rfind('a')
print('A ultima vez que a letra "a" apareceu foi no caractere "{}".'.format(a1))
'''

#27
'''
nome = str(input('Digite seu nome completo: '))
vari = nome.title().split()
#['0', '1', '2', '3', '4', ...] o ultimo da lista eu posso consultar com -1, o penultimo -2...
primeiro_nome = vari[0] #nome = primeiro nome da lista
sobrenome = vari[-1] #sobrenome = ultimo nome da lista
identificacao = primeiro_nome + sobrenome

print('E um prazer te conhecer, {} {}.'.format(primeiro_nome, sobrenome))
print(identificacao)
'''






