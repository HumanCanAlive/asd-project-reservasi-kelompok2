
def hapus_reservasi(data_reservasi):
    """Menghapus reservasi berdasarkan kode setelah konfirmasi pengguna."""

    if not data_reservasi:
        print("Belum ada data reservasi.")
        return False

    print("\n=== HAPUS RESERVASI ===")
    kode = input("Masukkan kode reservasi yang ingin dihapus: ").strip()

    if not kode:
        print("Kode reservasi tidak boleh kosong.")
        return False

    # Cari reservasi berdasarkan kode
    reservasi_ditemukan = None

    for reservasi in data_reservasi:
        if reservasi.get("kode") == kode:
            reservasi_ditemukan = reservasi
            break

    # Jika kode tidak ditemukan
    if reservasi_ditemukan is None:
        print("Kode reservasi tidak ditemukan.")
        return False

    # Tampilkan detail sebelum menghapus
    print("\n=== DETAIL RESERVASI ===")
    print(f"Kode          : {reservasi_ditemukan.get('kode', '-')}")
    print(f"Nama pemesan  : {reservasi_ditemukan.get('nama_pemesan', '-')}")
    print(f"Jenis         : {reservasi_ditemukan.get('jenis_reservasi', '-')}")
    print(f"Tanggal       : {reservasi_ditemukan.get('tanggal_reservasi', '-')}")
    print(f"Nomor kamar   : {reservasi_ditemukan.get('nomor_kamar', '-')}")
    print(f"Lama menginap : {reservasi_ditemukan.get('lama_menginap', '-')}")
    print(f"Status        : {reservasi_ditemukan.get('status', '-')}")

    # Konfirmasi sebelum menghapus
    konfirmasi = input(
        "\nYakin ingin menghapus reservasi ini? (y/n): "
    ).strip().casefold()

    if konfirmasi == "y":
        data_reservasi.remove(reservasi_ditemukan)
        print("Reservasi berhasil dihapus.")
        return True

    elif konfirmasi == "n":
        print("Penghapusan dibatalkan.")
        return False

    else:
        print("Pilihan tidak valid. Penghapusan dibatalkan.")
        return False
