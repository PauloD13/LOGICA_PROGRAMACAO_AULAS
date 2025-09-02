'''mini atividade de adivinhacao'''
#importando lib
from random import randint
print('tente adivinhar o numero!')
n1 = int(input('digite um numero de 1 a 10: '))
ns = randint(1, 10)
if n1 == ns:
    print('parabens, voce acertou!')
else:
    print(f'voce errou, o numero era {ns}')

#nivel elevado do mesmo exercicio
import random
nsc = random.randint(1, 10)
tentativas = 0
maxtentativas = 3
acerto = False
print(50*'-','bem vindo ao jogo de adivinhacao','-'*50)
print(f'voce tem {maxtentativas} tentativas para acertar o numero de 1 a 10')

while tentativas < maxtentativas:
    try:
        #entrada do usuario
        palpite = int(input('digite seu palpite: '))
    except:
        print('digite um numero inteiro valido')
        continue
    tentativas += 1

    #verificar palpite
    if palpite == nsc:
        acerto = True
        print(f'parabens, voce acertou o numero {nsc}')
        break
    elif palpite < nsc:
        print('tente um numero maior')
    else:
        print('tente um numero menor')
if acerto:
    print(f'voce acertou em {tentativas} tentativas, parabens!')
else:
    print(f'voce nao acertou, o numero era {nsc}, sinto muito, voce sera morto em')
    import os
    from time import sleep
    cont = 5
    try:
        cont_int = int(cont)
        while cont_int >= 0:
            os.system('cls')
            print(f'errou, voce sera morto por um sniper em: {cont_int} :)')
            sleep(1)
            cont_int -= 1
    except:
        print('nao morreu')

