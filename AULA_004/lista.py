'''listas sao variaveis compostas que armazenam varios valores
em uma unica variavel
'''
#AVISO: por causa de repeticoes, coloque as partes que voce nao quer usar em comentarios

#criando a lista
nome_lista = ['ana', 'marcos', 'maria', 'baltazar', 'tanaka', 'dandara', 'samara']
#exibindo a lista
for nome in nome_lista:
    print(nome)
#percorrenndo a lista com o for/contador
for i in range(len(nome_lista)):
    print(f'{i + 1}º nome da lista: {nome_lista[i]}')
#operador in
#verifica de um elemento esta na lista
nome = input('digite seu nome: ')
if nome in nome_lista:
    print(f'{nome} esta na lista, parabens!')
else:
    print(f'{nome} nao esta na lista, desculpe.')
#verificando o tamanho da lista
print(f'A lista possui {len(nome_lista)} nomes')
#index, é o indice do elemento na lista
#isto é, o numero da posicao do elemento na lista
nome = input('digite o nome que deseja buscar: ')
indice = nome_lista.index(nome)
try:
    print(f'O nome {nome} encontrado no indice {indice}')
except:
    print(f'O nome {nome} nao foi encontrado na lista')
#count, conta quantas vezes o elemento aparece na lista
nome = input('digite o nome que deseja contar: ')
qtd = nome_lista.count(nome)
try:
    print(f'O nome {nome} aparece {qtd} vezes na lista')
except:
    print(f'O nome {nome} nao foi encontrado na lista')
#alterando dados de uma lista
nome_lista[0] = 'alexandre'
print(f'Lista alterada: {nome_lista}')
#alterando com input do user
nome_alt = input('digite o nome que deseja alterar: ')
nome_lista[nome_lista.index(nome_alt)] = input(' digite o novo nome: ')
for nome in nome_lista: 
    print(nome)

#IMPORTANDO BIBLIOTECAS
import os
from time import sleep
cont = input(' digite um numero inteiro: ')
try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f'contagem regressiva: {cont_int}')
        sleep(1)
        cont_int -= 1
except:
    print('Digite um numero inteiro valido')
print('Contagem finalizada!')

#RANDOM
import random
#escolhendo um nome aleatorio de uma lista
nome1 = input('digite o primeiro nome: ')
nome2 = input('digite o segundo nome: ')
nome3 = input('digite o terceiro nome: ')
nome4 = input('digite o quarto nome: ')
nome5 = input('digite o quinto nome: ')
lista = [nome1, nome2, nome3, nome4, nome5]
escolhido = random.choice(lista)
print(f'O nome escolhido foi: {escolhido}')