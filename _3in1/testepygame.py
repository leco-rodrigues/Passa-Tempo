import tkinter as tk


window = tk.Tk()
window.geometry('1200x720')

frame1 = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame2 = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)

label1 = tk.Label(master=frame1, text='First Name:', width=15)
label2 = tk.Label(master=frame2, text='Last Name:')

label1.pack()
label2.pack()

#label1.grid(row=0, column=0, sticky='nw')
#label2.grid(row=1, column=0, sticky='nw')

entry1 = tk.Entry(width=50)
entry2 = tk.Entry(width=50)

entry1.grid(row=0, column=1, sticky='nw')
entry2.grid(row=1, column=1, sticky='nw')

window.mainloop()