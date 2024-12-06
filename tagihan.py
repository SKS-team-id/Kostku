riwayat_pembayaran = {}

# Fungsi tambah tagihan baru
def tambah_tagihan():
    no_kamar = input("Nomor Kamar: ")
    if no_kamar not in riwayat_pembayaran:
        riwayat_pembayaran[no_kamar] = []

    nama_penyewa = input("Nama Penyewa: ")
    tanggal_tagihan = input("Tanggal Tagihan (YYYY-MM-DD): ")
    jumlah = float(input("Jumlah Tagihan: "))

    riwayat_pembayaran[no_kamar].append({
        "nama_penyewa": nama_penyewa,
        "tanggal": tanggal_tagihan,
        "jumlah": jumlah,
        "status": "Belum Dibayar"  # Status default untuk tagihan baru
    })
    print(f"Tagihan untuk kamar {no_kamar} berhasil ditambahkan.")

# Fungsi input pembayaran untuk tagihan tertentu
def input_pembayaran():
    no_kamar = input("Nomor Kamar: ")
    if no_kamar not in riwayat_pembayaran or not riwayat_pembayaran[no_kamar]:
        print("Tidak ada tagihan untuk kamar ini.")
        return
    
    print(f"\n--- Daftar Tagihan untuk Kamar {no_kamar} ---")
    for i, pembayaran in enumerate(riwayat_pembayaran[no_kamar], start=1):
        print(f"{i}. Tanggal: {pembayaran['tanggal']}, Jumlah: {pembayaran['jumlah']}, Status: {pembayaran['status']}")
    
    indeks = int(input("\nPilih nomor tagihan yang ingin dibayar: ")) - 1
    if 0 <= indeks < len(riwayat_pembayaran[no_kamar]):
        if riwayat_pembayaran[no_kamar][indeks]['status'] == "Lunas":
            print("Tagihan ini sudah lunas.")
        else:
            riwayat_pembayaran[no_kamar][indeks]['status'] = "Lunas"
            print("Pembayaran berhasil diproses. Tagihan telah diperbarui menjadi lunas.")
    else:
        print("Pilihan tidak valid.")

# Fungsi lihat riwayat pembayaran/tagihan berdasarkan nomor kamar
def lihat_riwayat_pembayaran():
    no_kamar = input("Nomor Kamar: ")
    if no_kamar not in riwayat_pembayaran or not riwayat_pembayaran[no_kamar]:
        print("Belum ada tagihan atau riwayat pembayaran untuk kamar ini.")
        return
    
    print(f"\n--- Riwayat Pembayaran untuk Kamar {no_kamar} ---")
    for pembayaran in riwayat_pembayaran[no_kamar]:
        print(f"Nama Penyewa: {pembayaran['nama_penyewa']}")
        print(f"Tanggal: {pembayaran['tanggal']}")
        print(f"Jumlah: Rp{pembayaran['jumlah']}")
        print(f"Status: {pembayaran['status']}")
        print("-" * 30)

# Program utama
while True:
    print("\n--- Sistem Manajemen Pembayaran Kost ---")
    print("1. Tambah Tagihan")
    print("2. Input Pembayaran")
    print("3. Lihat Riwayat Tagihan/Pembayaran")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_tagihan()
    elif pilihan == "2":
        input_pembayaran()
    elif pilihan == "3":
        lihat_riwayat_pembayaran()
    elif pilihan == "4":
        print("Keluar dari sistem. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
