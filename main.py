from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
import tkinter as tk


def utf_8():
    value = input.get()

    if value:
        msg = "Файл сохранен"
        mb.showinfo("Информация", msg)
        Transform(value, 'UTF.txt', 'utf-8')
        return
    else:
        msg = "Текст отсутсвует"
        mb.showwarning("Предупреждение", msg)
        return


def windows_1251():
    value = input.get()

    if value:
        msg = "Файл сохранен"
        mb.showinfo("Информация", msg)
        Transform(value, 'Win.txt', 'windows-1251')
        return
    else:
        msg = "Текст отсутсвует"
        mb.showwarning("Предупреждение", msg)
        return


def Transform(text, filename, encode):
    with open(filename, 'wb') as f:
        f.write(text.encode(encode, errors='replace'))


ws = tk.Tk()
ws.title('OS')
ws.geometry('200x200')

input = ttk.Entry(ws)
input.pack()

tk.Button(ws, text='UTF-8', command=utf_8).pack()
tk.Button(ws, text='WINDOWS-1251', command=windows_1251).pack()

ws.mainloop()
