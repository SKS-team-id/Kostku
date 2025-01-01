import json
import os
from datetime import datetime

def baca_file_json(nama_file, default_value):
    if os.path.exists(nama_file):
        with open(nama_file, "r") as file:
            return json.load(file)
    return default_value

def simpan_file_json(nama_file, data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data berhasil disimpan ke {nama_file}.")

data_kamar = baca_file_json("data_kamar.json", [])
data_pembayaran = baca_file_json("data_pembayaran.json", {})

def tampilan_pembayaran_pengelola():
    while True:
        print("\n--- Menu Riwayat Pembayaran Pengelola Kost ---\n")
        print("1. Input Pembayaran")
        print("2. Edit data pembayaran")
        print("3. Hapus data pembayaran")
        print("4. lihat data pembayaran")
        print("5. Keluar")
        pilih = input("Pilih Menu: ")
        if not pilih:
            print("Menu masih kosong. Silakan masukkan menu yang ada!")
            continue
        if pilih == "1":
            input_pembayaran()
        elif pilih == "2":
            edit_pembayaran()
        elif pilih == "3":
            hapus_pembayaran()
        elif pilih == "4":
            lihat_riwayat_pembayaran()
        elif pilih == "5":
            print("Anda keluar dari role pengelola.")
            return
        else:
            print("Pilihan tidak ada. Pilih menu yang ada!")

def tampilan_pembayaran_penyewa():
    while True:
        print("\n--- Menu Penyewa ---\n")
        print("1. Lihat Riwayat Pembayaran")
        print("2. Keluar")
        pilihan = input("Pilih menu: ")
        if not pilihan:
            print("Pilihan tidak ada. Pilih menu yang ada.")
            continue
        if pilihan == "1":
            lihat_riwayat_pembayaran()
        elif pilihan == "2":
            print("Keluar dari menu penyewa.")
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def input_pembayaran():
    print("\n=== Input Pembayaran ===\n")
    print("Daftar Kamar Terisi:")
    kamar_terisi = False
    
    for kamar in data_kamar:
        if kamar["status"] == "Terisi":
            kamar_terisi = True
            print(f"Kamar {kamar['id']} - Penyewa: {kamar['penyewa']} - Harga: Rp{kamar['harga']}")
    
    if not kamar_terisi:
        print("Tidak ada kamar yang terisi.")
        return
        
    while True:
        no_kamar = input("\nMasukkan Nomor Kamar: ")
        if not no_kamar.isdigit():
            print("Nomor kamar harus berupa angka dan tidak boleh kosong.")
            continue

        kamar = next((k for k in data_kamar if k["id"] == no_kamar and k["status"] == "Terisi"), None)
        
        if not kamar:
            print("Nomor kamar tidak valid, silakan coba lagi.")
            continue
            
        # Initialize payment history for new room
        if no_kamar not in data_pembayaran:
            data_pembayaran[no_kamar] = []
        
        # Payment details
        nama_penyewa = kamar["penyewa"]

        while True:
            tanggal = input("Tanggal Pembayaran (YYYY-MM-DD): ")   #verifikasi format tanggal
            try:
                datetime.strptime(tanggal, "%Y-%m-%d")
                break #tanggal valid, keluar dari loop
            except ValueError:
                print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD.")
        
        while True:
            try:
                jumlah = input("Jumlah yang Dibayarkan: Rp")
                if not jumlah.isdigit():
                    print("Jumlah harus berupa angka dan tidak boleh kosong.")
                    continue
                break
            except ValueError:
                print("Jumlah tidak valid.")
                
        while True:
            status = input("Status Pembayaran (Lunas/Belum Lunas): ").strip().lower()
            if status == "lunas" or status == "belum lunas":
                status = status.capitalize()
                break
            print("Status harus 'Lunas' atau 'Belum Lunas' dan tidak boleh kosong. Silakan coba lagi.")

        # Add payment record
        pembayaran_baru = {
            "nama_penyewa": nama_penyewa,
            "tanggal": tanggal,
            "jumlah": jumlah,
            "status": status
        }
        
        data_pembayaran[no_kamar].append(pembayaran_baru)
        print(f"\nPembayaran untuk kamar {no_kamar} berhasil dicatat:")
        print(f"Penyewa: {nama_penyewa}")
        print(f"Jumlah: Rp{jumlah}")
        print(f"Status: {status}")
        
        simpan_file_json("data_pembayaran.json", data_pembayaran)
        break

def lihat_riwayat_pembayaran():
    print("\n=== Riwayat Pembayaran ===\n")
    
    while True:
        no_kamar = input("Masukkan Nomor Kamar: ")
        if not no_kamar.isdigit():
            print("Nomor kamar harus berupa angka dan tidak boleh kosong")
            return
        
        if no_kamar not in data_pembayaran:
            print("Belum ada riwayat pembayaran untuk kamar ini.")
            return
        
        print(f"\nRiwayat Pembayaran Kamar {no_kamar}:")
        for pembayaran in data_pembayaran[no_kamar]:
            print("\nDetail Pembayaran:")
            print(f"Tanggal: {pembayaran['tanggal']}")
            print(f"Penyewa: {pembayaran['nama_penyewa']}")
            print(f"Jumlah: Rp{pembayaran['jumlah']}")
            print(f"Status: {pembayaran['status']}")
        break

def edit_pembayaran():
    print("\n=== Edit Pembayaran ===\n")

    while True:
        no_kamar = input("Nomor Kamar: ")
        if not no_kamar.isdigit():
            print("Nomor kamar harus berupa angka dan tidak boleh kosong")
            continue
        if no_kamar not in data_pembayaran or not data_pembayaran[no_kamar]:
            print("Tidak ada riwayat pembayaran untuk kamar ini.")
            return
    
        print(f"\n--- Riwayat Pembayaran untuk Kamar {no_kamar} ---")
        for i, pembayaran in enumerate(data_pembayaran[no_kamar], start=1):
            print(f"{i}. Tanggal: {pembayaran['tanggal']}, Jumlah: {pembayaran['jumlah']}, Status: {pembayaran['status']}")
        
        try:
            pilihan = int(input("\nMasukkan nomor pembayaran yang ingin diedit: ")) - 1
            pembayaran = data_pembayaran[no_kamar][pilihan]
        except (ValueError, IndexError):
            print("Pilihan tidak valid.")
            return

        pembayaran["nama_penyewa"] = input(f"Nama Penyewa [{pembayaran['nama_penyewa']}]: ") or pembayaran["nama_penyewa"]
        
        while True:    
            tanggal = input(f"Tanggal Pembayaran [{pembayaran['tanggal']}]: ") or pembayaran["tanggal"]
            try:
                datetime.strptime(tanggal, "%Y-%m-%d")  # Validasi format tanggal
                pembayaran["tanggal"] = tanggal
                break
            except ValueError:
                print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD.")
            
        try:
            pembayaran["jumlah"] = float(input(f"Jumlah yang Dibayarkan [{pembayaran['jumlah']}]: ") or pembayaran["jumlah"])
        except ValueError:
            print("Jumlah harus berupa angka.")
            return
    
        while True:
            status = input(f"Status Pembayaran [{pembayaran['status']}]: ").strip().lower()
            if status == "lunas" or status == "belum lunas":
                pembayaran["status"] = status.capitalize()
                break
            print("Status harus 'Lunas' atau 'Belum Lunas'. Silakan coba lagi.")

        print("Riwayat pembayaran berhasil diperbarui.")
        simpan_file_json("data_pembayaran.json", data_pembayaran)

def hapus_pembayaran():
    print("\n=== Hapus Pembayaran ===\n")

    while True:
        no_kamar = input("Nomor Kamar: ")
        if not no_kamar.isdigit():
            print("Nomor kamar harus berupa angka dan tidak boleh kosong")
            continue
        if no_kamar not in data_pembayaran or not data_pembayaran[no_kamar]:
            print("Tidak ada riwayat pembayaran untuk kamar ini.")
            return
        
        print(f"\n--- Riwayat Pembayaran untuk Kamar {no_kamar} ---")
        for i, pembayaran in enumerate(data_pembayaran[no_kamar], start=1):
            print(f"{i}. Tanggal: {pembayaran['tanggal']}, Jumlah: {pembayaran['jumlah']}, Status: {pembayaran['status']}")
        
        try:
            pilihan = int(input("\nMasukkan nomor pembayaran yang ingin dihapus: ")) - 1
            pembayaran = data_pembayaran[no_kamar].pop(pilihan)
        except (ValueError, IndexError):
            print("Pilihan tidak valid.")
            return

        print(f"Riwayat pembayaran tanggal {pembayaran['tanggal']} berhasil dihapus.")
        simpan_file_json("data_pembayaran.json", data_pembayaran)
        break