contas = {}
proximo_numero = 1001

def exibir_dados():
    if not contas:
        print('Nenhuma conta encontrada!')
        return
    
    for numero, dados in contas.items():
        print()
        print(f'{20*'-'} Dados Bancários {20*'-'}')
        print(f'Conta: {numero}')
        print(f'Saldo: {dados['saldo']}')
        print(f'Cliente: {dados['nome']} | CPF: {dados['cpf']} ')
        print(f'{57*'-'}')
        print()

def criar_conta():
    global proximo_numero
    nome = input('Digite seu nome: ').strip()
    cpf = input('Digite seu CPF: ').strip()
    contas[proximo_numero] = {'nome':nome, 'saldo':0.0, 'cpf':cpf}
    print(f"Conta criada com sucesso! Número da conta: {proximo_numero}")
    proximo_numero +=1

def depositar():
    numero = int(input('Digite o número da conta: '))
    if numero in contas:
        valor = float(input('Digite o valor que deseja depositar: ').replace(',','.'))
        contas[numero]['saldo'] += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')
    else:
        print('Conta não encontrada!')

def sacar():
    numero = int(input('Digite o número da conta: '))
    if numero in contas:
        valor = float(input('Digite o valor que deseja sacar: ').replace(',','.'))
        if valor <= contas[numero]['saldo']:
            contas[numero]['saldo'] -= valor
            print(f'Saque de {valor:.2f} realizado com sucesso!')
        else:
            print('Saldo insuficiente!')
    else:
        print('Conta não encontrada!')

def encerrar_conta():
    numero = int(input('Digite o número da conta: '))
    if numero in contas:
        del contas[numero]
        print('Conta encerrada!')
    else:
        print('Conta não encontrada!')

def menu():
    print(f'{40*'-'} Sistema Bancário {40*'-'}')
    print(f'1. Criar Cc')
    print(f'2. Exibir dados')
    print(f'3. Depositar')
    print(f'4. Sacar')
    print(f'5. Encerrar conta')
    print(f'6. Sair')

    opcao = input('Digite a opção desejada: ')

    return opcao