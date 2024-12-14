import tkinter as tk
from tkinter import messagebox
import hashlib

# Fungsi untuk membuat akun
def buat_akun():
    username = entry_username.get()
    password = entry_password.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan Password tidak boleh kosong.")
        return
    
    if username in akun_db:
        messagebox.showerror("Error", "Username sudah digunakan.")
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        akun_db[username] = hashed_password
        messagebox.showinfo("Info", "Akun berhasil dibuat!")

# Fungsi untuk login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username dan Password tidak boleh kosong.")
        return
    
    if username in akun_db:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if akun_db[username] == hashed_password:
            messagebox.showinfo("Info", "Login berhasil!")
        else:
            messagebox.showerror("Error", "Password salah.")
    else:
        messagebox.showerror("Error", "Username tidak ditemukan.")

# Inisialisasi database akun
akun_db = {}

# Membuat jendela utama
root = tk.Tk()
root.title("Simulasi Akun")

# Frame untuk memasukkan data
frame = tk.Frame(root)
frame.pack(pady=10)

# Label dan input untuk username
label_username = tk.Label(frame, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5)
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Label dan input untuk password
label_password = tk.Label(frame, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Tombol untuk membuat akun
button_buat_akun = tk.Button(frame, text="Buat Akun", command=buat_akun)
button_buat_akun.grid(row=2, column=0, columnspan=2, pady=5)

# Tombol untuk login
button_login = tk.Button(frame, text="Login", command=login)
button_login.grid(row=3, column=0, columnspan=2, pady=5)

# Menjalankan loop GUI
root.mainloop()
