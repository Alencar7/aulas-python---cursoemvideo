# Cores do Texto
print(' Cores do Texto:'
      '\n Vermelho: \033[31mTexto Vermelho\033[m ' # \033[31m \033[m
      '\n Verde: \033[32mTexto Verde\033[m ' # \033[32m \033[m
      '\n Azul: \033[34mTexto Azul\033[m'
      '\n Ciano: \033[36mTexto Ciano\033[m'
      '\n Magenta: \033[35mTexto Magenta\033[m'
      '\n Amarelo: \033[33mTexto Amarelo\033[m'
      '\n Preto: \033[30mTexto Preto\033[m'
      '\n Branco: \033[37mTexto Branco\033[m '
      '\n'
      )
# Estilos de Texto:
print(' Estilos de Texto:'
      '\n Negrito: \033[1mTexto em Negrito\033[m'
      '\n Itálico: \033[3mTexto em Itálico\033[m'
      '\n Sublinhado: \033[4mTexto Sublinhado\033[m'
      '\n Inversão de Cores: \033[7mTexto com Cores Invertidas\033[m'
      '\n'
      )

# Cores de Fundo:
print('Cores de Fundo: '
      '\n Fundo Preto: \033[40mTexto com Fundo Preto\033[m'
      '\n Fundo Vermelho: \033[41mTexto com Fundo Vermelho\033[m'
      '\n Fundo Verde: \033[42mTexto com Fundo Verde\033[m'
      '\n Fundo Amarelo: \033[43mTexto com Fundo Amarelo\033[m'
      '\n Fundo Azul: \033[44mTexto com Fundo Azul\033[m'
      '\n Fundo Magenta: \033[45mTexto com Fundo Magenta\033[m'
      '\n Fundo Ciano: \033[46mTexto com Fundo Ciano\033[m'
      '\n Fundo Branco: \033[47mTexto com Fundo Branco\033[m'
      'n'
      )

nome = 'Adriano'
print(f"A maquina ganhou! O resultado da maquina foi \033[7;29m {nome} \033[m.")

print('Ola, {} {} {}, e um prazer te conhecer!'.format('\033[4;34m', nome, '\033[m)'))
#posso criar variaveis para nao ficar colocando \033[m sempre!
#organizar cores
nome = 'Adriano de Alencar'
cores = {'limpa': '\033[m',
         'azul': '\0333[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:29m'}
print('ola! muito rpazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))