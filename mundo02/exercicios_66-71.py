'''

'''#DESAFIO 66
'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O preograma so vai parar quando o usuario digitar o valor 999, que e a condicao de parada.
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.
(desconsidere o flag)
#coloque quantos falores foram digitados tb!
'''

#DESAFIO 67
'''
Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado
pelo usuario. O programa sera interrompido quando o numero solicitado for negativo.
'''
#RESOLUCAO 67
'''
while True:
    condicao = int(input('Digite 1 para escrever um numero.\n'
                         'Digite -1 para parar o programa.\n'
                         '[1/-1]> '))
    if condicao > 0:
        while  True:
            numero = int(input('Digite o numero que voce deseja colocar.\n'
                  '>'))
            if numero >= 0:
                print(f'A tabuada do numero {numero} é:\n')
                for c in range (1,11):
                    resultado = c * numero
                    print(f'{c} x {numero} = {resultado}. \n')
                    c += 1
            else:
                print('Programa encerrado.')
                break
    else:
        print('Programa encerrado.')
        break
    break

'''

#DESAFIO 68
'''
Faca um programa que jogue par ou impar com o computador. O programa so sera interrompido quando
o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
#vitorias consecutivas
'''
#ex
'''
digite um valor 
escolha impa ou par
voce venceu 'n' vezes!
'''

#DESAFIO 69
'''
Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa 
devera perguntar se o usuario quer ou nao continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos
'''
# RESOLUCAO 69
''' 
lista = []

idade = int
nome = str
sexo = str
quantidade_homem = 0
quantidade_mulher = 0

print("SEJA BEM VIND@ AO SISTEMA DE CADASTROS! \n")


while True:
    var = int(input('Para entrar aperte [1].\n'
                    'Para sair aperte [0]\n'
                    '> '))
    if var == 1:
        print('Por favor, coloque seus dados.')
        idade = int(input('Digite sua idade.\n'
                          '> '))
        nome = str(input('Digite seu nome.\n'
                         '> '))
        sexo = str(input('Digite seu sexo.\n'
                         '> '))
        pessoa = (idade, nome, sexo)
        lista.append(pessoa)
        # break
    elif var == 0:
        print(lista)
        break

# a) pessoas com +18
for pessoa in lista:
    idade, nome, sexo = pessoa
    if idade > 18:
        print(f'Idade = {idade}. Nome = {nome}. Sexo = {sexo}. ')

# b) quantidade de homens cadastrados
for pessoa in lista:
    idade, nome, sexo = pessoa
    quantidade_homem += 1 if sexo == 'masculino' else 0
    print(f'Quantidade de homens cadastrados: {quantidade_homem}.\n')

# c) quantas mulheres tem menos de 20 anos
for pessoa in lista:
    idade, nome, sexo = pessoa
    quantidade_mulher += 1 if sexo == 'feminino' and idade < 20 else 0
    print(f'Quantidade de mulheres que tem menos de 20 anos: {quantidade_mulher}.')

'''


#DESAFIO 70
'''
Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se 
o usuario vai continuar. No final, mostre:
a) qual e o total gasto na compra
b) quantos produtos custam mais de R$1000
c) qual e o nome do produto mais barato
'''
#RESOLUCAO 70
'''
lista = []

valor_total = 0
preco1k = 0
preco_barato = None
produto_barato = None

while True:
    condicao = int(input(' Bem vindo! Vamos cadastrar suas compras!\n'
                         ' Pressione [1] para entrar.\n'
                         ' Pressione [0] para sair ou encerrar. \n'
                         ' > '))
    if condicao == 1:
        produto = str(input('Digite o produto:\n > '))
        preco = int(input('Digite o valor:\n > '))
        compras = (produto, preco)
        lista.append(compras)
    else:
        print('Encerrando...')
        break

# a) total gasto
for compras in lista:
    produto, preco = compras
    valor_total += preco
print(f' O valor total gasto foi de {valor_total}')

# b) produtos +1k
for compras in lista:
    produto, preco = compras
    preco1k += 1 if preco > 1000 else 0
print(f' A quantidade de produtos que custam mais de 1.000 sao {preco1k}')

# c) nome do produto mais barato /// da para fazer ordenando a lista 'sort' e pegando o menor valor dela
for compras in lista:
    produto, preco = compras
    if preco_barato is None or preco < preco_barato: #'None' para ficar sem valor
        preco_barato = preco
        produto_barato = produto
print(f'O produto com o menor valor foi o {produto_barato}, que custou {preco_barato}')
''' 

#EXERCICIO 71
'''
Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario
qual sera o valor a ser sacado(numero inteiro) e o programa vai informar quantas cedulas de cada
valor serao entregues.
OBS: considere que o caixa possui cedulas de 
R$50, R$20, R$10 e R$1
'''
#ex
'''
qual o valor:  1234
total de 24 cedulas de: 50
total de 1 cedulas de: 20
total de 1 cedulas de: 10
total de 4 cedulas de: 1
'''
#RESOLUCAO 71   
'''

valor = int(input('Digite o valor a ser sacado:\n > '))
notas = [50, 20, 10, 1] #a ordem vai fazer o for e o if funcionarem!

if valor > 0:
    for c in notas:
        quantidade = valor // c #divisao inteira 
        if quantidade > 0:
            print(f'o total de notas de R${c}: {quantidade} unidade(s).\n'
                  f'(total {c * quantidade} reais)')
            valor -= quantidade * c
            
'''































