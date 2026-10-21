def hapus_reservasi(daftar_reservasi):
    kode = input("Masukkan kode reservasi: ").strip()

    for reservasi in daftar_reservasi:
        if reservasi["kode_reservasi"].lower() == kode.lower():
            print("\n=== DETAIL RESERVASI ===")
            print(f"Kode  : {reservasi['kode_reservasi']}")
            print(f"Nama  : {reservasi['nama_pemesan']}")
            print(f"Jenis : {reservasi['jenis']}")
            print(f"Status: {reservasi['status']}")

            konfirmasi = input(
                "Yakin ingin menghapus? (y/n): "
            ).strip().lower()

            if konfirmasi == "y":
                daftar_reservasi.remove(reservasi)
                print("Reservasi berhasil dihapus.")
            elif konfirmasi == "n":
                print("Penghapusan dibatalkan.")
            else:
                print("Input tidak valid. Penghapusan dibatalkan.")

            return

    print("Kode reservasi tidak ditemukan.")