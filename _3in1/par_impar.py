# Jogo do par ou ímpar:
    # Faça um programa que jogue par ou ímpar com o seu computador.
    # O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from custom_module import txt_style as styl, print_error, sepa_rator as sep_
from random import randint


# Passo 1: Solicitar um valor para "escolha"
print(styl(f"\t{' ODDS & EVENS ':=^40}\n", 'bd'))

player_wins: int = 0

while True:

    while True:
        player_choice: str = str(input(styl("Please enter 'Odd' or 'Even' (game's only stop when you lose):", 'n') + " ")).strip().lower()

        if player_choice in ("odd", "even"):
            break
        else:
            print_error("Invalid input. Please enter 'even' or 'odd'.")

    computer: int = randint(0, 10)

    while True:
        try:
            player_num: int = int(input(styl("Please enter a number:", 'n') + " "))

            if 0 <= player_num <= 10:
                break
            else:
                print_error("Invalid input. Please enter an integer between 0 and 10.")

        except ValueError:
            print_error("Invalid input. Please enter an integer between 0 and 10.")

    sep_(color = 'c')
    total: int = computer + player_num

    print(styl(f"Player's choice: {player_choice}\n" + f"Player: {player_num} + Computer: {computer} = {total} ({'even' if total % 2 == 0 else 'odd'})", 'bd', 'p'))

    if (total % 2 == 0 and player_choice == "even") or (total % 2 == 1 and player_choice == 'odd'):
        print(styl("Player wins!", 'bd', 'g'))
        sep_(color = 'c')
        player_wins += 1
    else:
        print(styl("Computer wins!", 'bd', 'y'))
        sep_(color = 'c')
        break

# Passo 2: Exibir número de vitórias consecutivas
print(styl(f"Player's consecutive victories: {player_wins}", 'bd', 'p'))
sep_(color = 'c')

# Passo 3: Exibir mensagem de encerramento
print(styl("Exiting the program... Thank you for playing! 😄", 'bd'))
# -------------------------------------------------------------------| AULA 15 - INTERROMPENDO REPETIÇÕES "WHILE" | DESAFIO [068]
