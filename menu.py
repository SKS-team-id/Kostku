# Data simulasi untuk menyimpan akun
akun = {}


def login():
    print("=== Halaman Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in akun and akun[username]['password'] == password:
        print("Login berhasil! Selamat datang di aplikasi Kostku!")
        return username
    else:
        print("Login gagal! Username atau password salah.")

def register():
    print("\n=== Halaman Register ===")
    username = input("Masukkan username baru: ")
    
    if username in akun:
        print("Username sudah digunakan, silakan coba lagi.")
        return  # Keluar dari fungsi register jika username sudah ada
    password = input("Masukkan password: ")
    kode = input("Masukkan kode referal: ")

    if kode == "kostku1" :
        akun[username] = {'password': password}
        print("Registrasi berhasil! Silakan login.")
    else : 
        print("Kode referal salah, silakan coba lagi.")

def main():
    while True:
        print("\n=== Pilihan Menu ===")
        print("a. Login")
        print("b. Register")
        pilihan = input("Pilih (a/b): ").lower()
        
        if pilihan == 'a':
            login()
        elif pilihan == 'b':
            register()
        else:
            print("Pilihan tidak valid, silakan pilih 'a' atau 'b'.")

# Memulai program utama
main()
