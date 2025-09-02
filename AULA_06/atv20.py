import os
print('Ola usuário')

dist_metros = float(input('Digite a distancia em metros: '))

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
print('Um minuto, estamos calculando o valor')

centimetros = dist_metros *100
quilometros = dist_metros /1000

limpar()
print('Perfeito as distancias são de ∇')
print(f'{20*'='}CONVERSÕES{20*'='}')
print(f'Km: {quilometros}')
print(f'M: {dist_metros}')
print(f'Cm: {centimetros}')

input('\nAperte enter para avançar')

limpar()
print('Obrigado por testar o codigo ;)')
input('Aperte enter para fechar o codigo')

SystemExit()