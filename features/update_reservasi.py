def update_status_reservasi(data_reservasi):
    """Mengubah status reservasi berdasarkan kode reservasi."""

    
    if not data_reservasi:
        print("Belum ada data reservasi.")
        return False

    # 2. Minta kode reservasi dari user
    kode = input("Masukkan ID/kode reservasi: ").strip()

    # 3. Cari reservasi berdasarkan kode
    reservasi_ditemukan = None

    for reservasi in data_reservasi:
        if reservasi.get("kode") == kode:
            reservasi_ditemukan = reservasi
            break

    # 4. Jika kode tidak ditemukan
    if reservasi_ditemukan is None:
        print("Kode reservasi tidak ditemukan.")
        return False

    # 5. Tampilkan informasi reservasi
    print("\nData reservasi ditemukan")
    print("Kode       :", reservasi_ditemukan["kode"])
    print("Nama       :", reservasi_ditemukan["nama_pemesan"])
    print("Status saat ini:", reservasi_ditemukan["status"])

    # 6. Status hanya bisa diubah jika masih Aktif
    if reservasi_ditemukan["status"] != "Aktif":
        print("Status reservasi sudah final dan tidak dapat diubah.")
        return False

    # 7. Tampilkan pilihan status baru
    print("\nPilih status baru:")
    print("1. Selesai")
    print("2. Dibatalkan")

    pilihan = input("Masukkan pilihan: ").strip()

    # 8. Validasi pilihan user
    pilihan_status = {
        "1": "Selesai",
        "2": "Dibatalkan"
    }

    if pilihan not in pilihan_status:
        print("Pilihan tidak valid.")
        return False

    # 9. Update data reservasi yang ditemukan
    status_lama = reservasi_ditemukan["status"]
    status_baru = pilihan_status[pilihan]

    reservasi_ditemukan["status"] = status_baru

    print("\nStatus reservasi berhasil diubah.")
    print("Status lama :", status_lama)
    print("Status baru :", status_baru)

    return True