#SECTION - parte 1
import os
print('Ola usuário')
input('Aperte enter para avançar')
print(f'{20*'='}User{20*'='}')
print('1 - Gomes')
print('2 - Cesar')

#SECTION - Variaveis e Funções
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

usuario1 = {
    'nome' : 'Gomes',
    'idade' : 26,
    'email' : 'gomes@gmail.com'
}

usuario2 = {
    'nome' : 'Cesar',
    'idade' : 2000,
    'email' : 'cesar@gamil.com'
}

user = int(input('Qual usuario voce é: '))
limpar()
#SECTION - Codigo central
match user:
    case 1:
        print('Nos temos o seguintes dados disponíveis')
        print(f'Nome: {usuario1['nome']}' )
        print(f'Idade: {usuario1['idade']}')
        print(f'Email: {usuario1['email']}')
    case 2:
        print('Nos temos o seguintes dados disponíveis')
        print(f'Nome: {usuario2['nome']}' )
        print(f'Idade: {usuario2['idade']}')
        print(f'Email: {usuario2['email']}')
    case _:
        print('Usuario inexistente')
        print('Dados indisponiveis')

#SECTION - Central interna do codigo
input('\nAperte enter para avançar')
limpar()

#SECTION - Final do codigo
limpar()
print('Obrigado por testar o codigo ;)')
input('Aperte enter para fechar o codigo')

SystemExit()
