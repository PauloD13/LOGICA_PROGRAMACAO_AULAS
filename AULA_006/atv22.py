#SECTION - parte 1
import os
print('Ola usuário')
input('Aperte enter para avançar')
print('Você prefere ∇')
print('1 - Calcular a distancia')
print('2 - Informar a distancia')

#SECTION - Variaveis e Funções
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

opcao = int(input('Digite Qual opção voce prefere: '))

#SECTION - Codigo central
print('Obeservação: Use valores inteiro')
if opcao == 1:
    print('Entendido, então ∇')
    km_i = int(input('Informe a quilometragem do seu carro antes da viagem: '))
    km_f = int(input('Informe a quilometragem ao final do percurso: '))
    combs = int(input('Quantos litros de combustivel foram consumidos: '))
    km_g = km_f - km_i
    kml = km_g/combs

    input('Aperte enter para avançar')
    limpar()

elif opcao == 2:
    print('Perfeito, então ∇')
    km_g = int(input('Insira a distancia percorrida: '))
    combs = int(input('Insira os litros de combustivel consumido: '))
    kml = km_g/combs

    input('Aperte enter para avançar')
    limpar()

else:
    print("Opção invalida")
    print('Erro')

#SECTION - Central interna do codigo
print(f'Os valore foram de ∇')
print(f'{20*'='}VALORES{20*'='}')
print(f'Distancia: {km_g}Km')
print(f'Consumo: {combs}L')
print(f'Consumo proporcional; {kml:.2f}Km/L')
input('\nAperte enter para avançar')
limpar()

#SECTION - Final do codigo
limpar()
print('Obrigado por testar o codigo ;)')
input('Aperte enter para fechar o codigo')

SystemExit()
