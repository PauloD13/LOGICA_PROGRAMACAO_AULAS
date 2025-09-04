import json
import os

#variaveis
#temas
#filmes = {}
    #SECTION variaveis de filme
    #filme_nome
    #filme_sessão
    #filme_preço
    #!SECTION fim da variavel
#marcas = {}
    #SECTION ariaveis de marca
    #marca_nome
    #marca_produto
    #marca_avaliação
    #!SECTION fim da variavel
#carros = {}
    #SECTION ariaveis de carros
    #carro_modelo
    #carro_marca
    #carro_categoria
    #!SECTION fim da variavel
Animais = {}
    #SECTION variaveis de animais
    #animal_nome
    #animal_nome_cientifico
    #animal_domestico s/n
    #!SECTION fim da variavel
#temas = [filmes, marcas, carros, animais]
opcao1 = None

#função para limpar o console
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def menu1():
    print(f'{40*'='} Enciclopédia {40*'='}')
    print(f'1. Animais')
    print(f'2. Marcas')
    print(f'3. Carros')
    print(f'4. Filmes')
    print(f'5. sair')
    print(f'{90*'='}')

    opcao = int(input('Digite a opção desejada: '))

    global opcao1
    match opcao:
        case 1:
            opcao1 = Animais
        case 2:
            ... #opcao1 = marcas
        case 3:
            ... #opcao1 = carros
        case 4:
            ... #opcao1 = filmes

    return opcao

def ler():
    #solicitando leitura do arquivo
        #abrindo o arquivo
    with open(fr'C:\Users\ead\Documents\LOGICA_PROGRAMACAO_AULAS\AULA_08\ATV\temas.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
        #carregando os dados e exibindo na tela
        
        print(f'{'='*45} INFORMAÇÕES {'='*45}')
        global opcao1
        #ciclo de repetição para gravar todos os nomes na tela
        for opcao1 in dados:
            for chave in opcao1:
                print(fr'{chave.capitalize()}: {opcao1.get(chave)}')
            print('='*100)

            #tabela para exibir o proximo nome
            input('Aperte enter para avançar')
            limpar()
            print(100*'=')
                    
        #tabela para permitir o avanço do codigo
        limpar()
        input('Aperte enter para sair')
        limpar()


def exit():
    SystemExit(print('Fechando sistema'))