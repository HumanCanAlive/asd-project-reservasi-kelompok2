"""Cari reservasi berdasarkan kode atau nama pemesan (Panji)."""

PENANDA_STATUS = {
    "Aktif": "[AKTIF]",
    "Selesai": "[SELESAI]",
    "Dibatalkan": "[DIBATALKAN]",
}

KOLOM = [
    ("Kode", "kode"),
    ("Nama Pemesan", "nama_pemesan"),
    ("Jenis", "jenis_reservasi"),
    ("Tanggal", "tanggal_reservasi"),
    ("No. Kamar", "nomor_kamar"),
    ("Lama (hari)", "lama_menginap"),
    ("Status", "status"),
]


def _nilai(item, key):
    nilai = item.get(key, "-")
    if key == "status":
        nilai = PENANDA_STATUS.get(nilai, nilai)
    return str(nilai)


def _cetak_tabel(daftar):
    judul = ["No"] + [nama for nama, _ in KOLOM]
    baris = [
        [str(no)] + [_nilai(item, key) for _, key in KOLOM]
        for no, item in enumerate(daftar, start=1)
    ]
    lebar = [max(len(judul[i]), *(len(b[i]) for b in baris)) for i in range(len(judul))]

    def format_baris(isi):
        return "│ " + " │ ".join(t.ljust(lebar[i]) for i, t in enumerate(isi)) + " │"

    garis = "─" * len(format_baris(judul))
    print(garis)
    print(format_baris(judul))
    print(garis)
    for b in baris:
        print(format_baris(b))
    print(garis)


def _cetak_detail(item):
    print("\nDetail Reservasi")
    print("─" * 40)
    for nama, key in KOLOM:
        print(f"{nama:<14}: {_nilai(item, key)}")
    print("─" * 40)


def cari_reservasi(data_reservasi):
    """Cari reservasi berdasarkan kode (exact match) atau nama (partial match)."""
    # Pilih mode pencarian.
    while True:
        print("\nCari reservasi berdasarkan:")
        print("1. Kode reservasi (harus persis)")
        print("2. Nama pemesan (boleh sebagian)")
        mode = input("Pilih mode (1/2): ").strip()
        if mode in ("1", "2"):
            break
        print("Error: Pilihan tidak valid. Masukkan 1 atau 2.")

    # Kata kunci tidak boleh kosong.
    label = "kode" if mode == "1" else "nama pemesan"
    while True:
        kata_kunci = input(f"Masukkan {label}: ").strip()
        if kata_kunci:
            break
        print("Error: Kata kunci tidak boleh kosong.")

    if mode == "1":
        hasil = [item for item in data_reservasi if item.get("kode") == kata_kunci]
        if not hasil:
            print(f"Reservasi dengan kode '{kata_kunci}' tidak ditemukan.")
            return
        _cetak_detail(hasil[0])
    else:
        kunci = kata_kunci.casefold()
        hasil = [
            item for item in data_reservasi
            if kunci in item.get("nama_pemesan", "").casefold()
        ]
        if not hasil:
            print(f"Reservasi dengan nama pemesan '{kata_kunci}' tidak ditemukan.")
            return
        print(f"\nDitemukan {len(hasil)} reservasi dengan nama mengandung '{kata_kunci}':")
        _cetak_tabel(hasil)