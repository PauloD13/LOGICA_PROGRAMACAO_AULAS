from funcoes import menu, criar_conta, exibir_dados, depositar, sacar, encerrar_conta

while True:
    match menu():
        case '1':
            criar_conta()
        case '2':
            exibir_dados()
        case '3':
            depositar()
        case '4':
            sacar()
        case '5':
            encerrar_conta()
        case '6':
            print('Saindo do Sistema...')
            break
        case _:
            print('Opção inválida')
            continue
print('Programa Finalizado')