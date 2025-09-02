import os
import json

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

apelido = None
senha = None
entrada = None
conta = None
saldo = None
cad_pf = None
renda_anual = None
nome_comp = None

def criar_c():
    limpar()
    global conta
    global nome_comp
    if conta != 1:
        print('Os seguintes dados serão necessários')
        print('Nome Completo: Nome sobrenome1 sobrenome2... \nData de nascimento: dd_mm_aaaa \nCPF: 00011122234 \nRenda anual: R$xxxx,xx')

        global cad_pf
        global renda_anual
        print(10*'=','Preencha os dados',10*'=')
        nome_comp = input('Nome completo: ')
        dt_nasc = input('Data de nascimento: \nUltilize esse formato dd_mm_aaaa\n')
        cad_pf = str(input('CPF: '))
        renda_anual = float(input('Renda anual: R$').replace(',','.'))

        global apelido
        global senha
        global saldo
        saldo = 0.0
        apelido = input("Como gostaria de ser Chamado \nUse apenas um termo: Ex: Eduardo \n")
        senha = int(input('Crie uma senha numerica: '))
        conta = 1
        input('Conta criada com sucesso')
    else:
        print('Já existe uma conta')
        input(f'A conta esta no CPF: {cad_pf}')
    return nome_comp

def login():
    limpar()
    global apelido
    global senha
    global entrada
    print('Faça o login para continuar')
    user = input('Informe o usuario: ')
    passe = int(input('Informe sua senha numérica: '))

    if passe == senha and user == apelido:
        entrada = 1
        print('Login validado')
    else:
        entrada = 0
        print('Login Inválido')

def deposit():
    global saldo
    limpar()
    print('Seu saldo é de: R$', saldo)
    deposito = float(input('Informe o valor do deposito: R$'))
    saldo += deposito
    input(f'Deposito de R${deposito} feito com sucesso.')
def sacar():
    global saldo
    limpar()
    print(f'Seu saldo atual é de: {saldo}')
    saque = float(input('Quanto você deseja sacar? R$'))
    if saque <= saldo:
        saldo -= saque
        print(f'Saque de R${saque} efetuado com sucesso')
        input(f'Seu saldo é de R${saldo}.')
    else:
        print('Saldo insuficiente')
        input()
def extrat():
    global saldo
    limpar()
    print(15*'=','Dados',15*'=')
    print(f'Nome: {nome_comp}')
    print(f'CPF: {cad_pf}')
    print(f'Renda Inf: {renda_anual}')
    print(f'Saldo: R${saldo}')
    print(40*'=')
    input('Aperte Enter para avançar')

def cancel():
    global saldo
    if saldo > 0:
        print('Para encerrar a conta saque o valor primeiro')
        print(f'Saldo: R${saldo}')
        return
    else:
        print('Encerrando conta')
        SystemExit
def menu():
    #menu principal
    limpar()
    print(50*'=','Menu Principal',50*'=')
    print('1 - Criar conta')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Extrato')
    print('5 - Cancelar conta')
    print('0 - sair')
    print('101 - Teste')
    opcao = int(input('digite a opcao desejada: '))
    return opcao

#iniciando o menu principal
while True:
    match menu():
        case 1:
            criar_c()
        case 2:
            login()
            if entrada == 1:
                deposit()
            else:
                input('Acesso bloqueado')
                continue
        case 3:
            login()
            if entrada == 1:
                sacar()
            else:
                input('Acesso bloqueado')
                continue
        case 4:
            login()
            if entrada == 1:
                extrat()
            else:
                input('Acesso bloqueado')
                continue
        case 5:
            login()
            if entrada == 1:
                cancel()
            else:
                input('Acesso bloqueado')
                continue
            break
        case 0:
            print('Saindo do aplicativo')
            break
        case 101:
            ...

SystemExit(print('Sistema encerrado'))