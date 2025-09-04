import os
import json
import random

opcao = None
escolher_palavras = None

def menu():
    print(f'{40*'='} Enciclopédia {40*'='}')
    print(f'1. Animais')
    print(f'2. Comidas')
    print(f'3. Filmes')
    print(f'4. sair')
    print(f'{90*'='}')

    global opcao

    opcao = int(input('Digite o numero da opcão: '))

    return opcao


def _random_words():
    animais = ["pirarucu", "galinha-da-angola", "cabra", "onça-pintada", "jaguar", "mosca"]
    comidas = ["pizza", "strognoff", "lasanha", "hamburguer", "pure", "empada"]
    filmes = ["Batman", "interstelar", "inception", "ironman", "superman", "halloween"]

    while True:
        match menu():
            case 1:
                caixa_palavras = animais
                break
            case 2:
                caixa_palavras = comidas
                break
            case 3:
                caixa_palavras = filmes
                break
            case 4:
                break

    global escolher_palavras

    escolher_palavras = random.choice(caixa_palavras)
    return escolher_palavras

def jogar_forca():
    global escolher_palavras
    palavra = escolher_palavras
    letras_corretas= []
    letras_erradas= []  
    tentativas= 6

    while True:
        palavra_escondida= ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'

        print('Palavra:', palavra_escondida)
        print('Letras erradas:', letras_erradas)
        print('Tentativas restantes:', tentativas)

        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!')
            break
        elif tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            break

        letra_usuario= input('Digite uma letra: ').lower()

        if letra_usuario in palavra:
            print('Letra correta!')
            letras_corretas.append(letra_usuario)
        else:
            print('Letra errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1

_random_words()

if __name__ == "__main__":
    os.system('cls')
    print("Bem-vindo ao jogo da Forca!")
    jogar_forca()

