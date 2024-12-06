import json
import os

riwayat_pembayaran = {}
file_json = 'riwayat_pembayaran.json'

# Fungsi untuk memuat data dari file JSON
def muat_data():
    global riwayat_pembayaran
    if os.path.exists(file_json):
        with open(file_json, 'r') as file:
            try:
                riwayat_pembayaran = json.load(file)
            except json.JSONDecodeError:
                riwayat_pembayaran = {}

# Fungsi untuk menyimpan data ke file JSON
def simpan_data():
    with open(file_json, 'w') as file:
        json.dump(riwayat_pembayaran, file, indent=4)

# Fungsi input riwayat pembayaran
def input_pembayaran():
    no_kamar = input("Nomor Kamar: ")
    if no_kamar not in riwayat_pembayaran:
        riwayat_pembayaran[no_kamar] = []

    nama_penyewa = input("Nama Penyewa: ")
    tanggal = input("Tanggal Pembayaran (YYYY-MM-DD): ")
    jumlah = float(input("Jumlah yang Dibayarkan: "))
    status = input("Status Pembayaran (Lunas/Belum Lunas): ").capitalize()

    riwayat_pembayaran[no_kamar].append({
        "nama_penyewa": nama_penyewa,
        "tanggal": tanggal,
        "jumlah": jumlah,
        "status": status
    })
    simpan_data()
    print(f"Riwayat pembayaran untuk kamar {no_kamar} berhasil ditambahkan.")

# Fungsi edit riwayat pembayaran berdasarkan nomor kamar dan tanggal
def edit_pembayaran():
    no_kamar = input("Nomor Kamar: ")
    if no_kamar not in riwayat_pembayaran or not riwayat_pembayaran[no_kamar]:
        print("Tidak ada riwayat pembayaran untuk kamar ini.")
        return
    
    print(f"\nRiwayat Pembayaran untuk Kamar {no_kamar}:")
    for i, pembayaran in enumerate(riwayat_pembayaran[no_kamar], start=1):
        print(f"{i}. Tanggal: {pembayaran['tanggal']}, Jumlah: {pembayaran['jumlah']}, Status: {pembayaran['status']}")
    
    tanggal_edit = input("\nMasukkan tanggal pembayaran yang ingin diedit: ")
    pembayaran_ditemukan = False
    
    for pembayaran in riwayat_pembayaran[no_kamar]:
        if pembayaran["tanggal"] == tanggal_edit:
            pembayaran["nama_penyewa"] = input(f"Nama Penyewa [{pembayaran['nama_penyewa']}]: ") or pembayaran["nama_penyewa"]
            pembayaran["tanggal"] = input(f"Tanggal Pembayaran [{pembayaran['tanggal']}]: ") or pembayaran["tanggal"]
            pembayaran["jumlah"] = float(input(f"Jumlah yang Dibayarkan [{pembayaran['jumlah']}]: ") or pembayaran["jumlah"])
            pembayaran["status"] = input(f"Status Pembayaran [{pembayaran['status']}]: ").capitalize() or pembayaran["status"]
            simpan_data()
            print("Riwayat pembayaran berhasil diperbarui.")
            pembayaran_ditemukan = True
            break
    
    if not pembayaran_ditemukan:
        print("Tanggal pembayaran tidak ditemukan.")

# Fungsi hapus riwayat pembayaran berdasarkan nomor kamar dan tanggal
def hapus_pembayaran():
    no_kamar = input("Nomor Kamar: ")
    if no_kamar not in riwayat_pembayaran or not riwayat_pembayaran[no_kamar]:
        print("Tidak ada riwayat pembayaran untuk kamar ini.")
        return
    
    print(f"\nRiwayat Pembayaran untuk Kamar {no_kamar}:")
    for i, pembayaran in enumerate(riwayat_pembayaran[no_kamar], start=1):
        print(f"{i}. Tanggal: {pembayaran['tanggal']}, Jumlah: {pembayaran['jumlah']}, Status: {pembayaran['status']}")
    
    tanggal_hapus = input("\nMasukkan tanggal pembayaran yang ingin dihapus: ")
    pembayaran_ditemukan = False
    
    for i, pembayaran in enumerate(riwayat_pembayaran[no_kamar]):
        if pembayaran["tanggal"] == tanggal_hapus:
            riwayat_pembayaran[no_kamar].pop(i)
            simpan_data()
            print(f"Riwayat pembayaran tanggal {tanggal_hapus} berhasil dihapus.")
            pembayaran_ditemukan = True
            break
    
    if not pembayaran_ditemukan:
        print("Tanggal pembayaran tidak ditemukan.")

# Fungsi lihat riwayat pembayaran berdasarkan nomor kamar
def lihat_riwayat_pembayaran():
    no_kamar = input("Nomor Kamar: ")
    if no_kamar not in riwayat_pembayaran or not riwayat_pembayaran[no_kamar]:
        print("Belum ada riwayat pembayaran untuk kamar ini.")
        return
    
    print(f"\n--- Riwayat Pembayaran untuk Kamar {no_kamar} ---")
    for pembayaran in riwayat_pembayaran[no_kamar]:
        print(f"Nama Penyewa: {pembayaran['nama_penyewa']} | Tanggal: {pembayaran['tanggal']} | Jumlah: Rp{pembayaran['jumlah']} | Status: {pembayaran['status']}")
        print("-" * 50)

# Program utama
muat_data()
while True:
    print("\n--- Sistem Manajemen Pembayaran Kost ---")
    print("1. Login sebagai Pengelola")
    print("2. Login sebagai Penyewa")
    print("3. Keluar")
    
    role = input("Pilih role: ")

    if role == "1":
        while True:
            print("\n--- Menu Pengelola ---")
            print("1. Input Riwayat Pembayaran")
            print("2. Edit Riwayat Pembayaran")
            print("3. Hapus Riwayat Pembayaran")
            print("4. Lihat Riwayat Pembayaran")
            print("5. Keluar")
            
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                input_pembayaran()
            elif pilihan == "2":
                edit_pembayaran()
            elif pilihan == "3":
                hapus_pembayaran()
            elif pilihan == "4":
                lihat_riwayat_pembayaran()
            elif pilihan == "5":
                print("Keluar dari menu pengelola.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    elif role == "2":
        while True:
            print("\n--- Menu Penyewa ---")
            print("1. Lihat Riwayat Pembayaran")
            print("2. Keluar")
            
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                lihat_riwayat_pembayaran()
            elif pilihan == "2":
                print("Keluar dari menu penyewa.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    
    elif role == "3":
        print("Keluar dari sistem. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
