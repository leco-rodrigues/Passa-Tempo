# Faça o computador escolher um número aleatório de 1 a 100. e o usuário deve adivinhar com dicas de "maior" ou "menor".

from random import randint
from time import sleep


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritoverde':'\033[1;32m',
         'negritoazul':'\033[1;34m', 'negritoamarelo':'\033[1;33m', 'negritovermelho':'\033[1;31m'}

def adivinhar_numero(jogador):
    numero = randint(1, 100)
    while True:
        try:
            palpite = int(input(f'{cores['pretoebranco']}{jogador}, qual você acha que foi o número sorteado?{cores['limpa']} '))
            if 1 <= palpite <= 100:
                print(f'{cores['negritoroxo']}--=--' * 3,
                      f'\nVejamos aqui...{cores['limpa']}')
                print(f'{cores['negritoroxo']}--=--{cores['limpa']}' * 3)
                sleep(2)
                if palpite == numero:
                    return f'{cores['negritoverde']}Meus parabéns! Você acertou! O número era {numero}.{cores['limpa']}'
                elif palpite > numero:
                    print(f'{cores['negritoazul']}O número correto é menor... Tente novamente!{cores['limpa']}')
                else:
                    print(f'{cores['negritoamarelo']}O número correto é maior... Tente novamente!{cores['limpa']}')
            else:
                print(f'{cores['negritovermelho']}Por favor, escolha um número inteiro entre 1 e 100.{cores['limpa']}')
        except ValueError:
            print(f'{cores['negritovermelho']}Por favor, digite apenas números inteiros.{cores['limpa']}')

j1 = input(f'{cores['pretoebranco']}Jogador 1, digite o seu nome:{cores['limpa']} ')
print(adivinhar_numero(j1))
