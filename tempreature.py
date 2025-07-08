import tkinter as tk
from tkinter import ttk, messagebox


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def convert():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == 'Celsius':
            result_f = celsius_to_fahrenheit(temp)
            result_k = celsius_to_kelvin(temp)
            output.set(
                f"{temp}°C = {result_f:.2f}°F\n{temp}°C = {result_k:.2f}K")
        elif unit == 'Fahrenheit':
            result_c = fahrenheit_to_celsius(temp)
            result_k = fahrenheit_to_kelvin(temp)
            output.set(
                f"{temp}°F = {result_c:.2f}°C\n{temp}°F = {result_k:.2f}K")
        elif unit == 'Kelvin':
            result_c = kelvin_to_celsius(temp)
            result_f = kelvin_to_fahrenheit(temp)
            output.set(
                f"{temp}K = {result_c:.2f}°C\n{temp}K = {result_f:.2f}°F")
    except ValueError:
        messagebox.showerror(
            "Invalid Input", "Please enter a valid numeric value.")


# GUI setup
root = tk.Tk()
root.title("🧊 Temperature Converter 🌡️")
root.geometry("350x300")
root.resizable(False, False)

unit_var = tk.StringVar(value="Celsius")
output = tk.StringVar()

tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=5)
entry_temp = tk.Entry(root, font=("Arial", 12), justify='center')
entry_temp.pack(pady=5)

tk.Label(root, text="Select Unit:", font=("Arial", 12)).pack(pady=5)
ttk.Combobox(root, textvariable=unit_var, values=[
             "Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 11)).pack(pady=5)

tk.Button(root, text="Convert", command=convert,
          font=("Arial", 12), bg="#add8e6").pack(pady=10)

tk.Label(root, textvariable=output, font=(
    "Arial", 12), fg="green").pack(pady=10)


root.mainloop()