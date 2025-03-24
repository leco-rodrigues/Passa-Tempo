from getpass import getpass


def inserir_nome(jogador = 'Insira seu nome: '):
    while True:
        nome = input(jogador).strip()
        if nome and all(caractere.isalpha() or caractere.isnumeric() or caractere.isspace() for caractere in nome):
            return nome[:10].strip()
        else:
            print('Por favor, utilize apenas letras e números.')

def jogador_extra():
    while True:
        resposta = input('Deseja adicionar mais um(a) jogador(a) (s/n)? ').lower().strip()
        if resposta in ['s', 'sim']:
            jogador_extra = inserir_nome('Jogador 3, insira o seu nome: ')
            return jogador_extra
        elif resposta in ['n', 'não']:
            return False
        else:
            print('Por favor, digite "Sim" ou "Não".')

def process_escolha(escolha):
    while True:
        escolha = getpass(escolha)
        if escolha.lower().strip() in ['pedra', 'papel', 'tesoura']:
            return escolha.lower().strip()
        else:
            print('Por favor, escolha "pedra", "papel" ou "tesoura".')

def requisitar_escolhas(jogadores = []):
    escolhas = []
    escolha = None
    J3 = jogador_extra()
    if J3:
        jogadores.append(J3)
    for i, nome in enumerate(jogadores):
        escolha = process_escolha(f'{jogadores[i]}, escolha "pedra", "papel" ou "tesoura": ')
        escolhas.append(escolha)
    return escolhas

def jokenpo_2P(jogador1, jogador2):
    if jogador1 == jogador2:
        return 0
    elif ((jogador1 == 'pedra' and jogador2 == 'tesoura') or
          (jogador1 == 'papel' and jogador2 == 'pedra') or
          (jogador1 == 'tesoura' and jogador2 == 'papel')):
        return 1
    else:
        return 2

def jokenpo_3P(jogador1, jogador2, jogador3):
    if ((jogador1 == jogador2 == jogador3) or (jogador1 != jogador2 != jogador3)):
        return 0
    elif ((jogador1 == 'pedra' and jogador2 == 'tesoura' and jogador3 == 'tesoura') or
        (jogador1 == 'papel' and jogador2 == 'pedra' and jogador3 == 'pedra') or
        (jogador1 == 'tesoura' and jogador2 == 'papel' and jogador3 == 'papel')):
        return 1
    elif ((jogador2 == 'pedra' and jogador1 == 'tesoura' and jogador3 == 'tesoura') or
        (jogador2 == 'papel' and jogador1 == 'pedra' and jogador3 == 'pedra') or
        (jogador2 == 'tesoura' and jogador1 == 'papel' and jogador3 == 'papel')):
        return 2
    elif ((jogador3 == 'pedra' and jogador1 == 'tesoura' and jogador2 == 'tesoura') or
        (jogador3 == 'papel' and jogador1 == 'pedra' and jogador2 == 'pedra') or
        (jogador3 == 'tesoura' and jogador1 == 'papel' and jogador2 == 'papel')):
        return 3
    else:
        return
# ------------ [Exercício] Aula 14