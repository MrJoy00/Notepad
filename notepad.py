from tkinter.filedialog import *
import tkinter as tk
from tkinter import *

def open_file():
    file = askopenfile(mode="r", filetypes=[("Text Files", "*.txt")])
    if file:
        entry.insert(1.0, file.read())

def save_file():
    file = asksaveasfile(mode="w", filetypes=[("Text Files", "*.txt")])
    if file:
        file.write(entry.get(1.0, END))

def clear_text():
    entry.delete(1.0, END)

def exit_application():
    canvas.destroy()


canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="white")
top = Frame(canvas)

button_frame = Frame(canvas)
button_frame.pack(pady=10)

open_button = Button(button_frame, text="Open", command=open_file)
open_button.grid(row=0, column=0, padx=5, sticky='W')

save_button = Button(button_frame, text="Save", command=save_file)
save_button.grid(row=0, column=1, padx=5, sticky='W')

clear_button = Button(button_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=2, padx=5, sticky='W')

exit_button = Button(button_frame, text="Exit", command=exit_application)
exit_button.grid(row=0, column=3, padx=5, sticky='W')

entry = Text(canvas, wrap=WORD, bg="#7cceba", font=("poppins", 15))
entry.pack(padx=10, pady=5, expand=True, fill=BOTH)
canvas.mainloop()

