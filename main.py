# importação de bibliotecas
import os
from datetime import date

#entrada de dados
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
date = f'{date.today().day}/{date.today().month}/{date.today().year}'
# limpa console
os.system('cls')

# inicio do loop
while True:
    print(f'{'-'*20} CINE PYTHON {'-'*30}')
    print(f'{date}\n')
    print('Sala 1 - Deuses - 10 anos.')
    print('Sala 2 - Python - 14 anos.')
    print('sala 3 - poeira em alto mar - 16 anos.')
    print('sala 4 - guerra sem matar - livre.')
    print('sala 5 - A vingansa da minhoca - 18 anos')

    # escolha do usuario
    sala = input('\nSala desejada: ')

    # verficar a sala escolhida 
    match sala:
        case '1':
            idade_minima = 10
            filme = 'Deuses'
        case '2':
            idade_minima = 14
            filme = 'Python'
        case '3':
            idade_minima = 16
            fime = 'Poeira e alto mar.'
        case '4':
            idade_minima = 0
            filme = 'guerra sem matar. '
        case '5':
            idade_minima = 18
            filme = 'A vingansa das minhocas. '
        case _:
            print('sala inexistente. Por favor escolha outra opção. ')
            continue

    # Verificação da idade
    if idade >= idade_minima:
        print(f'Ingresso impresso no dia: {date}.')
        print(f'Pagante: {filme}. ')
        print(f'Filme: {filme}. ')
        print(f'Sala {sala}. ')
        print('\nTenha um otimo filme!')
        break
    else:
        print(f'{nome} não possui a idade minima para ver {filme}.')
        print('Por favor escolha outro filme!')
        continue


















