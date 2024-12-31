import json
import os
from riwayat_pembayaran import tampilan_pembayaran_pengelola, tampilan_pembayaran_penyewa

file_path = "users.json"

def load_users(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

def save_users(users):
    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)
def simpan_ke_json():
    with open("data_kamar.json", "w") as file:
        json.dump(data_kamar, file, indent=4)
    print("Data berhasil disimpan ke file JSON.")
    with open("data_pembayaran.json", "w") as file:
        json.dump(data_kamar, file, indent=4)
    print("Data berhasil disimpan ke file JSON.")

def baca_dari_json():
    global data_kamar
    if os.path.exists('data_kamar.json'):
        with open('data_kamar.json', 'r') as file:
            return json.load(file)
    else:
        return []
    
    if os.path.exists("data_pembayaran.json"):
        with open("data_pembayaran.json", "r") as f:
            data_pembayaran = json.load(f)
    else:
        data_pembayaran = {}
    
    return data_kamar, data_pembayaran

def login():
    print("=== Halaman Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    users = load_users(file_path)

    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Login berhasil! Selamat datang, {username}!")
            if user["username"] == "admin":
                print("Anda login sebagai pengelola.")
                tampilan_pembayaran_pengelola()
            elif user["username"] != "admin":
                print("Anda login sebagai penyewa.")
                tampilan_pembayaran_penyewa()
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
    print("Logout berhasil! Sampai jumpa kembali.")
    return None

def main():
    pengguna_saat_ini = None
    while True:
        print("\n=== Pilihan WOY ===")
        print("1. Login")
        print("2. Register")
        if pengguna_saat_ini:
            print("3. Logout")
        pilihan = input("Pilih (angka menu): ").strip()
        if pilihan == '1':
            if pengguna_saat_ini:
                print(f"Anda sudah login sebagai {pengguna_saat_ini['username']}. Silakan logout terlebih dahulu.")
            else:
                pengguna_saat_ini = login()
        elif pilihan == '2':
            if pengguna_saat_ini:
                print(f"Anda sudah login sebagai {pengguna_saat_ini['username']}. Silakan logout terlebih dahulu.")
            else:
                register()
        elif pilihan == '3' and pengguna_saat_ini:
            pengguna_saat_ini = logout()
        elif pilihan == '3' and not pengguna_saat_ini:
            print("Anda belum login, silakan login terlebih dahulu.")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()