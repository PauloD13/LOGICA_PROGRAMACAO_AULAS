#SECTION concatenação com +

'''
#concatenação com +
nome = "Juninho"
idade = 23
altura = 1.70

#saida de dados
print('Olá meu nome é ' + nome + ' e eu tenho ' + str(idade) + ' anos de idade')

#concatenação com ,
print('Olá, meu nome é', nome,'e tenho', idade, 'anos de idade')

#concatenação com format
print('Olá, meu nome é {} e tenho {} anos de idade'.format(nome,idade))

#concatenação com f-string
print(f'Olá, meu nome é {nome} e tenho {idade} anos de idade')
'''
"""
#eliminando quebra de linha. o end='' exerce a função de um juntador de linhas
print('firulei firuflei ', end='')
print('leiflu fleilu.')
texto no console será: firulei firuflei leiflu fleilu.'
"""
'''
valor = 1.23456789
#exibindo o valor com duas casas depois da virgula
print(f'{valor:.2f}')
#omitindo o valor de depois da segunda casa depois da virgula
#2f signica que serão exibidas duas casas depois da virgula
'''

'''
print(30*'=') #decorativo
peso = input('Digite seu peso: ').replace(',','.') #O codigo .replace diz que, sempre que for digitada uma virgula no codigo ela sera convertida pra um ponto. visando evitar quebras no codigo dessa forma se o usuario digitar o peso como 55,5 ou 55.5,o resulta vai ser coerente par ao codigo
#solicitando a interação do usuario e coletando o valor
peso = float(peso)
#convertendo a string em float, isto é, numeros reais
print(f'Peso: {peso:.2f}Kg'.replace('.',','))
#imprimindo uma string no console devolvendo o valor do peso, simplificado, ou seja, limitada a duas casas depois da virgula. ex 77,89023 => 77,89, ou 77 => 77.00
'''

'''
#definindo variaveis
bom_dia = "Olá usuário, Bom dia!" 
pi = 3,14159265
pontos = 80
ativo = True

#printando uma string com as variaveis e testando o tipo de cada uma
print(f'{bom_dia}, atualmente sua pontuação é de {pontos*pi}, continua assim!')
print(type(pi)) #float
print(type(pontos)) #int
print(type(ativo)) #bool
print(type(bom_dia)) #tuple

#calculando os valores
res1 = 12+7
res2 = 15%4
res3 = 3**2

#imprimindo os resultados
print(f'12+7 = {res1}')
print(f'15/100*4 = {res2}')
print(f'3^2 = {res3}')

print(f'{bom_dia}')
username = input('Por favor, digite um nome de usuário: ')

print(f'{bom_dia}'.replace('usuário',username))

val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))
res4 = val1*val2
print(f'O resultado da multiplicação desses numeros é {res4}')
'''
'''
val1 = input('Digite um valor: '))
val1 = int
res4=val1*2
print(Esse valor multiplicado por 2 resulta em: res4)
'''