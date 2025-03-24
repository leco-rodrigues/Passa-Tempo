import tkinter as tk
import tkinter.ttk as ttk


window_menu = tk.Tk()

window_menu.title('Adivinhe o número')
window_menu.geometry('1920x1080')


frm_titulo = tk.Frame(
    master=window_menu,
    relief='sunken',
    borderwidth=5
)
frm_titulo.pack(padx=75, pady=75)
# titulo do jogo
lbl_titulo = tk.Label(
    master=frm_titulo,
    text='Adivinhe o número!',
    foreground='purple'
)
lbl_titulo.pack()
# regras do jogo
frm_regras = tk.Frame(
    master=window_menu,
    relief='ridge',
    borderwidth=5
)
frm_regras.pack(padx=75, pady=75)

txt_regras = tk.Text(master=frm_regras)
txt_regras.insert(
    '1.0', 'Como jogar:', '2.0',
    '\nO jogo funciona baseado em turnos.'
)


txt_regras.pack()

frm_btn_menu = tk.Frame(
    master=window_menu,
    relief='raised'
)
frm_btn_menu.pack(padx=75, pady=75)
# botões do menu principal
btn_iniciar = tk.Button(
    master=frm_btn_menu,
    text='Iniciar',
    width=25,
    foreground='green',
    background='black'     
)
btn_iniciar.pack()

btn_sair = tk.Button(
    master=frm_btn_menu,
    text='Sair',
    width=25,
    foreground='red',
    background='black'
)
btn_sair.pack()

#frm_nome_jogador = tk.Frame(relief='solid',borderwidth=5)
#frm_nome_jogador.pack()
#
#lbl_nome_jogador = tk.Label(
#    master=frm_nome_jogador,
#    text='Jogador(a) 1, insira seu some:',
#    foreground='black',
#    background='white',
#    width=25
#)
#lbl_nome_jogador.pack()
#
#ent_nome_jogador = tk.Entry(
#    master=frm_nome_jogador,
#    foreground='black',
#    background='white',
#    width=20
#)
#ent_nome_jogador.insert(1, 'Insira seu nome aqui')
#ent_nome_jogador.pack()


window_menu.mainloop()
