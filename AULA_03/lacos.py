'''problema: crie um sistema que calcule o indice de massa corporal (IMC) do usuário, mostre o valor
do IMC na tela, retorne se o usuário estiver no peso ideal ou precisa emagrecer ou engordar.
Utilize a tabela do IMC para definir os valores
imc = peso / (altura²)
18,5'''
'''
if opcao == 's':
    continue
elif opcao == 'n':
    print('Saindo do sistema')
    break
else:
    print('Sem resposta, saindo do sitema')
    SystemExix

'''

#LAÇOS
#laços são estruturas de repetição, ou seja, executam um bloco de código várias vezes
#existem 3 tipos de laços: while, continue

num = 10
while num >= 0:
    print(num)
    num -= 1 

#iniciando o menu principal
while True:
    #menu principal
    print(50*'=','sistema console 2º ds',50*'=')
    print('1 - calculadora IMC')
    print('2 - maioridade')
    print('3 - calculadora simples')
    print('4 - dados pessoais')
    print('5 - arvore de natal')
    print('0 - sair')
    opcao = input('digite a opcao desejada: ')

#SECTION - executando a calculadora de IMc
    if opcao == '1':
        while True: #iniciando outro ciclo de repetição
            print(30*'=','calculadora IMC',30*'=')
            #SECTION - variaveis
            altura = float(input('digite a sua altura: ').replace(',','.'))
            peso = float(input('digite seu peso: ').replace(',','.'))
            imc = peso / (altura ** 2)
            #SECTION - imprimindo o valor do do resultado na tela
            print()
            print(f'Seu IMC é: {imc:.2f}')

            #SECTION - condição do valor resultado para casa resultado
            if imc <= 18.5:
                print('Abaixo do normal')
            elif imc <= 24.9:
                print('Peso Normal')
            elif imc <= 29.9:
                print('Sobrepeso')
            elif imc <= 34.9:
                print('Obesidade grau I')
            elif imc <= 39.9:
                print('Obseidade grau II')
            else:
                print('Obesidade grau III')

            #bloco de interação
            opcao = input('Deseja calcular novamente? s/n: ').lower()

            #condições de repetição
            if opcao == 's':
                continue
            elif opcao == "n":
                print('Sainda da calculadora')
                break
            else:
                print('Erro, Voltando para o menu')
                break

    elif opcao == '2':
        #MAIORIDADE
        print(50*'=','MAIORIDADE',50*'=')
        #definindo as variaveis
        ano = 2025
        nasc = int(input('digite seu ano de nascimento: '))
        idade = ano - nasc
        #condições para devolver o valor
        if idade >= 18:
            print('voce é maior de idade')
        else:
            print('voce é menor de idade')
        #solicitando a interação do usuario
        input('Aperte qualquer tecla para voltar para o menu!')

    elif opcao == '3':
        #CALCULADORA SIMPLES
        while True: #ajustando condições de repetição
            print(50*'=','calculadora simples',50*'=')
            print('1 - soma')
            print('2 - subtração')
            print('3 - multiplicação')
            print('4 - divisão')
            print('Aperte Enter para voltar')
            #solicitando a interação para coletar a variavel
            op_calc = input('digite a operacao desejada: ')
            if op_calc == "": #condição para interrupção do condigo de imediato
                break
            n1 = float(input('digite o primeiro numero: ').replace(',', '.'))
            n2 = float(input('digite o segundo numero: ').replace(',', '.'))
            #condições de execução de cada operação
            if op_calc == '1':
                print(f'a soma de {n1} e {n2} é: {n1 + n2}')
            elif op_calc == '2':
                print(f'a subtração de {n1} e {n2} é: {n1 - n2}')
            elif op_calc == '3':
                print(f'a multiplicação de {n1} e {n2} é: {n1 * n2}')
            elif op_calc == '4':
                print(f'a divisão de {n1} e {n2} é: {n1 / n2}')

            #interação para definir a repetição ou não do codigo
            input('Deseja continuar? s/n: ').lower().replace('Sim','3').replace('Não','n').replace('s','3')
            if opcao == '3':
                continue
            elif opcao == "n":
                print('Sainda da calculadora')
                break
            else:
                print('Erro, Voltando para o menu')
                break

    elif opcao == '4':
        #DADOS PESSOAIS
        #coletando as variaveis
        nome = input("digite seu nome: ")
        cpf = input("digite seu cpf: ")
        telefone = input("digite seu telefone: ")
        dt = input("digite sua data de nascimento: ")
        #devolvendo as variaveis
        print(100*'=')
        print(f'nome: {nome}')
        print(f'cpf: {cpf}')
        print(f'telefone: {telefone}')
        print(f'data de nascimento: {dt}')
        print(100*'=')

        input('Aperte qualquer tecla para voltar para o menu!')

    elif opcao == '5':
        ... #pular esse trecho
    elif opcao == '0': 
        #condição de encerramento do sistema
        print('Encerrando sistema')
        break
    SystemExit #interrompendo o script