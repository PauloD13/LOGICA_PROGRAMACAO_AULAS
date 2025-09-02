#SECTION - definindo as variaveis diretas
nome_autor = "Paulo Demeris"
cidade_orig = "Brasília-DF"
cidade_2 = "Taguatinga"
idade = 16
ano_nasc = 2008
saudacao = "Hello everyone!"

#SECTION - execuntando o print com as informações
print(80*"=") #NOTE - moldura decorativa
print(saudacao,"\nEu me chamo",nome_autor)
print("Eu venho da cidade de",cidade_orig,"mais especificamente de",cidade_2)
print("Tenho",idade,"anos de idade e sou de",ano_nasc)
print(80*"=")

#SECTION - Variaveis para print(type())
nome = "Nome"
idade = 18
altura = 1.80
ativo = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(ativo))

#SECTION - Operadores e variaveis
print(34*"=","operadores",34*"=")
num1 = 48
num2 = 25

soma = num1+num2
div = num1/num2 #NOTE - Divisão real
div2 = num1//num2 #NOTE - Divisão inteira
multi = num1*num2
sub = num1-num2
expo = num1**num2
resto = num1 %25 #NOTE - Resto da divisão inteira

print('O resultuda da soma',num1,'+',num2,'é:',soma)
print('O resultuda da subtração',num1,'-',num2,'é:',sub)
print('O resultuda da divisão',num1,'/',num2,'é:',div)
print('O resultuda da divisão inteira de',num1,'/',num2,'é:',div2)
print('O resto da divisão inteira é:',resto)
print('O resultuda da multiplicação',num1,'*',num2,'é:',multi)
print('O resultado da potência',num1,'^',num2,'é:',expo)

print(80*'=')

#SECTION - Operadores de Comparação
#NOTE - Operadores possiveis de comparar
'''
num1>num2 1 maior que 2
num1<num2 1 menor que 2
num1==num2 2 passa a valer 1
num1>=num2 
num1<=num2
num1!=num2
'''

ano=2025 #NOTE - O valor é atribuido e printado no console na linha abaixo
print('Ano atual',ano)
ano+=1 #NOTE - O valor sofre uma alteração na linha sucessiva ao primeiro print e retorna com o valor atualizado no print a seguir
print('Ano acrescido de +1',ano)
ano-=1 #NOTE - O valor novamente é alterado e printado no momento seguinte a alteração
print('Ano decrementado de -1',ano) #REVIEW - Esse comportamento expõe um comportamento ordenado de execução linha a linha, onde o valor pode ser alterado depois de se executado com um valor diferente na linha anterior
#!SECTION - Operadores Logicos #NOTE - AND, OR, NOT

#SECTION - Input de dados
print(30*'=','Entrada de dados',30*'=')

#NOTE - Recebendo o input de um dado(nome de usuaruio) e atribuindo esse valor a uma variavel
nome_usuario=input("Digite o seu nome:")
#NOTE - Recuperando esse dado e utilizando ele no retorno(print)

print('Welcome to the piton system', nome_usuario)

#NOTE - recebendo o input do ano nascimento
ano_nascimento = input("Digito o ano do seu nascimento ")
print(type(ano_nascimento)) #NOTE - testando o tipo do valor (deve ser strg)
ano_nascimento = int(ano_nascimento) #NOTE - Covertendo strg em int
print(type(ano_nascimento)) #NOTE - testando o tipo do valor

ano_at = input("Digite o ano atual ")#NOTE - Recebendo input do ano atual
ano_at = int(ano_at) #NOTE - Covertendo strg em int
idade_at = ano_at-ano_nascimento #NOTE - Calculando o valor para chegar na idade
print('Sua idade é',idade_at,'anos')#NOTE - Devolvendo o valor da idade

print(80*'=')

#SECTION - Testando funcionalidades

#NOTE - Coletando os dados pessoais
inicio = input('Digite seu nome: ')
cpf = input('Digite o seu CPF: ')
telefone = input('Digite o seu número de celular: ')
email 
print(20*'=', "Dados Pessoais", 20*"=")
print('Nome: ', inicio)
print('CPF: ', cpf, '| Telefone', telefone)
print(80*'=')