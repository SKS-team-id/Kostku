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
    useri = input("Masukkan username: ")
    password = input("Masukkan password: ")
    users = load_users(file_path)
    
    for user in users: 
        if user ['username'] == useri and user ['password'] == password:
            print("Login berhasil! Selamat datang di aplikasi Kostku!")
        return user
    
    print("Login gagal! Username atau password salah.")
    

def register():
    print("=== Halaman Register ===")
    username = input("Masukkan username baru: ")
    users = load_users(file_path)
    
    if username in users:
        print("Username sudah digunakan, silakan coba lagi.")
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

def main():
    while True:
        print("=== Pilihan Menu ===")
        print("a. Login")
        print("b. Register")
        pilihan = input("Pilih (a/b): ").lower()
        
        if pilihan == 'a':
            login()
        elif pilihan == 'b':
            register()
        else:
            print("Pilihan tidak valid, silakan pilih 'a' atau 'b'.")

main()
