import os

while True:
    try:
        arquivo = input('Digite o nome do arquivo (Sem extensão): ').strip().lower()
        #nome do arquivo informado pelo user

        #abrindo o arquivo
        with open(f'{arquivo}.txt', 'r', encoding='utf-8') as f:
            arquivoaberto = f.read()
        os.system('cls' if os.name == 'nt' else 'clear')

        #encontrar os arquivos
        print(arquivoaberto)

#loop drepetição para ler mais de um arquivo
        while True:
            prosseguir = input('Deseja abrir outro arquivo? (s/n)').lower().strip()
            #condições de repetição
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('Opção Inválida')
                continue
            #match case para avaliar a resposta s para ler outro arquivo n para parar o codigo
        match prosseguir:
            case 's':
                continue
            case 'n':
                print('Fechando sistema...')
                print('...')
                print('...')
                break

    #caso o codigo não consiga ler o arquivo ele devolve um report de erro
    except Exception as e:
        print(f'Não foi possível abrir o arquivo {e}')

#finalizando o codigo
SystemExit(print('Código encerrado'))