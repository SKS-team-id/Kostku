import json
import os
from datetime import datetime

def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def simpan_ke_json():
    with open("data_kamar.json", "w") as file:
        json.dump(data_kamar, file, indent=4)
    print("Data berhasil disimpan ke file JSON.")

def baca_dari_json():
    global data_kamar
    if os.path.exists('data_kamar.json'):
        with open('data_kamar.json', 'r') as file:
            return json.load(file)
    else:
        return []

data_kamar = baca_dari_json()

def simpan_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            return json.load(file)
    return []

def tampilkan_menu_pengelola(user):
    while True:
        print("\n=== Menu Pengelola ===")
        print("1. Tambah Kamar")
        print("2. Hapus Kamar")
        print("3. Data Kamar")
        print("4. Riwayat Pembayaran")
        print("5. Keluar")
        pilih = input("Pilih Menu: ")

        if not pilih:
            print("Menu masih kosong, silakan masukkan menu yang ada!")
            continue

        if pilih == "1":
            tambah_kamar(user)
        elif pilih == "2":
            hapus_kamar(user)
        elif pilih == "3":
            data_kamar_menu(user)
        elif pilih == "4":
            from riwayat_pembayaran import tampilan_pembayaran_pengelola
            tampilan_pembayaran_pengelola(user)
        elif pilih == "5":
            from menu import main
            print("Anda keluar dari role pengelola")
            main()
            
            break
        else:
            print("Pilihan tidak ada. Pilih menu yang ada")

def tampilkan_menu_penyewa(user):
    while True:
        print("\n--- Menu Penyewa ---")
        print("1. Lihat Data Kamar")
        print("2. Pilih Kamar")
        print("3. Lihat Riwayat Pembayaran")
        print("4. Keluar")
        pilih = input("Pilih Menu: ")

        if not pilih:
            print("Menu masih kosong, silakan masukkan menu yang ada!")
            continue

        if pilih == "1":
            lihat_data_kamar_penyewa(user)
        elif pilih == "2":
            if user["room_id"]:
                print("Anda sudah memilih kamar. Tidak dapat mengganti kamar.")
            else:
                pilih_kamar_penyewa(user)
        elif pilih == "3":
            from riwayat_pembayaran import lihat_riwayat_pembayaran
            lihat_riwayat_pembayaran(user) 
        elif pilih == "4":
            from menu import main
            print("Anda keluar dari role penyewa")
            main() 
        else:
            print("Silahkan pilih menu yang ada.")
            tampilkan_menu_penyewa(user)

def tambah_kamar(user):
    print("\n--- Tambah Kamar ---")
    while True:
        kamar_baru = input("Masukkan Nomor kamar baru (3 digit, contoh: 001) atau ENTER untuk kembali: ")
        if not kamar_baru:
            print("Kembali ke menu pengelola")
            tampilkan_menu_pengelola(user)
            continue
        if not kamar_baru.isdigit():
            print("Input tidak valid. Nomor kamar harus berupa angka.")
            return
        if len(kamar_baru) != 3:
            print("Input tidak valid. Nomor kamar harus terdiri dari 3 digit.")
            continue
        if any(k["id"] == kamar_baru for k in data_kamar):
            print("Nomor kamar sudah ada.")
            return
        data_kamar.append({"id": kamar_baru, "penyewa": "", "telepon": "", "alamat": "", "harga": 0, "status": "Kosong", "fasilitas": []})
        data_kamar.sort(key=lambda x: int(x['id']))
        print(f"Kamar {kamar_baru} berhasil ditambahkan.")
        simpan_ke_json()
        break

