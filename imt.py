import tkinter as tk
from tkinter import messagebox

def hitung_imt():
    try:
        tinggi = float(entry_tinggi.get()) / 100  # Konversi tinggi ke meter
        berat = float(entry_berat.get())
        imt = berat / (tinggi ** 2)
        label_hasil.config(text=f"IMT Anda: {imt:.2f}")
        
        if imt < 18.5:
            kategori = "Kurus"
        elif 18.5 <= imt < 24.9:
            kategori = "Normal"
        elif 25 <= imt < 29.9:
            kategori = "Gemuk"
        else:
            kategori = "Obesitas"
            
        label_kategori.config(text=f"Kategori: {kategori}")
        
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

# Inisialisasi GUI
root = tk.Tk()
root.title("Kalkulator IMT")

# Label dan Entry untuk tinggi badan
label_tinggi = tk.Label(root, text="Tinggi badan (cm):")
label_tinggi.grid(column=0, row=0, padx=10, pady=10)

entry_tinggi = tk.Entry(root)
entry_tinggi.grid(column=1, row=0, padx=10, pady=10)

# Label dan Entry untuk berat badan
label_berat = tk.Label(root, text="Berat badan (kg):")
label_berat.grid(column=0, row=1, padx=10, pady=10)

entry_berat = tk.Entry(root)
entry_berat.grid(column=1, row=1, padx=10, pady=10)

# Tombol hitung
button_hitung = tk.Button(root, text="Hitung IMT", command=hitung_imt)
button_hitung.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Label hasil
label_hasil = tk.Label(root, text="IMT Anda: ")
label_hasil.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Label kategori
label_kategori = tk.Label(root, text="Kategori: ")
label_kategori.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Menjalankan GUI
root.mainloop()
