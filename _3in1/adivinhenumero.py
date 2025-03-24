# Faça o computador escolher um número aleatório de 1 a 100. e o usuário deve adivinhar com dicas de "maior" ou "menor".

def main():
    from random import randint
    from time import sleep


    def cor(txt:str, type:int = 1):
        cores = {"limpa":"\033[m", "pretoebranco":"\033[7;40m", "negritoroxo":"\033[1;35m", "negritoverde":"\033[1;32m",
             "negritoazul":"\033[1;34m", "negritoamarelo":"\033[1;33m", "negritovermelho":"\033[1;31m"}
        
        if type == 1:
            return f'{cores["pretoebranco"]}{txt}{cores["limpa"]} '
        if type == 2:
            return f'{cores["negritovermelho"]}{txt}{cores["limpa"]}'
        if type == 3:
            return f'{cores["negritoroxo"]}{txt}{cores["limpa"]}'
        if type == 4:
            return f'{cores["negritoazul"]}{txt}{cores["limpa"]}'
        if type == 5:
            return f'{cores["negritoamarelo"]}{txt}{cores["limpa"]}'
        if type == 6:
            return f'{cores["negritoverde"]}{txt}{cores["limpa"]}'

    def separador():
        print(cor('--=--', 3) * 23)

    def sim_não(pergunta:str):
        while True:
            resposta = input(pergunta).strip()
            
            if resposta.lower() in ['sim', 's']:
                return True
            elif resposta.lower() in ['não', 'n']:
                return False
            else:
                print(cor('Por favor, digite apenas "sim" ou "não".', 2))

    def nome_jogador(jogador:str):
        while True:
            nome = input(jogador).strip()
            
            if nome.split() and all(carac.isalnum() or carac.isspace() for carac in nome):
                return nome
            else:
                print(cor('Por favor, digite um nome válido (sem símbolos ou espaço em branco).', 2))

    def validar_palpite(jogador:str):
        while True:
            try:
                palpite = int(input(cor(f'{jogador}, qual você acha que foi o número sorteado?', 1)))
                
                if 1 <= palpite <= 100:
                    return palpite
                else:
                    print(cor('Por favor, escolha um número inteiro entre 1 e 100.', 2))
            
            except ValueError:
                print(cor('Por favor, digite um número inteiro.', 2))

    def adivinhar_numero(jogadores:list):
        if sim_não(cor('Gostaria de adicionar mais um jogador(a) (s/n)?', 1)):
            j3 = nome_jogador(cor('Jogador(a) 3, por favor, digite o seu nome:', 1))
            jogadores.append(j3)
        
        numero = randint(1, 100)
        tentativas = 0
        
        while tentativas != len(jogadores) * 5:
            for i in range(len(jogadores)):
                palpite = validar_palpite(jogadores[i])
                
                separador()
                print(cor('Vejamos aqui...', 3))
                separador()
                sleep(0.5)
                
                print(cor('Alterando o número...', 3))
                separador()
                sleep(0.5)
                
                print(cor('Haha! Brincadeirinha!', 3))
                separador()
                sleep(0.5)
                
                if palpite == numero:
                    return cor(f'Meus parabéns, {jogadores[i]}! Você venceu! O número correto era {numero}.', 6)
                elif palpite > numero:
                    print(cor(f'Mas você errou, {jogadores[i]}! O número correto é menor...', 4))
                    separador()
                    tentativas = tentativas + 1
                else:
                    print(cor(f'Mas você errou, {jogadores[i]}! O número correto é maior...', 5))
                    separador()
                    tentativas = tentativas + 1
        
        sleep(0.5)
        print(cor(f'Que pena! O número de tentativas se esgotou! O número correto era {numero}.', 2))
        separador()

        return cor('Obrigado por jogar "Adivinhe o número"!', 3)

    j1 = nome_jogador(cor('Jogador(a) 1, por favor, digite o seu nome:', 1))
    j2 = nome_jogador(cor('Jogador(a) 2, por favor, digite o seu nome:', 1))
    jogadores = [j1, j2]

    print(adivinhar_numero(jogadores))

main()

while True:
    continuar = input('\n\033[7;40mDeseja jogar novamente (s/n)?\033[m ').strip()
    
    if continuar.lower() in ['sim', 's']:
        main()
        continue
    elif continuar.lower() in ['não', 'n']:
        print('\033[1;35m--=--' * 23,
              '\n\Espero ver você(s) aqui de novo em breve! Até a próxima!\033[m')
        break
    else:
        print(f'\033[1;31mPor favor, digite apenas "sim" ou "não".\033[m')

exit()