def hapus_kamar(user):
    print("\n--- Hapus Kamar ---")
    print("Daftar Kamar:")
    while True:
        for kamar in data_kamar:

            print(f"Kamar {kamar['id']} - Status: {kamar['status']}")
        kamar_id = input("Masukkan ID kamar yang ingin dihapus atau ENTER untuk kembali: ")
        if not kamar_id:
            print("Kembali ke menu pengelola")
            tampilkan_menu_pengelola(user)
            continue

        if not kamar_id.isdigit():
            print("Input tidak valid. Nomor kamar harus berupa angka.")
            continue

        kamar_ditemukan = False
        for kamar in data_kamar:
            if kamar["id"] == kamar_id:
                kamar_ditemukan = True
                if kamar["status"] == "Kosong":
                    data_kamar.remove(kamar)
                    print(f"Kamar {kamar_id} berhasil dihapus.")
                    simpan_ke_json()
                else:
                    print(f"Kamar {kamar_id} tidak dapat dihapus karena statusnya masih 'Terisi'.")
                break
    
        if not kamar_ditemukan:
            print("Kamar tidak ditemukan.")

def data_kamar_menu(user):
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
                if not pilihan:
                    print("Menu masih kosong, silakan masukkan menu yang ada!")
                    return
                if pilihan == "1":                    
                    input_data_kamar(kamar)
                elif pilihan == "2":
                    if kamar["status"] == "Terisi":
                        edit_data_kamar(kamar)
                    else:
                        print("Kamar belum terisi. Edit data hanya bisa dilakukan jika kamar terisi.")
                elif pilihan == "3":
                    lihat_data_kamar(kamar)
                elif pilihan == "4":
                    kelola_fasilitas_kamar(kamar)
                elif pilihan == "5":
                    tampilkan_menu_pengelola(user)
                else:
                    print("Pilihan tidak ada. Pilih menu yang ada.")
                return
    if kamar_id:
        print("Kamar tidak ditemukan.")

def input_data_kamar(kamar):
    print(f"\n--- Input Data Kamar {kamar['id']} ---")
    print("Setiap inputan tidak boleh kosong!")

    while True:
        penyewa = input("Masukkan nama penyewa: ").strip()
        if not penyewa:
            print("Inputan tidak boleh kosong!")
            continue
        if all(char.isalpha() or char.isspace() for char in penyewa):
            kamar["penyewa"] = penyewa
            break
        else:
            print("Nama penyewa hanya boleh diisi huruf.")

    while True:
        telepon = input("Masukkan nomor telepon penyewa: ").strip()
        if not telepon:
            print("Inputan tidak boleh kosong!")
            continue
        if telepon.isdigit():
            kamar["telepon"] = int(telepon)
            break
        else:
            print("Nomor telepon hanya boleh mengandung angka.")

    while True:
        alamat = input("Masukkan alamat penyewa: ").strip()
        if not alamat:
            print("Inputan tidak boleh kosong!")
            continue
        kamar["alamat"] = alamat
        break

    while True:
        harga = input("Masukkan harga kamar: ").strip()
        if not harga:
            print("Inputan tidak boleh kosong!")
            continue
        if harga.isdigit():
            kamar["harga"] = int(harga)
            break
        else:
            print("Harga harus berupa angka.")
    while True:
        tanggal_mulai = input("Masukkan tanggal mulai sewa (YYYY-MM-DD): ").strip()
        if not tanggal_mulai:
            print("Inputan tidak boleh kosong!")
            continue
        if not validate_date(tanggal_mulai):
            print("Format tanggal tidak valid! Gunakan format YYYY-MM-DD")
            continue
        kamar["tanggal_mulai"] = tanggal_mulai
        break

    while True:
        tanggal_akhir = input("Masukkan tanggal berakhir sewa (YYYY-MM-DD): ").strip()
        if not tanggal_akhir:
            print("Inputan tidak boleh kosong!")
            continue
        if not validate_date(tanggal_akhir):
            print("Format tanggal tidak valid! Gunakan format YYYY-MM-DD")
            continue
        
        tgl_mulai = [int(x) for x in tanggal_mulai.split('-')]
        tgl_akhir = [int(x) for x in tanggal_akhir.split('-')]
        
        if tgl_akhir[0] < tgl_mulai[0] or \
        (tgl_akhir[0] == tgl_mulai[0] and tgl_akhir[1] < tgl_mulai[1]) or \
        (tgl_akhir[0] == tgl_mulai[0] and tgl_akhir[1] == tgl_mulai[1] and tgl_akhir[2] <= tgl_mulai[2]):
            print("Tanggal akhir harus setelah tanggal mulai!")
            continue
            
        kamar["tanggal_akhir"] = tanggal_akhir
        break
    
    kamar["status"] = "Terisi"
    print(f"Data kamar {kamar['id']} berhasil diinput.")
    simpan_ke_json()

