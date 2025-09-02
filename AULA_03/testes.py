#problema 2: um elevador de carga possui capacidade para 200kg.
#crie um programa que receba do usuario, seu peso e o peso da carga
#e verifique se a carga esta autorizada a usar o elevador ou não

print(30*'=','Elevador',30*'=')

#apresentando a pergunta e solicitando interação do usuario
print('Informe o peso do passageiro')
print('Se não houver passageiro informe 0')
peso_p = float(input('Peso: ')) #coletando peso da pessoa
print('Informe o peso da carga extra')
print('Se não houver carga informe 0')
peso_c = float(input('Peso: ')) #coletando peso da carga

#calculando o peso total dentro do elevador
peso_total = peso_p + peso_c
sim = True
Sim = True
#para a determinar a escolha de caso definimos que o peso maximo seria de duzentos

#o peso atende ao limite?
if peso_total > 200:
    print('A carga excede a capacidade do elevador')
    if peso_total - peso_p <= 200: #se a carga estiver dentro do limite esta função é executada
        print('A carga possui peso dentro da metrica')
        print('É possivel seguir se o passageiro descer')
        resp = input('Deseja fazer isso s/n: ')
        if resp == 's': #se o usuario aceitar o elevador sobe
            print('Perfeito')
            print('Elevador subindo')
            SystemExit() # o codigo pará
        elif ((peso_total - peso_c) <= 200) and resp == 'n': #se o usuario não aceitar descer essa condição e testada
            print('Deseja retirar a carga e subir')
            resp_2 = input('Deseja fazer isso s/n: ')
            if resp_2 == 's':#se o usuario aceitar o elevador sobe e o codigo pará
                print('Perfeito')
                print('Subindo')
                SystemExit
            else: #se o usuario recusa todas as alternativas o codigo pará e o elevador não sobe
                print('O elevador não pode subir')
                SystemExit
        else:#se o passageiro e mais pesado que a carga e não quer descer o codigo pará
            print('O elevador não pode subir')
            SystemExit
    elif 200 >= peso_total - peso_c: #se a carga for mais pesada que o limite mas o passageiro não esta função é acionada
        print('Deseja retirar a carga e subir')
        resp_2 = input('Deseja fazer isso s/n: ')
        if resp_2 == 's': # se o usuarioa aceitar o elevador sobe
            print('Perfeito')
            print('Subindo')
        else: #se o usuario recusar o elevador fica parado
            print('O elevador não pode subir')
            SystemExit
    else: #se a carga excede tanto o passageiro quanto a carga adicional o codigo pará automaticamente
        print('O elevador não pode subir')
        SystemExit 
else: #se a carga total e aceita o elevador sobe diretamente
    print('Carga aceita')
    print('Boa Viagem! ;)')        