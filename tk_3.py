# -*- coding: utf-8 -*-
import Tkinter as tk

def resize(ev = None):
    label.config(font = 'Helvetica -%d bold' % scale.get())

top = tk.Tk()
top.geometry('350x250')

label = tk.Label(top, text = 'hello world', font = 'Helvetica -12 bold')
label.pack(fill = tk.Y, expand = 1)

scale = tk.Scale(top, from_ = 10, to = 40, orient = tk.HORIZONTAL, command = resize)
scale.set(12)
scale.pack(fill = tk.X, expand = 1)

quit1 = tk.Button(top, text = 'QUIT', command = top.quit, activebackground = 'red', activeforeground = 'white')
quit1.pack(fill = tk.X, expand = 1)

quit2 = tk.Button(top, text = 'QUIT', command = top.quit, bg = 'blue', fg = 'white')
quit2.pack(fill = tk.X, expand = 1)
tk.mainloop()