def edit_data_kamar(kamar):
    print(f"\n--- Edit Data Kamar {kamar['id']} ---")
    
    while True:
        penyewa = input(f"Nama penyewa [{kamar['penyewa']}] (ENTER jika tidak diubah):").strip()
        if not penyewa:
            break
        if all(char.isalpha() or char.isspace() for char in penyewa):
            kamar["penyewa"] = penyewa
            break
        print("Nama penyewa hanya boleh diisi huruf.")

    while True:
        telepon = input(f"Nomor telepon [{kamar['telepon']}] (ENTER jika tidak diubah):").strip()
        if not telepon:
            break
        if telepon.isdigit():
            kamar["telepon"] = int(telepon)
            break
        print("Nomor telepon hanya boleh mengandung angka.")

    while True:
        alamat_baru = input(f"Masukkan alamat penyewa[{kamar['alamat']}] (ENTER jika tidak diubah): ").strip()
        if alamat_baru:
            kamar["alamat"] = alamat_baru
        break

    while True:
        harga = input(f"Harga kamar [{kamar['harga']}] (ENTER jika tidak diubah): ").strip()
        if not harga: 
            break
        if harga.isdigit():
            kamar["harga"] = int(harga)
            break
        print("Harga harus berupa angka.")

    while True:
        tanggal_mulai = input(f"Tanggal Mulai Sewa [{kamar['tanggal_mulai']}] (YYYY-MM-DD, ENTER jika tidak diubah): ").strip()
        if not tanggal_mulai:
            break
        if validate_date(tanggal_mulai):
            kamar["tanggal_mulai"] = tanggal_mulai
            break
        print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD.")

    while True:
        tanggal_akhir = input(f"Tanggal Akhir Sewa [{kamar['tanggal_akhir']}] (YYYY-MM-DD, ENTER jika tidak diubah): ").strip()
        if not tanggal_akhir:
            break
        if validate_date(tanggal_akhir):
            kamar["tanggal_akhir"] = tanggal_akhir
            break
        print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD.")

    while True:
        status = input(f"Status kamar (Enter untuk terisi dan False untuk kosong) [{kamar['status']}] : ").capitalize().strip()
        if not status:
            break
        if status == "True":
            kamar["status"] = "Terisi"
            break
        elif status == "False":
            kamar["status"] = "Kosong"
            kamar["penyewa"] = ""
            kamar["telepon"] = ""
            kamar["alamat"] = ""
            kamar["harga"] = 0
            kamar["tanggal_mulai"] = ""
            kamar["tanggal_akhir"] = ""
            print("Data kamar telah dihapus. Kamar kembali menjadi kosong.")
            break
        print("Status tidak valid. Masukkan True atau False.")
    
    print(f"Data kamar {kamar['id']} berhasil diperbarui.")
    simpan_ke_json()

def lihat_data_kamar(kamar):
    print(f"\n--- Detail Kamar {kamar['id']} ---")
    print(f"Penyewa: {kamar['penyewa'] if kamar['penyewa'] else 'Belum ada penyewa'}")
    print(f"Telepon: {kamar['telepon'] if kamar['telepon'] else 'Belum ada data telepon'}")
    print(f"Alamat: {kamar['alamat'] if kamar['alamat'] else 'Belum ada data alamat'}")
    print(f"Harga: Rp{kamar['harga'] if kamar['harga'] else 'Belum ditentukan'}")
    print(f"Status: {kamar['status']}")
    print(f"Tanggal Mulai Sewa: {kamar['tanggal_mulai'] if 'tanggal_mulai' in kamar and kamar['tanggal_mulai'] else 'Belum ditentukan'}")
    print(f"Tanggal Akhir Sewa: {kamar['tanggal_akhir'] if 'tanggal_akhir' in kamar and kamar['tanggal_akhir'] else 'Belum ditentukan'}")
    print(f"Fasilitas: {', '.join(kamar['fasilitas']) if kamar['fasilitas'] else 'Tidak ada fasilitas'}")
    tampilkan_menu_pengelola(kamar)

