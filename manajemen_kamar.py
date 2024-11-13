# Data Awal
kamar_list = []
fasilitas_list = []
harga_list = []

# Fungsi CRUD untuk Pengelola
def input_data_kamar():
    nomor_kamar = input("Masukkan nomor kamar: ")
    status = "Belum Disewa"
    kamar = {"nomor_kamar": nomor_kamar, "status": status}
    kamar_list.append(kamar)
    print("Data kamar berhasil ditambahkan.")

def edit_status_kamar():
    nomor_kamar = input("Masukkan nomor kamar yang ingin diubah statusnya: ")
    for kamar in kamar_list:
        if kamar["nomor_kamar"] == nomor_kamar:
            kamar["status"] = "Disewa" if kamar["status"] == "Belum Disewa" else "Belum Disewa"
            print(f"Status kamar {nomor_kamar} berhasil diubah menjadi {kamar['status']}.")
            return
    print("Kamar tidak ditemukan.")

def input_data_fasilitas():
    nomor_kamar = input("Masukkan nomor kamar yang ingin ditambahkan fasilitas: ")
    fasilitas = input("Masukkan nama fasilitas: ")
    fasilitas_list.append({"nomor_kamar": nomor_kamar, "fasilitas": fasilitas})
    print("Fasilitas berhasil ditambahkan.")

def edit_data_fasilitas():
    nomor_kamar = input("Masukkan nomor kamar untuk mengedit fasilitas: ")
    fasilitas_lama = input("Masukkan nama fasilitas yang ingin diubah: ")
    fasilitas_baru = input("Masukkan nama fasilitas baru: ")
    for fasilitas_data in fasilitas_list:
        if fasilitas_data["nomor_kamar"] == nomor_kamar and fasilitas_data["fasilitas"] == fasilitas_lama:
            fasilitas_data["fasilitas"] = fasilitas_baru
            print("Fasilitas berhasil diubah.")
            return
    print("Fasilitas tidak ditemukan.")

def hapus_data_fasilitas():
    nomor_kamar = input("Masukkan nomor kamar untuk menghapus fasilitas: ")
    fasilitas = input("Masukkan nama fasilitas yang ingin dihapus: ")
    for fasilitas_data in fasilitas_list:
        if fasilitas_data["nomor_kamar"] == nomor_kamar and fasilitas_data["fasilitas"] == fasilitas:
            fasilitas_list.remove(fasilitas_data)
            print("Fasilitas berhasil dihapus.")
            return
    print("Fasilitas tidak ditemukan.")

def input_harga_kost():
    nomor_kamar = input("Masukkan nomor kamar: ")
    harga = input("Masukkan harga kost: ")
    harga_list.append({"nomor_kamar": nomor_kamar, "harga": harga})
    print("Harga kost berhasil ditambahkan.")

def edit_harga_kost():
    nomor_kamar = input("Masukkan nomor kamar yang ingin diubah harganya: ")
    for harga_data in harga_list:
        if harga_data["nomor_kamar"] == nomor_kamar:
            harga_data["harga"] = input("Masukkan harga baru: ")
            print("Harga kost berhasil diubah.")
            return
    print("Harga kost tidak ditemukan.")

# Fungsi untuk Penyewa
def lihat_kamar_kosong():
    print("Daftar Kamar Kosong:")
    for kamar in kamar_list:
        if kamar["status"] == "Belum Disewa":
            print(f"Nomor Kamar: {kamar['nomor_kamar']}")

def pilih_kamar():
    nomor_kamar = input("Masukkan nomor kamar yang ingin disewa: ")
    for kamar in kamar_list:
        if kamar["nomor_kamar"] == nomor_kamar and kamar["status"] == "Belum Disewa":
            kamar["status"] = "Disewa"
            print(f"Kamar {nomor_kamar} berhasil dipilih.")
            return
    print("Kamar tidak ditemukan atau sudah disewa.")

# Menu Program
def main():
    while True:
        print("\nManajemen Kost")
        print("1. Input Data Kamar")
        print("2. Edit Status Kamar")
        print("3. Input Data Fasilitas")
        print("4. Edit Data Fasilitas")
        print("5. Hapus Data Fasilitas")
        print("6. Input Daftar Harga Kost")
        print("7. Edit Harga Kost")
        print("8. Lihat Kamar Kosong")
        print("9. Pilih Kamar Kosong")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            input_data_kamar()
        elif pilihan == "2":
            edit_status_kamar()
        elif pilihan == "3":
            input_data_fasilitas()
        elif pilihan == "4":
            edit_data_fasilitas()
        elif pilihan == "5":
            hapus_data_fasilitas()
        elif pilihan == "6":
            input_harga_kost()
        elif pilihan == "7":
            edit_harga_kost()
        elif pilihan == "8":
            lihat_kamar_kosong()
        elif pilihan == "9":
            pilih_kamar()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi manajemen kost.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()