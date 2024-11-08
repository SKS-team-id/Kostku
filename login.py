user = { 
    "admin" : "admin1"
}

print("========login=======")
print("belum punya akun? pilih register")
kesempatan = 3 

while True: 
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    if username in user and user[username] == password: 
        print("==================================")
        print("Selamat datang di aplikasi Kostku!")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0 :
            print(f"Username atau password salah kesempatan login anda tersisa {kesempatan}")
        else : 
            print("anda telah mencoba 3 kali login gagal")
#saifulloh fattah bintoro_2408256