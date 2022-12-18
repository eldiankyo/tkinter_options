import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()

label2 = ttk.Label(root)
label2.config(text='Hi, there')
label2.pack()

root.mainloop()