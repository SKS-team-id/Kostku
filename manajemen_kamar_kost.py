# Program Manajemen Kamar Kost
# Data awal: 10 kamar kosong
data_kamar = [
    {"id": f"00{i}", "penyewa": "", "telepon": "", "alamat": "", "harga": 0, "status": "Kosong"}
    for i in range(1, 41)
]

def tampilkan_menu():
    print("\n--- Menu Pengelola Kost ---")
    print("1. Tambah Kamar")
    print("2. Hapus Kamar")
    print("3. Data Kamar")
    print("4. Keluar")

def tambah_kamar():
    print("\n--- Tambah Kamar ---")
    kamar_baru = input("Masukkan ID kamar baru (contoh: 011): ")
    if any(k["id"] == kamar_baru for k in data_kamar):
        print("ID kamar sudah ada.")
    else:
        data_kamar.append({"id": kamar_baru, "penyewa": "", "telepon": "", "alamat": "", "harga": 0, "status": "Kosong"})
        print(f"Kamar {kamar_baru} berhasil ditambahkan.")

def hapus_kamar():
    print("\n--- Hapus Kamar ---")
    print("Daftar Kamar:")
    for kamar in data_kamar:
        print(f"Kamar {kamar['id']} - Status: {kamar['status']}")
    kamar_id = input("Masukkan ID kamar yang ingin dihapus: ")
    for kamar in data_kamar:
        if kamar["id"] == kamar_id:
            data_kamar.remove(kamar)
            print(f"Kamar {kamar_id} berhasil dihapus.")
            return
    print("Kamar tidak ditemukan.")

def data_kamar_menu():
    print("\n--- Data Kamar ---")
    for kamar in data_kamar:
        print(f"Kamar {kamar['id']} - Status: {kamar['status']}")
    kamar_id = input("Masukkan ID kamar untuk melihat detail atau tekan Enter untuk kembali: ")
    for kamar in data_kamar:
        if kamar["id"] == kamar_id:
            while True:
                print(f"\n--- Menu Kamar {kamar_id} ---")
                print("1. Input Data Kamar")
                print("2. Edit Data Kamar")
                print("3. Lihat Data Kamar")
                print("4. Kembali")
                pilihan = input("Pilih menu: ")
                if pilihan == "1":
                    if kamar["status"] == "Kosong":
                        input_data_kamar(kamar)
                    else:
                        print("Data sudah tersedia, silakan lakukan edit data kamar.")
                elif pilihan == "2":
                    if kamar["status"] == "Kosong":
                        print("Data kamar masih kosong, tidak bisa melakukan modifikasi.")
                    else:
                        edit_data_kamar(kamar)
                elif pilihan == "3":
                    lihat_data_kamar(kamar)
                elif pilihan == "4":
                    return  # Kembali ke daftar kamar
                else:
                    print("Pilihan tidak valid.")
            return
    if kamar_id:
        print("Kamar tidak ditemukan.")

def input_data_kamar(kamar):
    print(f"\n--- Input Data Kamar {kamar['id']} ---")
    kamar["penyewa"] = input("Masukkan nama penyewa: ")
    kamar["telepon"] = input("Masukkan nomor telepon penyewa: ")
    kamar["alamat"] = input("Masukkan alamat penyewa: ")
    kamar["harga"] = int(input("Masukkan harga kamar: "))
    status = input("Masukkan status kamar (True untuk Terisi): ").capitalize()
    if status == "True":
        kamar["status"] = "Terisi"
        print(f"Data kamar {kamar['id']} berhasil diinput.")
    else:
        print("Status tidak valid. Hanya bisa mengisi status dengan True.")

def edit_data_kamar(kamar):
    print(f"\n--- Edit Data Kamar {kamar['id']} ---")
    kamar["penyewa"] = input(f"Nama penyewa [{kamar['penyewa']}]: ") or kamar["penyewa"]
    kamar["telepon"] = input(f"Nomor telepon [{kamar['telepon']}]: ") or kamar["telepon"]
    kamar["alamat"] = input(f"Alamat [{kamar['alamat']}]: ") or kamar["alamat"]
    kamar["harga"] = input(f"Harga kamar [{kamar['harga']}]: ")
    kamar["harga"] = int(kamar["harga"]) if kamar["harga"] else kamar["harga"]
    status = input(f"Status kamar (True untuk Terisi / False untuk Kosong) [{kamar['status']}]: ").capitalize()
    if status == "True":
        kamar["status"] = "Terisi"
    elif status == "False":
        kamar["status"] = "Kosong"
        kamar["penyewa"] = ""
        kamar["telepon"] = ""
        kamar["alamat"] = ""
        kamar["harga"] = 0
        print("Data kamar telah dihapus. Kamar kembali menjadi kosong.")
    else:
        print("Status tidak valid. Status tetap seperti sebelumnya.")
    print(f"Data kamar {kamar['id']} berhasil diperbarui.")

def lihat_data_kamar(kamar):
    if kamar["status"] == "Kosong":
        print("Data kamar masih kosong, silakan lakukan input data kamar terlebih dahulu.")
    else:
        print(f"\n--- Detail Kamar {kamar['id']} ---")
        print(f"Penyewa: {kamar['penyewa']}")
        print(f"Telepon: {kamar['telepon']}")
        print(f"Alamat: {kamar['alamat']}")
        print(f"Harga: {kamar['harga']}")
        print(f"Status: {kamar['status']}")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_kamar()
    elif pilihan == "2":
        hapus_kamar()
    elif pilihan == "3":
        data_kamar_menu()
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
