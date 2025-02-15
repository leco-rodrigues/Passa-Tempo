# Faça o computador escolher um número aleatório de 1 a 100. e o usuário deve adivinhar com dicas de "maior" ou "menor".

def main():
    from random import randint
    from time import sleep


    cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritoverde':'\033[1;32m',
             'negritoazul':'\033[1;34m', 'negritoamarelo':'\033[1;33m', 'negritovermelho':'\033[1;31m'}

    def sim_não(pergunta):
        while True:
            resposta = input(pergunta).strip()
            if resposta.lower() in ['sim', 's']:
                return True
            elif resposta.lower() in ['não', 'n']:
                return False
            else:
                print(f'{cores["negritovermelho"]}Por favor, digite apenas "sim" ou "não".{cores["limpa"]}')

    def nome_jogador(nome):
        while True:
            jogador = input(nome).strip()
            if jogador.split() and all(carac.isalnum() or carac.isspace() for carac in jogador):
                return jogador
            else:
                print(f'{cores["negritovermelho"]}Por favor, digite um nome válido (sem espaço vazio).{cores["limpa"]}')

    def validar_palpite(palpite):
        

    def adivinhar_numero(jogadores):
        if sim_não(f'{cores["pretoebranco"]}Gostaria de adicionar mais um jogador(a) (s/n)?{cores["limpa"]} '):
            j3 = nome_jogador(f'{cores["pretoebranco"]}Jogador 3, por favor, digite o seu nome:{cores["limpa"]} ')
            jogadores.append(j3)
        numero = randint(1, 100)
        while True:
            for i in range(len(jogadores)):
                    while True:
                        try:
                            palpite = int(input(f'{cores["pretoebranco"]}{jogadores[i]}, qual você acha que foi o número sorteado?{cores["limpa"]} '))
                            if 1 <= palpite <= 100:
                                print(f'{cores["negritoroxo"]}--=--' * 3,
                                        f'\nVejamos aqui...{cores["limpa"]}')
                                print(f'{cores["negritoroxo"]}--=--{cores["limpa"]}' * 3)
                                sleep(1)
                                if palpite == numero:
                                    return f'{cores["negritoverde"]}Meus parabéns! Você acertou! O número era {numero}.{cores["limpa"]}'
                                elif palpite > numero:
                                    print(f'{cores["negritoazul"]}O número correto é menor...{cores["limpa"]}')
                                else:
                                    print(f'{cores["negritoamarelo"]}O número correto é maior...{cores["limpa"]}')
                                break
                            else:
                                print(f'{cores["negritovermelho"]}Por favor, escolha um número inteiro entre 1 e 100.{cores["limpa"]}')
                        except ValueError:
                            print(f'{cores["negritovermelho"]}Por favor, digite um número inteiro.{cores["limpa"]}')

    j1 = nome_jogador(f'{cores["pretoebranco"]}Jogador(a) 1, por favor, digite o seu nome:{cores["limpa"]} ')
    j2 = nome_jogador(f'{cores["pretoebranco"]}Jogador(a) 2, por favor, digite o seu nome:{cores["limpa"]} ')
    jogadores = [j1, j2]

    print(adivinhar_numero(jogadores))

main()
while True:
    continuar = input('\033[7;40mDeseja jogar novamente (s/n)?\033[m ').strip()
    if continuar.lower() in ['sim', 's']:
        main()
        continue
    elif continuar.lower() in ['não', 'n']:
        print('\033[1;35mAté a próxima!\033[m')
        break
    else:
        print(f'\033[1;31mPor favor, digite apenas "sim" ou "não".\033[m')
