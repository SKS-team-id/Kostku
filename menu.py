import json
import os
from manajemen_kamar_kost import tampilkan_menu_pengelola, tampilkan_menu_penyewa

file_path = "users.json"

def load_users(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

def save_users(users):
    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)

def login():
    print("=== Halaman Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    users = load_users(file_path)

    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Login berhasil! Selamat datang, {username}!")
            if user['username'] == "admin":
                print("Anda login sebagai pengelola.")
                tampilkan_menu_pengelola()
            elif user['username'] != "admin":
                print("Anda login sebagai penyewa.")
                tampilkan_menu_penyewa()
            return user
    print("Login gagal! Username atau password salah.")

def register():
    print("=== Halaman Register ===")
    username = input("Masukkan username baru: ")
    users = load_users(file_path)
    
    if any(user["username"] == username for user in users):
        print("Username sudah digunakan, silakan coba username lain.")
        return 
    password = input("Masukkan password: ")
    kode = input("Masukkan kode referral: ")
    if kode == "kostku1":
        new_user = {"username": username, "password": password}
        users.append(new_user)
        save_users(users)
        print("Registrasi berhasil! Silakan login.")
    else:
        print("Kode referral salah, silakan coba lagi.")

def logout():
    print("Logout berhasil! Sampai jumpa kembali >.<")
    return None

def main():
    pengguna_saat_ini = None
    while True:
        print("\n=== Pilihan Menu ===")
        print("1. Login")
        print("2. Register")
        pilihan = input("Pilih (angka menu): ").strip()
        if pilihan == '1':
            login()
        elif pilihan == '2':
            register()

if __name__ == "__main__":
    main()