import json
import os

#variaveis
usuarios = []
novo_arquivo = ''

#função para limpar o console
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#ciclo de repetição
while True:
    #chamando a variavel
    usuario = {}

    #menu de opções
    print('1 - Cadastrar novo usuário')
    print('2 - Salvar arquivo JSON')
    print('3 - Fazer leitura JSON')
    print('4 - Sair do sistema')

    #opção do usuario
    opcao = int(input('Informe o número da opção desejada: '))
    limpar()

    #match case de qual foi a opção escolhida
    match opcao:
        case 1:
            #input das informações para o arquivo json
            usuario['nome'] = input('Informe o nome do usuário: ').strip().title()
            usuario['idade'] = int(input('Informe a idade do usuário: ').strip())
            usuario['email'] = input('Informe o email do usuário: ').strip().lower()
            
            #salvando os dados e finalizando o caso
            usuarios.append(usuario)
            limpar()
            print('Usuário cadastrado com sucesso!')
            continue

        case 2:
            #criando o arquivo json
            novo_arquivo = input('Informe o nome do arquivo: ').strip().lower()
            with open(fr'C:\Users\ead\Documents\LOGICA_PROGRAMACAO_AULAS\AULA_06\{novo_arquivo}.json', 'w', encoding='utf-8') as f:
                #variaveis a escrever no arquivo
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            limpar()
            print('Arquivo salvo com sucesso!')
            continue

        case 3:
            #solicitando leitura do arquivo
            #checando se um arquivo já foi criado
            if not novo_arquivo:
                novo_arquivo = input('Digite o nome do arquivo: ').strip().lower()
            #abrindo o arquivo
            with open(fr'C:\Users\ead\Documents\LOGICA_PROGRAMACAO_AULAS\AULA_06\{novo_arquivo}.json', 'r', encoding='utf-8') as f:
                dados = json.load(f)
                #carregando os dados e exibindo na tela
            print(f'{'='*45} USUÁRIOS {'='*45}')
            #ciclo de repetição para gravar todos os nomes na tela
            for usuario in dados:
                for chave in usuario:
                    print(fr'{chave.capitalize()}: {usuario.get(chave)}')
                print('='*100)

                #tabela para exibir o proximo nome
                input('Aperte enter para avançar')
                limpar()
                print(100*'=')
            
            #tabela para permitir o avanço do codigo
            limpar()
            input('Aperte enter para sair')
            limpar()

        case 4: # caso sair do sistema
            print('Saindo do sistema...')
            print('Aguarde...')
            print('Aguarde...')
            break

        case _: #caso de segurança de opcao invalida
            print('Opção inválida')
            limpar()
            print('Escolha uma opção abaixo')
            continue

SystemExit(print('Sistema encerrado'))