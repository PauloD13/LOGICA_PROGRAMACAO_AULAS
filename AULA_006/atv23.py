#SECTION - parte 1
import os
print('Ola usuário')
input('Aperte enter para avançar')

#SECTION - Variaveis e Funções
print('Por favor, insira valores inteiros')
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
valor = int(input('Informe um valor negativo ou positivo: '))
limpar()

#SECTION - Codigo central

if valor >= 0:
    valor_a = valor
else:
    valor_a = -valor

#SECTION - Central interna do codigo
print('Valores Calculados')
input('\nAperte enter para avançar')
limpar()

#SECTION - Final do codigo
limpar()
print(f'{20*'='}VALORES{20*'='}')
print(f'O valor absoluto de: {valor} é {valor_a}')
print('Obrigado por testar o codigo ;)')
input('Aperte enter para fechar o codigo')

SystemExit()
