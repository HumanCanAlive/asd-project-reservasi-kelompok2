
def update_status_reservasi(data_reservasi, data_riwayat):
    """Mengubah status reservasi berdasarkan kode reservasi."""

    
    if not data_reservasi:
        print("Belum ada data reservasi.")
        return False

    
    kode = input("Masukkan ID/kode reservasi: ").strip()


    reservasi_ditemukan = None

    for reservasi in data_reservasi:
        if reservasi.get("kode") == kode:
            reservasi_ditemukan = reservasi
            break


    if reservasi_ditemukan is None:
        print("Kode reservasi tidak ditemukan.")
        return False


    print("\nData reservasi ditemukan")
    print("Kode       :", reservasi_ditemukan["kode"])
    print("Nama       :", reservasi_ditemukan["nama_pemesan"])
    print("Status saat ini:", reservasi_ditemukan["status"])


    if reservasi_ditemukan["status"] != "Aktif":
        print("Status reservasi sudah final dan tidak dapat diubah.")
        return False


    print("\nPilih status baru:")
    print("1. Selesai")
    print("2. Dibatalkan")

    pilihan = input("Masukkan pilihan: ").strip()


    pilihan_status = {
        "1": "Selesai",
        "2": "Dibatalkan"
    }

    if pilihan not in pilihan_status:
        print("Pilihan tidak valid.")
        return False


    status_lama = reservasi_ditemukan["status"]
    status_baru = pilihan_status[pilihan]

    reservasi_ditemukan["status"] = status_baru

    print("\nStatus reservasi berhasil diubah.")
    print("Status lama :", status_lama)
    print("Status baru :", status_baru)

    return True