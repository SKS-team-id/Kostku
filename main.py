import json
import os

file_path= "users.json"

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
        if user ['username'] == username and user ['password'] == password:
            print("Login berhasil! Selamat datang di aplikasi Kostku", username, "!")
            return username
    
    print("Login gagal! Username atau password salah.")
    return None
    

def register():
    print("=== Halaman Register ===")
    username = input("Masukkan username baru: ")
    users = load_users(file_path)
    
    if any (user["username"] == username for user in users):
        print("Username sudah digunakan, silakan coba username yang lain.")
        return 
    password = input("Masukkan password: ")
    kode = input("Masukkan kode referral: ")

    if kode == "kostku1" :
        new_user = {
        "username": username,
        "password": password
    }
        users.append(new_user)
        save_users(users)
        print("Registrasi berhasil! Silakan login.")
    else : 
        print("Kode referral salah, silakan coba lagi.")

def logout() :
    print("Logout berhasil! Sampai datang kembali.")
    return None


def main():
    pengguna_saat_ini = None
    while True:
        print("=== Pilihan Menu ===")
        print("1. Login")
        print("2. Register")
        if pengguna_saat_ini:
            print("3. Logout")

        pilihan = input("Pilih (1/2/3): ").lower()
        
        if pilihan == '1':
            if pengguna_saat_ini:
                print("Anda sudah login sebagai", pengguna_saat_ini, ". Silakan logout terlebih dahulu.")
            else:
                pengguna_saat_ini = login()
        elif pilihan == '2':
            if pengguna_saat_ini:
                    print("Anda sudah login sebagai", pengguna_saat_ini, ". Silakan logout terlebih dahulu untuk membuat akun baru.")
            else:
                register()
        elif pilihan == "3" and pengguna_saat_ini:
            pengguna_saat_ini = logout()
        else:
            print("Pilihan tidak valid, silakancoba lagi.")

main()
