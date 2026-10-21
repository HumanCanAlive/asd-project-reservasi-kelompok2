def filter_reservasi(daftar_reservasi):
    status_dicari = input(
        "Masukkan status (Aktif/Selesai/Dibatalkan): "
    ).strip().lower()

    hasil = [
        r for r in daftar_reservasi
        if r["status"].lower() == status_dicari
    ]

    if not hasil:
        print("Reservasi tidak ditemukan.")
        return

    for r in hasil:
        print(r)

    print("Total ditemukan:", len(hasil))

daftar_reservasi = [
    {
        "kode_reservasi": "RSV001",
        "nama_pemesan": "Budi",
        "status": "Aktif"
    },
    {
        "kode_reservasi": "RSV002",
        "nama_pemesan": "Siti",
        "status": "Selesai"
    }
]

# Jalankan fungsi setelah daftar selesai dibuat
filter_reservasi(daftar_reservasi)