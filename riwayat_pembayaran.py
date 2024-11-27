riwayat_pembayaran = []

def tampilkan_menu_pembayaran():
    print("\n--- Menu Riwayat Pembayaran ---")
    print("1. Input Riwayat Pembayaran")
    print("2. Edit Riwayat Pembayaran Terakhir")
    print("3. Hapus Riwayat Pembayaran Terakhir")
    print("4. Lihat Riwayat Pembayaran")
    print("5. Keluar")

def input_pembayaran():
    print("\n--- Input Riwayat Pembayaran ---")
    no_kamar = input("Nomor Kamar: ")
    nama_penyewa = input("Nama Penyewa: ")
    tanggal = input("Tanggal Pembayaran (YYYY-MM-DD): ")
    jumlah = float(input("Jumlah yang Dibayarkan: "))
    status = input("Status Pembayaran (Lunas/Belum Lunas): ").capitalize()
    
    riwayat_pembayaran.append({
        "no_kamar": no_kamar,
        "nama_penyewa": nama_penyewa,
        "tanggal": tanggal,
        "jumlah": jumlah,
        "status": status
    })
    print("Riwayat pembayaran berhasil ditambahkan.")

def edit_pembayaran():
    if not riwayat_pembayaran:
        print("\nBelum ada riwayat pembayaran untuk diedit.")
        return
    
    print("\n--- Edit Riwayat Pembayaran Terakhir ---")
    pembayaran = riwayat_pembayaran[-1]  # Ambil data terakhir
    pembayaran["nama_penyewa"] = input(f"Nama Penyewa [{pembayaran['nama_penyewa']}]: ") or pembayaran["nama_penyewa"]
    pembayaran["tanggal"] = input(f"Tanggal Pembayaran [{pembayaran['tanggal']}]: ") or pembayaran["tanggal"]
    pembayaran["jumlah"] = float(input(f"Jumlah yang Dibayarkan [{pembayaran['jumlah']}]: ") or pembayaran["jumlah"])
    pembayaran["status"] = input(f"Status Pembayaran [{pembayaran['status']}]: ").capitalize() or pembayaran["status"]
    print("Riwayat pembayaran berhasil diperbarui.")

def hapus_pembayaran():
    if not riwayat_pembayaran:
        print("\nBelum ada riwayat pembayaran untuk dihapus.")
        return
    
    print("\n--- Hapus Riwayat Pembayaran Terakhir ---")
    riwayat_pembayaran.pop()  # Hapus data terakhir
    print("Riwayat pembayaran terakhir berhasil dihapus.")

def lihat_riwayat_pembayaran():
    print("\n--- Riwayat Pembayaran ---")
    if not riwayat_pembayaran:
        print("Belum ada riwayat pembayaran.")
        return
    
    for pembayaran in riwayat_pembayaran:
        print(f"Nomor Kamar: {pembayaran['no_kamar']}")
        print(f"Nama Penyewa: {pembayaran['nama_penyewa']}")
        print(f"Tanggal Pembayaran: {pembayaran['tanggal']}")
        print(f"Jumlah: Rp{pembayaran['jumlah']}")
        print(f"Status: {pembayaran['status']}")
        print("-" * 30)

# Program utama
while True:
    tampilkan_menu_pembayaran()
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
        print("Keluar dari menu riwayat pembayaran.")
        break
    else:
        print("Pilihan tidak valid.")