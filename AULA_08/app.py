import random
import string

def gerar_senha(comprimento=12, incluir_maiusculo=True, incluir_minusculo=True, incluir_numero=True, incluir_caracter=True):
    
    caracteres= ''
    if incluir_minusculo:
        caracteres += string.ascii_lowercase
    if incluir_maiusculo:
        caracteres += string.ascii_uppercase
    if incluir_numero:
        caracteres += string.digits
    if incluir_caracter:
        caracteres += string.punctuation
    if not caracteres:
        return ValueError('Campo vazio')
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'senha: {senha}')
    return senha

def main():
    print(30*'=','Gerador de senhas fortes',30*'=')
    comprimento = int(input('Qual deve ser o comprimento da senha? (padrão: 12): '))
    incluir_maiusculo = input('Incluir letras maiusculas? (s/n padrão: sim): ').lower != 'n'
    incluir_minusculo = input('Incluir letras minusculas? (s/n padrão: sim): ').lower != 'n'
    incluir_numero = input('Incluir numeros? (s/n padrão: sim): ').lower != 'n'
    incluir_caracter = input('Incluir lcaracteres especiais? (s/n padrão: sim): ').lower != 'n'

    senha = gerar_senha(comprimento, incluir_maiusculo, incluir_minusculo, incluir_numero, incluir_caracter)
    print(f'A senha gerada foi: {senha}')

    with open('AULA_08/senhas.txt', 'a') as s:
        s.write(f'/n{senha}')

if __name__=='__main__':
    main()