def kelola_fasilitas_kamar(kamar):
    print(f"\n--- Kelola Fasilitas Kamar {kamar['id']} ---")
    print("Fasilitas saat ini:", ", ".join(kamar["fasilitas"]) if kamar["fasilitas"] else "Belum ada fasilitas")
    print("1. Tambah Fasilitas")
    print("2. Edit Fasilitas")
    print("3. Hapus Fasilitas")
    print("4. Kembali")

    pilihan = input("Pilih menu: ").strip()

    while True:
        if pilihan == "1":
            fasilitas_baru = input("Masukkan fasilitas baru (pisahkan dengan koma untuk lebih dari satu) atau ENTER untuk kembali: ").strip()
            if not all(char.isalpha() or char.isspace() or char == ',' for char in fasilitas_baru):
                print("Fasilitas hanya boleh diisi huruf.")
                continue
            kamar["fasilitas"].extend(fasilitas_baru.split(", "))
            print("Fasilitas berhasil ditambahkan.")
            simpan_ke_json()
            break
        
    while True:
        if pilihan == "2":
            edit_fasilitas_kamar(kamar)
        if pilihan == "3":
            hapus_fasilitas_kamar(kamar)
        elif pilihan == "4":
            data_kamar_menu(kamar)
        else:
            print("Pilihan tidak valid atau kosong.")
            kelola_fasilitas_kamar(kamar)

def hapus_fasilitas_kamar(kamar):
    if not kamar["fasilitas"]:
        print("Tidak ada fasilitas untuk dihapus.")
        kelola_fasilitas_kamar(kamar)
        return

    while True:
        fasilitas_hapus = input("Masukkan nama fasilitas yang ingin dihapus (ENTER untuk kembali): ").strip()
        if not fasilitas_hapus:
            print("Anda belum memasukan nama fasilitas")
            kelola_fasilitas_kamar(kamar)
            return

        if fasilitas_hapus in kamar["fasilitas"]:
            kamar["fasilitas"].remove(fasilitas_hapus)
            print("Fasilitas berhasil dihapus.")
            simpan_ke_json()
            kelola_fasilitas_kamar(kamar)
            return
        else:
            print("Fasilitas tidak ditemukan.")

def edit_fasilitas_kamar(kamar):
    if not kamar["fasilitas"]:
        print("Tidak ada fasilitas untuk diedit.")
        kelola_fasilitas_kamar(kamar)
        return

    while True:
        print("\n--- Edit Fasilitas ---")
        for i, fasilitas in enumerate(kamar["fasilitas"], start=1):
            print(f"{i}. {fasilitas}")

        nomor_input = input("Pilih nomor fasilitas yang ingin diedit: ").strip()

        if not nomor_input:
            print("Pilihan tidak ada atau Anda belum memilih fasilitas.")
            kelola_fasilitas_kamar(kamar)

        try:
            nomor_edit = int(nomor_input)
            if 1 <= nomor_edit <= len(kamar["fasilitas"]):
                fasilitas_lama = kamar["fasilitas"][nomor_edit - 1]
                fasilitas_baru = input(f"Masukkan fasilitas baru untuk mengganti '{fasilitas_lama}' (ENTER untuk batal): ").strip()
                if not fasilitas_baru:
                    print("Perubahan dibatalkan.")
                    continue

                kamar["fasilitas"][nomor_edit - 1] = fasilitas_baru
                print("Fasilitas berhasil diperbarui.")
                simpan_ke_json()
                kelola_fasilitas_kamar(kamar)
                return
            else:
                print("Pilihan tidak ada atau Anda belum memilih fasilitas.")
                kelola_fasilitas_kamar(kamar)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

