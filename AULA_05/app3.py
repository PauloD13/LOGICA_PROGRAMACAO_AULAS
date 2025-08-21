import os

while True:
    try:
        novo_texto = input('Digite o texto \n')
        nome_arquivo = input('Digite o nome do arquivo, (Sem extensão): ').strip()

        with open(fr'C:\Users\ead\Documents\LOGICA_PROGRAMACAO_AULAS\AULA_05/{nome_arquivo}.txt','w', encoding='utf-8') as f:
            f.write(novo_texto)

        os.system('cls' if os.name == "nt" else 'clear')
        print(fr'{nome_arquivo}.txt, gravado com sucesso')

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