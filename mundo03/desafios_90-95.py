#Desafio 90
'''
Faça um prog que leia o nome e a media do aluno,
garantindo tambem a situacao em um dicionario.
No final, mostre o conteudo da estrutura na tela.

#ex
nome = adr
media de adr = 9
nome e igual a 'adr'
media e igual a 9
situacao e igual a aprovado
'''
#Resolucao 90

lista = []
dados = {}
media = 7
while True:
    cond = str(input('Deseja entrar?\n[S/N]> '))
    condicao = cond.upper()
    if condicao =='S':
        dados['nome'] = str(input('Nome: '))
        dados['media'] = float(input('Media: '))
        lista.append(dados.copy())
    elif condicao == 'N':
        print('Programa encerrado.')
        break
    else:
        print('Tente novamente!')

print('-='*34)
print(lista)
print('-='*34)
for pessoa in lista:
    print(f'Nome = {pessoa['nome']} ')
    print(f'Media de {pessoa['nome']} = {pessoa['media']}')
    if pessoa['media'] > media:
        print(f'{pessoa['nome']} esta aprovado!')
    else:
        print(f'{pessoa['nome']} esta reprovado!')
    print('-=' * 34)



#Desafio 91
'''
Crie um programa onde 4 jogadores joguem um dado e enham resultados 
aleatorios. Guarde-os em um dicionario. No final, coloque esse dicionario
em ordem, sabendo que o vencedor tirou o maior numero no dado.
# from operator import itemgetter
'''
#Resolucao 91 ----------- #coisas de fora da aula #colocar o dicionario em ordem

from random import randint
from time import sleep
from operator import itemgetter

ranking = ()
jogo = {'jogador_1': randint(1,6),
        'jogador_2': randint(1,6),
        'jogador_3': randint(1,6),
        'jogador_4': randint(1,6)}

for n, v in jogo.items():
    print(f'{n} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#key=itemgetter(1)=> (1) => para pegar apenas os valores int
#print(ranking)
print('-='*30)
for posicao, v in enumerate(ranking):
    #enumerate e para listas e o items() ara dicionarios
    print(f'{posicao+1} lugar: {v[0]} com {v[1]}')
    sleep(1.5)



#Desafio 92
'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os(com idade) em um dicionario se por acaso a CTPS for diferente
de zero, o dicionario recebera tambem o ano de contratacao e o salario.
Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
'''
#Resolucao 92


from datetime import datetime
#datetime.now().year => ano atual

dados = {}

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho: (0 nao tem) '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario(R$): '))
    #aposentadoria = idade + (ano de contrataco + tempo de trabalho )- ano atual)
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
#print(dados)
print('-='*30)
for nome_chave, valor_dentro_do_espaco in dados.items():
    print(f' - {nome_chave} tem o valor {valor_dentro_do_espaco}')

#Desafio 93
'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionario, incluindo o total de gols feitos durante
o campeonato.
'''
#Resolucao 93

pasta_jogador = []
dados_jogador = {}
jogo = []

dados_jogador['nome'] = str(input('Nome: '))
jogos = int(input('Quantidade de jogos: '))
dados_jogador['jogos'] = jogos
for c in range (1, jogos+1):
    print(f'No jogo {c} total de gol(s): ')
    for cc in range(1):
        #jogo.clear()
        gol = int(input('>'))
        jogo.append(gol)
    dados_jogador['quantidade_gol'] = jogo
    total = sum(jogo)
    dados_jogador['total_gol'] = total

pasta_jogador.append(dados_jogador.copy())
print(pasta_jogador)

for k, n in dados_jogador.items():
    print(f' {k} = {n}')
    print('-='*10)
n = 0
for ccc in range (jogos):
    print(f'No jogo {ccc} o jogador {dados_jogador['nome']} fez {jogo[n]} gol(s).')
    n += 1


#Desafio 94
'''
Crie um programa que leia nome, sexo e idade de varias pessoas, guardando 
os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
No final, mostre:
a) Quantas pessoas firam cadastradas
b) A media de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da media
'''

#Desafio 95
'''
Aprimore o desafio #93 para que ele funcione com varios jogadores, incluindo 
um sistema de visualizacao de detalhes do aproveitamento de cada jogador.

'''





