def lihat_data_kamar_penyewa(user):
    print("\n--- Data Kamar Anda ---")
    if user["room_id"]:
        kamar = next((k for k in data_kamar if k["id"] == user["room_id"]), None)
        if kamar:
            print(f"Kamar {kamar['id']} - Status: {kamar['status']}")
            print(f"Penyewa: {kamar['penyewa'] if kamar['penyewa'] else 'Belum ada penyewa'}")
            print(f"Telepon: {kamar['telepon'] if kamar['telepon'] else 'Belum ada data telepon'}")
            print(f"Alamat: {kamar['alamat'] if kamar['alamat'] else 'Belum ada data alamat'}")
            print(f"Harga: Rp{kamar['harga'] if kamar['harga'] else 'Belum ditentukan'}")
            print(f"Tanggal Mulai Sewa: {kamar['tanggal_mulai'] if 'tanggal_mulai' in kamar and kamar['tanggal_mulai'] else 'Belum ditentukan'}")
            print(f"Tanggal Akhir Sewa: {kamar['tanggal_akhir'] if 'tanggal_akhir' in kamar and kamar['tanggal_akhir'] else 'Belum ditentukan'}")
            print(f"Fasilitas: {', '.join(kamar['fasilitas']) if kamar['fasilitas'] else 'Tidak ada fasilitas'}")
        else:
            print("Kamar tidak ditemukan.")
    else:
        print("Anda belum memilih kamar.")
    tampilkan_menu_penyewa(user)

def pilih_kamar_penyewa(user):
    print("\n--- Pilih Kamar ---")
    
    if "room_id" in user and user["room_id"]:
        print(f"Anda sudah memilih kamar dengan ID {user['room_id']}. Anda tidak dapat memilih kamar lagi.")
        tampilkan_menu_penyewa(user)
        return
    
    ada_kamar_kosong = False
    for kamar in data_kamar:
        if kamar['status'] == 'Kosong':
            ada_kamar_kosong = True
            print(f"Kamar {kamar['id']:<5} | Status: {kamar['status']:<10} | Harga: Rp{kamar['harga']:<10} | Fasilitas: {', '.join(kamar['fasilitas']) if kamar['fasilitas'] else 'Tidak ada'}")
    
    if not ada_kamar_kosong:
        print("Tidak ada kamar kosong saat ini.")
        tampilkan_menu_penyewa(user)
        return
    
    kamar_id = input("Masukkan ID kamar yang ingin dipilih atau tekan ENTER untuk kembali: ")
    if not kamar_id:
        tampilkan_menu_penyewa(user)
        return
    
    kamar_ditemukan = False
    for kamar in data_kamar:
        if kamar["id"] == kamar_id:
            kamar_ditemukan = True
            if kamar["status"] == "Kosong":
                kamar["status"] = "Dipilih"
                user["room_id"] = kamar_id
                print(f"Kamar {kamar_id} berhasil dipilih. Silakan melanjutkan proses dengan pengelola.")
                simpan_ke_json()  # Simpan perubahan ke data kamar
                users = load_users()
                for u in users:
                    if u["username"] == user["username"]:
                        u["room_id"] = kamar_id
                simpan_users(users)  # Simpan perubahan ke data pengguna
                tampilkan_menu_penyewa(user)
            elif kamar["status"] == "Dipilih":
                print(f"Kamar {kamar_id} sudah dalam status 'Dipilih'. Anda dapat melanjutkan proses dengan pengelola.")
            else:
                print("Maaf, kamar ini sudah terisi.")
            break
    
    if not kamar_ditemukan:
        print("Maaf, kamar yang Anda pilih tidak ada. Silakan pilih kamar yang ada.")
        tampilkan_menu_penyewa(user)
