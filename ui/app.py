import tkinter as tk
from tkinter import filedialog, messagebox
import os

def select_input_file():
    file_path = filedialog.askopenfilename(
        title="Válassz egy Excel fájlt",
        filetypes=[("Excel fájlok", "*.xlsx *.xls")]
    )
    if file_path:
        input_file_path.set(file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(
        title="Eredményfájl mentése",
        defaultextension=".xlsx",
        filetypes=[("Excel fájlok", "*.xlsx")]
    )
    if file_path:
        output_file_path.set(file_path)

def process_data():
    input_file = input_file_path.get()
    output_file = output_file_path.get()

    if not input_file or not os.path.exists(input_file):
        messagebox.showerror("Hiba", "Érvényes bemeneti fájlt kell kiválasztani!")
        return

    if not output_file:
        messagebox.showerror("Hiba", "Érvényes eredményfájlt kell megadni!")
        return

    try:
        # Példa: adatfeldolgozás meghívása
        from data_processing.processor import process_excel
        process_excel(input_file, output_file)
        messagebox.showinfo("Siker", "Az adatfeldolgozás sikeresen befejeződött!")
    except Exception as e:
        messagebox.showerror("Hiba", f"Hiba történt: {str(e)}")

# Fő ablak
root = tk.Tk()
root.title("Excel Adatfeldolgozó")

# Input fájl kiválasztás
input_file_path = tk.StringVar()
tk.Label(root, text="Bemeneti fájl:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=input_file_path, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Tallózás...", command=select_input_file).grid(row=0, column=2, padx=10, pady=5)

# Output fájl kiválasztás
output_file_path = tk.StringVar()
tk.Label(root, text="Eredményfájl:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=output_file_path, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Mentés...", command=select_output_file).grid(row=1, column=2, padx=10, pady=5)

# Adatfeldolgozás gomb
tk.Button(root, text="Feldolgozás indítása", command=process_data).grid(row=2, column=0, columnspan=3, pady=10)

# Fő ciklus
root.mainloop()
