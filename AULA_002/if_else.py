'''
#coletando o nome e a idade
nome = input("Digite o seu nome: ")
idade = int(input('Digite a sua idade: '))

#testando se o caso é
print('Você está fora do bloco IF ELSE') #coments para leitura da execução do codigo
if idade >= 18: # maior de idade
    print('Você é maior de idade')
    print('VocÊ está dentro do bloco IF')#coments para leitura da execução do codigo
else: #menor de idade
    print('Você é menor de idade')
    print('Você está dentro do bloco ELSE')#coments para leitura da execução do codigo
print('Você está fora da estrutura condicional IF ELSE')#coments para leitura da execução do codigo
'''

'''
num1 = int(input('Digite um numero inteiro'))
#coletando o numero

#descobrindo se o numero e para ou impar e devolvendo a resposta a partir do caso em questão
if num1 %2 ==0:
    print('Isto é um número par')
else:
    print('Isto é um número impar')
'''

'''
print(30*'=','BOLETIM ESCOLAR',30*'=')

nome_aluno = input('Informe o nome do aluno: ').upper()

#coletnado variaveis basicas nome e notas

nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))
nota3 = float(input('Qual foi a terceira nota? '))
nota4 = float(input('Qual foi a quarta nota? '))

#descobrindo a media
media = (nota1+nota2+nota3+nota4)/4

Testando a situação
if media >= 7: #nota maior ou igual a 7 resulta em caso aprovado
    print(35*'=')
    print(f'{nome_aluno}: Aprovado')
    print(f'1° Nota: {nota1} | 2° Nota: {nota2}')
    print(f'3° Nota: {nota3} | 4° Nota: {nota4}')
    print(35*'=')
    print(f'Media: {media}')
    print(35*'=')

elif media >= 5: #se a nota e menor que 7 e maior ou igual a 5 o caso é recuperação
    print(35*'=')
    print(f'{nome_aluno}: Em recuperação')
    print(f'1° Nota: {nota1} | 2° Nota: {nota2}')
    print(f'3° Nota: {nota3} | 4° Nota: {nota4}')
    print(35*'=')
    print(f'Media: {media}')
    print(35*'=')

else:
    print(35*'=') #se nenhum dos casos é verdadeiro então automaticamento o caso reprovação é acionado
    print(f'{nome_aluno}: reprovado')
    print(f'1° Nota: {nota1} | 2° Nota: {nota2}')
    print(f'3° Nota: {nota3} | 4° Nota: {nota4}')
    print(35*'=')
    print(f'Media: {media}')
    print(35*'=')    
'''
'''
#variaveis
nome = input('Qual seu nome? ')
idade = int(input('Qual a sua idade? '))
altura = float(input('Qual a sua altura(M)? ').replace(',','.'))

#condições
if idade >= 60:
    print('Entrada negada') #caso positivo de idade excessiva resulta em entrada negada
    print('Prezamos pela segurança do parque')
    print('Por isso não permitimos a entrada de pessoas em grupo de risco')
    print(f'Lamentamos a situação {nome}')
elif idade >= 16 and altura >= 1.45: #caso positivo para altura minima e idade minima, resulta em entrada permitida
    print('Entrada permitida')
    print(f'Seja Bem-Vindo senhor {nome}')
else: #caso negativo para altura, ou idade minimos, ou caso negativo para ambos simultaneamente resulta em entrada negada
    print('Entrada Negada')
    print('Você não atende aos requisitos')
    print('Lamentamos a situação')
'''

#variveis
nome = 'Fe!n'
idade = 19

#operadores
print(nome, "é maior de idade" if idade>=18 else 'é menor de idade')