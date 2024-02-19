from tkinter import*
import random

root = Tk()
root.geometry('600x600')
root.resizable(0, 0)
root.title('DataFlair-pierre,feuille,ciseaux')
root.config(bg='steelblue3')

Label(root, text='pierre, feuille, ciseaux', font='arial 20 bold', bg='seashell2').pack()

user_name = StringVar()  # Utilisez StringVar au lieu de SyntaxError()
Label(root, text='Donnez votre nom', font='arial 15 bold', bg='seashell2').place(x=210, y=70)
Entry(root, font='arial 15', textvariable=user_name, bg='antiquewhite2').place(x=190, y=130)

user_take = StringVar()
Label(root, text='Faites votre choix: pierre, feuille, ciseaux', font='arial 15 bold', bg='seashell2').place(x=110, y=170)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=190, y=230)

comp_pick = random.randint(1, 3)

if comp_pick == 1:
    comp_pick = 'pierre'
elif comp_pick == 2:
    comp_pick = 'feuille'
else:
    comp_pick = 'ciseaux'

Result = StringVar()


def Play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set(f'Égalité, vous avez tous les deux choisi {user_pick}')
    elif user_pick == 'pierre' and comp_pick == 'feuille':
        Result.set(f'Tu as perdu, {user_name.get()}! L\'ordinateur a choisi feuille')
    elif user_pick == 'pierre' and comp_pick == 'ciseaux':
        Result.set(f'Tu as gagné, {user_name.get()}! L\'ordinateur a choisi ciseaux')
    elif user_pick == 'feuille' and comp_pick == 'ciseaux':
        Result.set(f'Tu as perdu, {user_name.get()}! L\'ordinateur a choisi ciseaux')
    elif user_pick == 'feuille' and comp_pick == 'pierre':
        Result.set(f'Tu as gagné, {user_name.get()}! L\'ordinateur a choisi pierre')
    elif user_pick == 'ciseaux' and comp_pick == 'pierre':
        Result.set(f'Tu as perdu, {user_name.get()}! L\'ordinateur a choisi pierre')
    elif user_pick == 'ciseaux' and comp_pick == 'feuille':
        Result.set(f'Tu as gagné, {user_name.get()}! L\'ordinateur a choisi feuille')
    else:
        Result.set('Invalide: Choisis entre pierre, feuille, ciseaux')


def Reset():
    Result.set("")
    user_take.set("")
    user_name.set("")


def Exit():
    root.destroy()


Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50, ).place(x=125, y=350)

Button(root, font='arial 13 bold', text='COMMENCER', padx=5, bg='seashell4', command=Play).place(x=250, y=290)

Button(root, font='arial 13 bold', text='RECOMMENCER', padx=5, bg='seashell4', command=Reset).place(x=170, y=410)

Button(root, font='arial 13 bold', text='SORTIR', padx=5, bg='seashell4', command=Exit).place(x=330, y=410)

root.mainloop()
