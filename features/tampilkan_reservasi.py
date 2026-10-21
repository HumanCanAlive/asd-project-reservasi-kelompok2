"""F2: Tampilkan semua reservasi (Panji)."""

# Penanda visual status agar mudah dibedakan di tabel.
PENANDA_STATUS = {
    "Aktif": "[AKTIF]",
    "Selesai": "[SELESAI]",
    "Dibatalkan": "[DIBATALKAN]",
}

# Kolom tabel: (judul kolom, key pada dictionary reservasi).
KOLOM = [
    ("Kode", "kode"),
    ("Nama Pemesan", "nama_pemesan"),
    ("Jenis", "jenis_reservasi"),
    ("Tanggal", "tanggal_reservasi"),
    ("No. Kamar", "nomor_kamar"),
    ("Lama (hari)", "lama_menginap"),
    ("Status", "status"),
]


def tampilkan_semua_reservasi(data_reservasi):
    """Tampilkan seluruh reservasi dalam bentuk tabel."""
    if not data_reservasi:
        print("Belum ada data reservasi yang tersimpan.")
        return

    judul = ["No"] + [nama for nama, _ in KOLOM]
    baris = []
    for nomor, item in enumerate(data_reservasi, start=1):
        isi = [str(nomor)]
        for _, key in KOLOM:
            nilai = item.get(key, "-")
            if key == "status":
                nilai = PENANDA_STATUS.get(nilai, nilai)
            isi.append(str(nilai))
        baris.append(isi)

    # Lebar tiap kolom mengikuti teks terpanjang (judul atau isi).
    lebar = [max(len(judul[i]), *(len(b[i]) for b in baris)) for i in range(len(judul))]

    def format_baris(isi):
        return "│ " + " │ ".join(t.ljust(lebar[i]) for i, t in enumerate(isi)) + " │"

    garis = "─" * len(format_baris(judul))
    print(f"\nDAFTAR RESERVASI ({len(data_reservasi)} data)")
    print(garis)
    print(format_baris(judul))
    print(garis)
    for b in baris:
        print(format_baris(b))
    print(garis)