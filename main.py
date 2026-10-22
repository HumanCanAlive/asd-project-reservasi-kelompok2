"""Entry point dan menu utama Sistem Manajemen Reservasi."""

from features.tambah_reservasi import tambah_reservasi
from features.tampilkan_reservasi import tampilkan_semua_reservasi
from features.cari_reservasi import cari_reservasi
from features.update_reservasi import update_status_reservasi
from features.filter_reservasi import filter_reservasi
from features.hapus_reservasi import hapus_reservasi


def tampilkan_menu():
    """Cetak daftar menu utama."""
    print("\n" + "=" * 40)
    print("   SISTEM MANAJEMEN RESERVASI")
    print("=" * 40)
    print("F1. Tambah Reservasi")
    print("F2. Tampilkan Semua Reservasi")
    print("F3. Cari Reservasi")
    print("F4. Update Status")
    print("F5. Filter Berdasarkan Status")
    print("F6. Hapus Reservasi")
    print("0.  Keluar")
    print("=" * 40)


def main():
    """Jalankan menu utama sampai pengguna memilih keluar."""
    data_reservasi = []

    # Pilihan menu -> fungsi dari folder features.
    menu = {
        "1": tambah_reservasi,
        "2": tampilkan_semua_reservasi,
        "3": cari_reservasi,
        "4": update_status_reservasi,
        "5": filter_reservasi,
        "6": hapus_reservasi,
    }

    while True:
        tampilkan_menu()
        try:
            pilihan = input("Pilih menu (0-6): ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nProgram dihentikan.")
            break

        # Izinkan penulisan "F1".."F6" selain angka "1".."6".
        if pilihan.startswith("F"):
            pilihan = pilihan[1:]

        if pilihan == "0":
            print("Terima kasih. Program selesai.")
            break

        fitur = menu.get(pilihan)
        if fitur is None:
            print("Pilihan tidak valid. Masukkan angka 0-6.")
            continue

        try:
            fitur(data_reservasi)
        except (EOFError, KeyboardInterrupt):
            print("\nProses dibatalkan, kembali ke menu.")


if __name__ == "__main__":
    main()