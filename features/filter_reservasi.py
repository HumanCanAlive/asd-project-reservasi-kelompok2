def filter_reservasi(data_reservasi):
    """Filter reservasi berdasarkan status, jenis, tanggal, atau nomor kamar."""

    if not data_reservasi:
        print("Belum ada data reservasi.")
        return

    print("\n=== FILTER RESERVASI ===")
    print("1. Berdasarkan status")
    print("2. Berdasarkan jenis reservasi")
    print("3. Berdasarkan tanggal reservasi")
    print("4. Berdasarkan nomor kamar")
    print("5. Kembali")

    pilihan = input("Pilih filter (1-5): ").strip()

    if pilihan == "5":
        return

    if pilihan == "1":
        print("\nPilihan status: Aktif, Selesai, Dibatalkan")
        kata_kunci = input("Masukkan status: ").strip().casefold()
        hasil = [
            r for r in data_reservasi
            if r.get("status", "").casefold() == kata_kunci
        ]

    elif pilihan == "2":
        print("\nPilihan jenis: Standard, Deluxe, Suite")
        kata_kunci = input("Masukkan jenis reservasi: ").strip().casefold()
        hasil = [
            r for r in data_reservasi
            if r.get("jenis_reservasi", "").casefold() == kata_kunci
        ]

    elif pilihan == "3":
        kata_kunci = input(
            "Masukkan tanggal (YYYY-MM-DD): "
        ).strip()
        hasil = [
            r for r in data_reservasi
            if r.get("tanggal_reservasi", "") == kata_kunci
        ]

    elif pilihan == "4":
        kata_kunci = input("Masukkan nomor kamar: ").strip()
        hasil = [
            r for r in data_reservasi
            if str(r.get("nomor_kamar", "")) == kata_kunci
        ]

    else:
        print("Pilihan tidak valid.")
        return

    if not hasil:
        print("Reservasi yang sesuai filter tidak ditemukan.")
        return

    print(f"\n=== HASIL FILTER ({len(hasil)} reservasi) ===")
    print("-" * 40)

    for nomor, r in enumerate(hasil, start=1):
        print(f"Reservasi ke-{nomor}")
        print(f"Kode          : {r.get('kode', '-')}")
        print(f"Nama pemesan  : {r.get('nama_pemesan', '-')}")
        print(f"Jenis         : {r.get('jenis_reservasi', '-')}")
        print(f"Tanggal       : {r.get('tanggal_reservasi', '-')}")
        print(f"Nomor kamar   : {r.get('nomor_kamar', '-')}")
        print(f"Lama menginap : {r.get('lama_menginap', '-')}")
        print(f"Status        : {r.get('status', '-')}")
        print("-" * 40)