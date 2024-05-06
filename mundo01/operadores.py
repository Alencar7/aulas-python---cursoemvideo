n1 = int(input('um valor:'))
n2 = int(input('um valor:'))
print(' a soma deu {}'.format(n1+n2))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma e '.format(s), end=' ')
print('a multip deu {}, '
      'a divisao deu {:.3f}, '
      'a divisao inteira deu {} e '
      'a exp deu {}'.format(m, d, di, e))
# {:.3f} divisao com ponto flutuante
