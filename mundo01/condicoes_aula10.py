#condicoes
# if, elif, else
#estrutura condicional simples (só o if)
#estrutura condicional composta(if,else)

nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
else:
    print('Seu nome é tao normal...')
print('Bom dia, {}'.format(nome))


n1 = float(input('Digite sua nota no P1: '))
n2 = float(input('Digite sua nota no P2: '))
media = (n1+n2)/2
if media >= 6:
    print('Sua media foi {:.2f}, você passou!'.format(media))
    print('Parabéns!!! ')

else:
    print('Sua media foi {:.2f}, abaixo do que é aceitavel.'
          ' Você não passou!'.format(media))
    print('Estude mais!')

# OU PODERIA SER ESCRITO DA SEGUINTE MANEIRA
# CONDICAO SIMPLIFICADA
m1 = float(input('Digite sua nota no P1: '))
m2 = float(input('Digite sua nota no P2: '))
mmedia = (m1+m2)/2
print('A sua média foi {:.2f}'.format(mmedia))
print('PARABENS' if media >= 6 else 'Estude mais!')