#aula 09
#analise        #transformacao      #juncao
frase = 'Curso em Video Python'
#3 ate o 12
print(frase[3:13])
#13 em diante
print(frase[13:])
#pulando de  em 2
print(frase[1:15:2])

print("""da pra escrever
qualquer coisa
assim
com 3 aspas duplas
""")

print(frase.upper().count('o'))

print(len(frase))

print(len(frase.strip()))

print(frase.replace('Python', 'Android')) #o replace nao muda a str, apenas o print!
#para SALVAR o resultado
#frase = frase.replace()

print('Curso' in frase)

print(frase.lower().find('video'))

dividido = frase.split()
print(dividido)

print(dividido[0][3]) #dividido 0 e mostrar a letra 3

"""

len(): Retorna o número de itens de um objeto.
count(): Conta quantas vezes um valor aparece numa sequência.
replace(): Substitui partes de uma string por outra string.
upper(): Converte todos os caracteres de uma string para maiúsculas.
lower(): Converte todos os caracteres de uma string para minúsculas.
capitalize(): Deixa a primeira letra de uma string em maiúscula.
title(): Converte a primeira letra de cada palavra para maiúscula.
strip(): Remove espaços em branco ou caracteres específicos do início e do fim de uma string.
join(): Combina os elementos de uma sequência numa única string, intercalados por um separador.

Funções de String:

find(): Retorna o índice da primeira ocorrência de um substring.
isalnum(): Verifica se todos os caracteres são alfanuméricos.
isalpha(): Verifica se todos os caracteres são apenas letras.
isdigit(): Verifica se todos os caracteres são dígitos.
isspace(): Verifica se todos os caracteres são espaços em branco.
startswith(): Verifica se a string começa com um substring específico.
endswith(): Verifica se a string termina com um substring específico.
split(): Divide a string em uma lista de substrings baseado em um separador.
rfind(): Retorna o índice da última ocorrência de um substring.
rjust(): Alinha a string à direita em um campo de um certo tamanho.
ljust(): Alinha a string à esquerda em um campo de um certo tamanho.
center(): Centraliza a string em um campo de um certo tamanho.
zfill(): Preenche a string com zeros à esquerda até um certo tamanho.

Funções de Lista:

append(): Adiciona um item ao final da lista.
extend(): Adiciona todos os elementos de uma lista (ou qualquer iterável) ao final da lista atual.
insert(): Insere um item em uma posição específica.
remove(): Remove o primeiro item encontrado na lista que tenha o valor especificado.
pop(): Remove o item em uma posição específica e o retorna.
clear(): Remove todos os itens da lista.
index(): Retorna o índice do primeiro item encontrado com o valor especificado.
count(): Conta quantas vezes um valor aparece na lista.
sort(): Ordena os itens da lista.
reverse(): Inverte a ordem dos itens da lista.
copy(): Retorna uma cópia da lista.

"""