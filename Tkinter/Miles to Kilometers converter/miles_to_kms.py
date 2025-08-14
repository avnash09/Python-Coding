import tkinter as tk, os

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

window = tk.Tk()
window.title("Miles to Kms converter")
# window.minsize(width=300, height=200)
window.geometry("300x200")
window.config(padx=20, pady=20)

miles = tk.Label(window, text="Miles", font=('Arial', 12))
miles.grid(column=2, row=0)

miles_entry = tk.Entry(window, width=5)
miles_entry.grid(column=1, row=0)

kms = tk.Label(window, text="Kms", font=('Arial', 12))
kms.grid(column=2, row=1)

eq_to = tk.Label(window, text="is equal to", font=('Arial', 12))
eq_to.grid(column=0, row=1)

def calculate_button():
    miles_input = float(miles_entry.get())
    result = round(miles_input * 1.609, 2)
    print(result)
    kms_output.config(text=f"{result}")

button = tk.Button(window, text="Calculate", command=calculate_button)
button.grid(column=1, row=2)

kms_output = tk.Label(window, text=0)
kms_output.grid(column=1, row=1)

window.mainloop()