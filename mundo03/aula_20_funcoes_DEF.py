'''
def soma(a,b):
    s = a + b
    print(s)
'''
#a = 4
#b = 5
#s = a + b
#print(s)
'''

#programa principal

soma(4,5)
soma(b=1, a=7)
'''
# EMPACOTAR PARAMETROS
# COM TUPLAS
'''
def contador(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e sao {tamanho} numeros. ')
    for valor in num:
        print(f'{valor} ', end='')
        print('fim.')


contador(8,7,6,5,4)
contador(1,2,3)
'''
# COM LISTAS
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 # DOBRAR O TAMANHO
        pos += 1


valores = [1,2,3,4,5]

dobra(valores)
print(valores)
'''


# DESEMPACOTAMENTOS
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}. ')

soma(5,2)
soma(4,3,5)

















