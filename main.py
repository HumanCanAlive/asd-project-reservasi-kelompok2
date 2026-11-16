"""Entry point dan menu utama Sistem Manajemen Reservasi.

Tahap 1 : F1-F6 (list + dictionary)
Tahap 2 : R1-R4 (riwayat booking dengan Doubly Linked List)
"""

from features.tambah_reservasi import tambah_reservasi
from features.tampilkan_reservasi import tampilkan_semua_reservasi
from features.cari_reservasi import cari_reservasi
from features.update_reservasi import update_status_reservasi
from features.filter_reservasi import filter_reservasi
from features.hapus_reservasi import hapus_reservasi
from riwayat import LinkedList, catat_riwayat


# ---------------------------------------------------------------------------
# R1 - Pencatatan riwayat otomatis
# ---------------------------------------------------------------------------
# Fitur F1, F4, dan F6 dibungkus di sini. Riwayat hanya dicatat jika aksi
# benar-benar berhasil (data reservasi berubah), dan semua pencatatan lewat
# satu fungsi: catat_riwayat() dari riwayat.py.

def _catat(data_riwayat, tail_sebelum, aksi, kode, nama, nilai_lama, nilai_baru):
    """Catat riwayat, kecuali fitur sudah mencatatnya sendiri (cegah duplikat)."""
    if data_riwayat.tail is not tail_sebelum:
        return
    catat_riwayat(data_riwayat, aksi, kode, nama, nilai_lama, nilai_baru)
    print("Riwayat tercatat.")


def _ringkasan(reservasi):
    """Ringkasan 'jenis; tanggal' untuk kolom nilai riwayat."""
    return f"{reservasi.get('jenis_reservasi', '-')}; {reservasi.get('tanggal_reservasi', '-')}"


def jalankan_f1(data_reservasi, data_riwayat):
    """F1 Tambah Reservasi + R1 (aksi TAMBAH)."""
    jumlah_sebelum = len(data_reservasi)
    tail_sebelum = data_riwayat.tail

    tambah_reservasi(data_reservasi, data_riwayat)

    if len(data_reservasi) > jumlah_sebelum:  # berhasil ditambahkan
        baru = data_reservasi[-1]
        _catat(data_riwayat, tail_sebelum, "TAMBAH", baru["kode"],
               baru["nama_pemesan"], "-", _ringkasan(baru))


def jalankan_f2(data_reservasi, data_riwayat):
    """F2 Tampilkan Semua Reservasi."""
    tampilkan_semua_reservasi(data_reservasi)


def jalankan_f3(data_reservasi, data_riwayat):
    """F3 Cari Reservasi."""
    cari_reservasi(data_reservasi)


def jalankan_f4(data_reservasi, data_riwayat):
    """F4 Update Status + R1 (aksi UBAH_STATUS)."""
    status_sebelum = {r.get("kode"): r.get("status") for r in data_reservasi}
    tail_sebelum = data_riwayat.tail

    update_status_reservasi(data_reservasi, data_riwayat)

    for r in data_reservasi:
        status_lama = status_sebelum.get(r.get("kode"))
        if status_lama is not None and status_lama != r.get("status"):
            _catat(data_riwayat, tail_sebelum, "UBAH_STATUS", r["kode"],
                   r["nama_pemesan"], status_lama, r["status"])
            break  # kode unik, hanya satu reservasi yang berubah


def jalankan_f5(data_reservasi, data_riwayat):
    """F5 Filter Reservasi."""
    filter_reservasi(data_reservasi)


def jalankan_f6(data_reservasi, data_riwayat):
    """F6 Hapus Reservasi + R1 (aksi HAPUS, hanya setelah konfirmasi y)."""
    sebelum = list(data_reservasi)  # salinan data reservasi (bukan riwayat)
    tail_sebelum = data_riwayat.tail

    hapus_reservasi(data_reservasi)

    if len(data_reservasi) < len(sebelum):  # benar-benar terhapus
        kode_tersisa = {r.get("kode") for r in data_reservasi}
        for r in sebelum:
            if r.get("kode") not in kode_tersisa:
                _catat(data_riwayat, tail_sebelum, "HAPUS", r["kode"],
                       r["nama_pemesan"], _ringkasan(r), "-")
                break


# ---------------------------------------------------------------------------
# R2 - R4: tampilan riwayat (traversal langsung pada linked list)
# ---------------------------------------------------------------------------

def _telusuri_maju(data_riwayat):
    """Telusuri dari head ke ujung lewat next (paling lama -> paling baru)."""
    node = data_riwayat.head
    while node is not None:
        yield node.data
        node = node.next


def _telusuri_mundur(data_riwayat):
    """Telusuri dari tail ke awal lewat prev (paling baru -> paling lama)."""
    node = data_riwayat.tail
    while node is not None:
        yield node.data
        node = node.prev


FORMAT_BARIS = "{:<4}{:<21}{:<13}{:<9}{:<20}{:<22}{:<22}"
GARIS = "=" * 111


def _cetak_header():
    print(GARIS)
    print(FORMAT_BARIS.format("No", "Waktu", "Aksi", "Kode",
                              "Nama Pemesan", "Nilai Lama", "Nilai Baru"))
    print(GARIS)


