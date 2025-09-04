import json
import os

from func import menu1, ler, exit
#função para limpar o console
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')


#ciclo de repetição
while True:

    #match case de qual foi a opção escolhida
    match menu1():
        case 1:
            ler()
        case 2:
            ler()
        case 3:
            ler()
        case 4: # caso sair do sistema
            ler()
        case 5: #caso de segurança de opcao invalida
            break
SystemExit(print('Sistema encerrado'))