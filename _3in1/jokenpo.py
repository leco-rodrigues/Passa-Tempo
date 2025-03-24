import jokenpo_utils as jkp


jogadores = []
J1 = jkp.inserir_nome('Jogador 1, insira o seu nome: ')
J2 = jkp.inserir_nome('Jogador 2, insira o seu nome: ')
jogadores.append(J1)
jogadores.append(J2)
escolhas = jkp.requisitar_escolhas(jogadores)

EMPATE = 0
VITORIA_J1 = 1
VITORIA_J2 = 2
VITORIA_J3 = 3
if range(len(escolhas)) == range(2):
    resultado = jkp.jokenpo_2P(escolhas[0], escolhas[1])
    for i, escolha in enumerate(escolhas):
        print(f'{jogadores[i]}: {escolha}.')
    if resultado == EMPATE:
        print('Empate!')
    elif resultado == VITORIA_J1:
        print(f'{jogadores[0]} venceu!')
    else:
        print(f'{jogadores[1]} venceu!')        
else:
    resultado = jkp.jokenpo_3P(escolhas[0], escolhas[1], escolhas[2])
    for i, escolha in enumerate(escolhas):
        print(f'{jogadores[i]}: {escolha}.')
    if resultado == EMPATE:
        print('Empate!')
    elif resultado == VITORIA_J1:
        print(f'{jogadores[0]} venceu!')
    elif resultado == VITORIA_J2:
        print(f'{jogadores[1]} venceu!')
    elif resultado == VITORIA_J3:
        print(f'{jogadores[2]} venceu!')
    else:
        print('Ninguém venceu!')
# ------------------------------ [Exercício] Aula 14