def _cetak_baris(r):
    print(FORMAT_BARIS.format(r["no_urut"], r["waktu"], r["aksi"],
                              r["kode_reservasi"], r["nama_pemesan"],
                              str(r["nilai_lama"]), str(r["nilai_baru"])))


def jalankan_r2(data_reservasi, data_riwayat):
    """R2 Tampilkan seluruh riwayat (lama -> baru) + ringkasan per aksi."""
    if data_riwayat.is_empty():
        print("Belum ada riwayat.")
        return

    jumlah = {"TAMBAH": 0, "UBAH_STATUS": 0, "HAPUS": 0}
    total = 0

    print("\n=== SELURUH RIWAYAT ===")
    _cetak_header()
    for r in _telusuri_maju(data_riwayat):
        _cetak_baris(r)
        jumlah[r["aksi"]] = jumlah.get(r["aksi"], 0) + 1
        total += 1
    print(GARIS)
    print(f"Ringkasan: TAMBAH {jumlah['TAMBAH']} | "
          f"UBAH_STATUS {jumlah['UBAH_STATUS']} | "
          f"HAPUS {jumlah['HAPUS']} | Total {total}")


def jalankan_r3(data_reservasi, data_riwayat):
    """R3 Tampilkan riwayat satu reservasi (exact match kode)."""
    while True:
        kode = input("Masukkan kode reservasi: ").strip()
        if kode:
            break
        print("Error: Kode reservasi tidak boleh kosong.")

    jumlah = sum(1 for r in _telusuri_maju(data_riwayat)
                 if r["kode_reservasi"] == kode)
    if jumlah == 0:
        print(f"Tidak ada riwayat untuk reservasi dengan kode '{kode}'.")
        return

    print(f"\nMenampilkan {jumlah} riwayat untuk reservasi {kode}.")
    _cetak_header()
    for r in _telusuri_maju(data_riwayat):
        if r["kode_reservasi"] == kode:
            _cetak_baris(r)
    print(GARIS)


def jalankan_r4(data_reservasi, data_riwayat):
    """R4 Tampilkan N riwayat terbaru (baru -> lama) lewat tail dan prev."""
    if data_riwayat.is_empty():
        print("Belum ada riwayat.")
        return

    try:
        n = int(input("Jumlah riwayat yang ingin ditampilkan (N): ").strip())
    except ValueError:
        print("Error: N harus berupa angka bulat lebih dari 0.")
        return
    if n <= 0:
        print("Error: N harus berupa angka bulat lebih dari 0.")
        return

    tampil = 0
    print()
    _cetak_header()
    for r in _telusuri_mundur(data_riwayat):
        if tampil == n:
            break
        _cetak_baris(r)
        tampil += 1
    print(GARIS)
    print(f"Menampilkan {tampil} riwayat terbaru.")


# ---------------------------------------------------------------------------
# Menu utama
# ---------------------------------------------------------------------------

# kunci menu -> (label, fungsi, alias yang juga diterima)
MENU = {
    "1": ("F1. Tambah Reservasi", jalankan_f1, "F1"),
    "2": ("F2. Tampilkan Semua Reservasi", jalankan_f2, "F2"),
    "3": ("F3. Cari Reservasi", jalankan_f3, "F3"),
    "4": ("F4. Update Status", jalankan_f4, "F4"),
    "5": ("F5. Filter Reservasi", jalankan_f5, "F5"),
    "6": ("F6. Hapus Reservasi", jalankan_f6, "F6"),
    "7": ("R2. Tampilkan Seluruh Riwayat", jalankan_r2, "R2"),
    "8": ("R3. Riwayat per Reservasi", jalankan_r3, "R3"),
    "9": ("R4. Riwayat Terbaru (N terakhir)", jalankan_r4, "R4"),
}

# Alias "F1".."F6" dan "R2".."R4" menunjuk ke nomor menu yang sama.
ALIAS = {alias: kunci for kunci, (_, _, alias) in MENU.items()}


def tampilkan_menu():
    """Cetak daftar menu utama."""
    print("\n" + "=" * 44)
    print("      SISTEM MANAJEMEN RESERVASI")
    print("=" * 44)
    for kunci, (label, _, _) in MENU.items():
        print(f"{kunci}. {label}")
    print("0. Keluar")
    print("-" * 44)
    print("R1: riwayat dicatat otomatis saat F1, F4, F6")
    print("=" * 44)


def main():
    """Jalankan menu utama sampai pengguna memilih keluar."""
    data_reservasi = []          # Tahap 1: list of dictionary
    data_riwayat = LinkedList()  # Tahap 2: Doubly Linked List (head + tail)

    while True:
        tampilkan_menu()
        try:
            pilihan = input("Pilih menu (0-9): ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nProgram dihentikan.")
            break

        pilihan = ALIAS.get(pilihan, pilihan)  # terima "F1", "R2", dst.

        if pilihan == "0":
            print("Terima kasih. Program selesai.")
            break

        if pilihan not in MENU:
            print("Pilihan tidak valid. Masukkan angka 0-9.")
            continue

        _, fitur, _ = MENU[pilihan]
        try:
            fitur(data_reservasi, data_riwayat)
        except (EOFError, KeyboardInterrupt):
            print("\nProses dibatalkan, kembali ke menu.")


if __name__ == "__main__":
    main()