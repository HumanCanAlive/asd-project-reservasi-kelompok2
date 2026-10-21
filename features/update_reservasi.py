def update_status_reservasi(data_reservasi):
    kode = input("Masukkan ID/kode reservasi: ").strip()

    for reservasi in data_reservasi:
        if reservasi["kode"] == kode:

            if reservasi["status"] != "Aktif":
                print("Status reservasi sudah final dan tidak dapat diubah.")
                return

            print("\nPilih status baru:")
            print("1. Selesai")
            print("2. Dibatalkan")

            pilihan = input("Masukkan pilihan: ").strip()

            if pilihan == "1":
                reservasi["status"] = "Selesai"
                print("Status reservasi berhasil diubah menjadi Selesai.")

            elif pilihan == "2":
                reservasi["status"] = "Dibatalkan"
                print("Status reservasi berhasil diubah menjadi Dibatalkan.")

            else:
                print("Pilihan tidak valid.")

            return

    print("Kode reservasi tidak ditemukan.")
    from features.update_reservasi import update_status_reservasi

data_reservasi = [
    {
        "kode": "R001",
        "nama_pemesan": "Budi",
        "jenis_reservasi": "Standard",
        "tanggal_reservasi": "2026-10-20",
        "nomor_kamar": 101,
        "lama_menginap": 2,
        "status": "Aktif"
    }
]

update_status_reservasi(data_reservasi)

print("\nData setelah diubah:")
print(data_reservasi)