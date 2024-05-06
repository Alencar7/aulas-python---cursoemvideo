#pedra > tesouta
#tesoura > papel
#papel > pedra

import random

jogo = ['pedra', 'papel', 'tesoura'] #a.pedra #b.papel #c.tesoura
escolha_automatica = random.choice(jogo)
#print(escolha_automatica)

print(f"\033[3;42mJogo da velha!\033[m")

escolha = str(input('Faca a sua escolha e jogue contra a maquina!\n'
                    'Escolha: \n '
                    '\033[1;31m(1)\033[m Pedra \n '
                    '\033[1;31m(2)\033[m Papel \n '
                    '\033[1;31m(3)\033[m Tesoura \n'                    
                    '\033[47mDigite um numero:\033[m '))
#print(escolha)
if ((escolha_automatica == 'pedra' and escolha == '1') or
        (escolha_automatica == 'papel' and escolha == '2') or
        (escolha_automatica == 'c' and escolha == '3')):
    print(f"O resultado deu empate!\nAmbos escolheram \033[1:33m{escolha_automatica}\033[m.")
#maquina ganha
elif escolha_automatica == 'pedra' and escolha == '3':
    print(f"A maquina ganhou! O resultado da maquina foi \033[1:33m{escolha_automatica}\033[m.")
elif escolha_automatica == 'papel' and escolha == '1':
    print(f"A maquina ganhou! O resultado da maquina foi \033[1:33m{escolha_automatica}\033[m.")
elif escolha_automatica == 'tesoura' and escolha == '2':
    print(f"A maquina ganhou! O resultado da maquina foi \033[1:33m{escolha_automatica}\033[m.")
#jogador ganha
elif escolha_automatica == 'pedra' and escolha == '2':
    print(f"Voce ganhou!!! O resultado da maquina foi \033[1:33m{escolha_automatica}\033[m.")
elif escolha_automatica == 'papel' and escolha == '3':
    print(f"Voce ganhou!!! O resultado da maquina foi \033[1:33m{escolha_automatica}\033[m.")
elif escolha_automatica == 'tesoura' and escolha == '1':
    print(f"Voce ganhou!!! O resultado da maquina foi \033[1:33m{escolha_automatica}\033[m.")
else:
    print(f"\033[31mResultado invalido. Tente novamente.\033[m ")
