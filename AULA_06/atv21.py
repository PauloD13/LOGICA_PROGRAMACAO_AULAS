#SECTION - parte 1
import os
print('Ola usuário')
input('Aperte enter para avançar')

#SECTION - Variaveis e Funções
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
horas = float(input('Informe um valor em horas: '))
minutos = horas*60
segundos = minutos*60

#SECTION - Codigo central e print dos valores
print(f'{horas}horas, são equivalentes a ∇')
print(f'{20*'='}VALORES{20*'='}')
print(f'Horas: {horas}h')
print(f'Minutos: {minutos}m')
print(f'Segundos: {segundos}s')

#SECTION - Central interna do codigo
input('\nAperte enter para avançar')
limpar()

#SECTION - Final do codigo
limpar()
print('Obrigado por testar o codigo ;)')
input('Aperte enter para fechar o codigo')

SystemExit()