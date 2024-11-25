data_kamar = [
    {"id": f"{i:03}", "penyewa": "", "telepon": "", "alamat": "", "harga": 0, "status": "Kosong", "fasilitas": []}
    for i in range(1, 41)
]

def tampilkan_menu_pengelola():
    print("\n--- Menu Pengelola Kost ---")
    print("1. Tambah Kamar")
    print("2. Hapus Kamar")
    print("3. Data Kamar")
    print("4. Keluar")

def tampilkan_menu_penyewa():
    print("\n--- Menu Penyewa ---")
    print("1. Lihat Data Kamar")
    print("2. Pilih Kamar")
    print("3. Keluar")

def tambah_kamar():
    print("\n--- Tambah Kamar ---")
    kamar_baru = input("Masukkan Nomor kamar baru (contoh: 001): ")
    if any(k["id"] == kamar_baru for k in data_kamar):
        print("Nomor kamar sudah ada.")
    else:
        data_kamar.append({"id": kamar_baru, "penyewa": "", "telepon": "", "alamat": "", "harga": 0, "status": "Kosong", "fasilitas": []})
        data_kamar.sort(key=lambda x: int(x['id']))
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
                print("4. Kelola Fasilitas")
                print("5. Kembali")
                pilihan = input("Pilih menu: ")
                if pilihan == "1":                    
                    input_data_kamar(kamar)
                elif pilihan == "2":
                    if kamar["status"] == "Terisi":  # Cek status kamar sebelum edit
                        edit_data_kamar(kamar)
                    else:
                        print("Kamar belum terisi. Edit data hanya bisa dilakukan jika kamar terisi.")
                elif pilihan == "3":
                    lihat_data_kamar(kamar)
                elif pilihan == "4":
                    kelola_fasilitas_kamar(kamar)
                elif pilihan == "5":
                    return
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
    print(f"\n--- Detail Kamar {kamar['id']} ---")
    print(f"Penyewa: {kamar['penyewa']}")
    print(f"Telepon: {kamar['telepon']}")
    print(f"Alamat: {kamar['alamat']}")
    print(f"Harga: {kamar['harga']}")
    print(f"Status: {kamar['status']}")
    print(f"Fasilitas: {', '.join(kamar['fasilitas']) if kamar['fasilitas'] else 'Tidak ada fasilitas'}")

def kelola_fasilitas_kamar(kamar):
    print(f"\n--- Kelola Fasilitas Kamar {kamar['id']} ---")
    print("Fasilitas saat ini:", ", ".join(kamar["fasilitas"]) if kamar["fasilitas"] else "Belum ada fasilitas")
    print("1. Tambah Fasilitas")
    print("2. Hapus Fasilitas")
    print("3. Kembali")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        fasilitas_baru = input("Masukkan fasilitas baru (pisahkan dengan koma untuk lebih dari satu): ").split(", ")
        kamar["fasilitas"].extend(fasilitas_baru)
        print("Fasilitas berhasil ditambahkan.")
    elif pilihan == "2":
        fasilitas_hapus = input("Masukkan fasilitas yang ingin dihapus: ")
        if fasilitas_hapus in kamar["fasilitas"]:
            kamar["fasilitas"].remove(fasilitas_hapus)
            print("Fasilitas berhasil dihapus.")
        else:
            print("Fasilitas tidak ditemukan.")
    elif pilihan == "3":
        return
    else:
        print("Pilihan tidak valid.")

def lihat_data_kamar_penyewa():
    print("\n--- Data Kamar ---")
    for kamar in data_kamar:
        print(f"Kamar {kamar['id']:<5} | Status: {kamar['status']:<10} | Harga: Rp{kamar['harga']:<10} | Fasilitas: {', '.join(kamar['fasilitas']) if kamar['fasilitas'] else 'Tidak ada'}")

def pilih_kamar_penyewa():
    print("\n--- Pilih Kamar ---")
    # Cek apakah penyewa sudah memilih kamar sebelumnya
    for kamar in data_kamar:
        if kamar["status"] == "Dipilih":
            print("Anda sudah memilih kamar. Tidak dapat memilih kamar lain.")
            return  # Keluar dari fungsi jika sudah ada kamar yang dipilih
    
    for kamar in data_kamar:
        print(f"Kamar {kamar['id']} - Status: {kamar['status']}")
    
    kamar_id = input("Masukkan ID kamar yang ingin dipilih: ")
    for kamar in data_kamar:
        if kamar["id"] == kamar_id:
            if kamar["status"] == "Kosong":
                kamar["status"] = "Dipilih"
                print(f"Kamar {kamar_id} berhasil dipilih. Silakan melanjutkan proses dengan pengelola.")
            else:
                print("Maaf, kamar ini sudah terisi atau dipilih.")
            return
    print("Kamar tidak ditemukan.")


# Program utama
while True:
    print("\n--- Sistem Manajemen Kost ---")
    print("1. Login sebagai Pengelola")
    print("2. Login sebagai Penyewa")
    print("3. Keluar")
    role = input("Pilih role: ")
    if role == "1":
        while True:
            tampilkan_menu_pengelola()
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                tambah_kamar()
            elif pilihan == "2":
                hapus_kamar()
            elif pilihan == "3":
                data_kamar_menu()
            elif pilihan == "4":
                print("Keluar dari mode pengelola.")
                break
            else:
                print("Pilihan tidak valid.")
    elif role == "2":
        while True:
            tampilkan_menu_penyewa()
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                lihat_data_kamar_penyewa()
            elif pilihan == "2":
                pilih_kamar_penyewa()
            elif pilihan == "3":
                print("Keluar dari mode penyewa.")
                break
            else:
                print("Pilihan tidak valid.")
    elif role == "3":
        print("Program berakhir. Terima kasih!")
        break
    else:
        print("Role tidak valid.")