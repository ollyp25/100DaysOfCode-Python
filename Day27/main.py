import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

window = ttk.Window(themename='journal')
window.title('Converter')
window.geometry('300x150')

title_label = ttk.Label(master=window, text= 'mile to kilometers', font=('Calibri', 24, "bold"))
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack()
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font=('Calibri', 24),
    textvariable=output_string
)
output_label.pack(pady=5)

window.mainloop()