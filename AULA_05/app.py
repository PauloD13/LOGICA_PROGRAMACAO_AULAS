while True:
    try:
        #entrada de dados
        etanol = float(input('Digite o preço do etanol: ').replace(',','.'))
        gasolina = float(input('Digite o preço da gasolina').replace(',','.'))
        calculo = (etanol/gasolina)*100
        resultado = "Gasolina" if calculo > 70 else 'Etanol'
        
        #resposta do calculo
        print(f'Nesse momento o idela é abastecer com {resultado}.')
        print(f'Descisão com base no resultado: {calculo:.2f}%.')

        opcao = input('Deseja repetir o calculo? (s/n)').lower().strip()
        match opcao:
            case 's':
                continue
            case 'n':
                break
            case _:
                print(f'Opção inválida')

    except Exception as e:
        print(f'Não foi possível fazer a')

        SystemExit