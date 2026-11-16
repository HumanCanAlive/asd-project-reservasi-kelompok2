class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_akhir(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
            return

        node_baru.prev = self.tail
        self.tail.next = node_baru
        self.tail = node_baru

    def is_empty(self):
        return self.head is None
    
DoublyLinkedList = LinkedList
    
from datetime import datetime

def catat_riwayat(
    data_riwayat,
    aksi,
    kode_reservasi,
    nama_pemesan,
    nilai_lama,
    nilai_baru
):
    """
    Mencatat aktivitas reservasi ke dalam Linked List.
    """

    # Menentukan nomor urut berikutnya
    no_urut = 1
    current = data_riwayat.head

    while current is not None:
        no_urut += 1
        current = current.next

    # Mengambil waktu pencatatan otomatis
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Membuat data riwayat
    data = {
        "no_urut": no_urut,
        "aksi": aksi,
        "kode_reservasi": kode_reservasi,
        "nama_pemesan": nama_pemesan,
        "nilai_lama": nilai_lama,
        "nilai_baru": nilai_baru,
        "waktu": waktu
    }

    # Menambahkan data ke Linked List
    data_riwayat.insert_akhir(data)

    return data

def tampilkan_riwayat(data_riwayat):
    """
    Menampilkan seluruh riwayat reservasi dari Linked List
    secara berurutan (dari yang paling awal dicatat).

    Mengembalikan jumlah data yang ditampilkan, supaya bisa
    dipakai fitur berikutnya (misalnya untuk validasi/statistik).
    """

    if data_riwayat.is_empty():
        print("Belum ada riwayat reservasi.")
        return 0

    garis = "=" * 110
    print(garis)
    print(
        f"{'No':<4}{'Waktu':<21}{'Aksi':<12}{'Kode':<10}"
        f"{'Nama Pemesan':<20}{'Nilai Lama':<20}{'Nilai Baru':<20}"
    )
    print(garis)

    jumlah = 0
    current = data_riwayat.head

    while current is not None:
        data = current.data

        print(
            f"{data['no_urut']:<4}"
            f"{data['waktu']:<21}"
            f"{data['aksi']:<12}"
            f"{data['kode_reservasi']:<10}"
            f"{data['nama_pemesan']:<20}"
            f"{str(data['nilai_lama']):<20}"
            f"{str(data['nilai_baru']):<20}"
        )

        jumlah += 1
        current = current.next

    print(garis)
    print(f"Total riwayat: {jumlah}")

    return jumlah

def cari_riwayat_reservasi(data_riwayat):
    if data_riwayat.is_empty():
        print("Belum ada riwayat reservasi.")
        return

    kode_dicari = input("Masukkan kode reservasi: ").strip()

    current = data_riwayat.head
    ditemukan = False

    print("\n=== HASIL PENCARIAN RIWAYAT ===")

    while current is not None:
        riwayat = current.data

        if riwayat["kode_reservasi"] == kode_dicari:
            print(f"No Urut       : {riwayat['no_urut']}")
            print(f"Aksi          : {riwayat['aksi']}")
            print(f"Kode Reservasi: {riwayat['kode_reservasi']}")
            print(f"Nama Pemesan  : {riwayat['nama_pemesan']}")
            print(f"Nilai Lama    : {riwayat['nilai_lama']}")
            print(f"Nilai Baru    : {riwayat['nilai_baru']}")
            print(f"Waktu         : {riwayat['waktu']}")
            print("-----------------------------")

            ditemukan = True

        current = current.next

    if not ditemukan:
        print("Riwayat dengan kode tersebut tidak ditemukan.")



def tampilkan_riwayat_terbaru(data_riwayat):
    """
    Menampilkan riwayat reservasi dari yang terbaru
    hingga yang terlama menggunakan Doubly Linked List.
    """

    if data_riwayat.is_empty():
        print("Belum ada riwayat reservasi.")
        return 0

    garis = "=" * 110

    print("\n=== RIWAYAT RESERVASI TERBARU ===")
    print(garis)

    print(
        f"{'No':<4}"
        f"{'Waktu':<21}"
        f"{'Aksi':<12}"
        f"{'Kode':<10}"
        f"{'Nama Pemesan':<20}"
        f"{'Nilai Lama':<20}"
        f"{'Nilai Baru':<20}"
    )

    print(garis)

    jumlah = 0

    # Memulai penelusuran dari node terakhir
    current = data_riwayat.tail

    while current is not None:
        data = current.data

        print(
            f"{data['no_urut']:<4}"
            f"{data['waktu']:<21}"
            f"{data['aksi']:<12}"
            f"{data['kode_reservasi']:<10}"
            f"{data['nama_pemesan']:<20}"
            f"{str(data['nilai_lama']):<20}"
            f"{str(data['nilai_baru']):<20}"
        )

        jumlah += 1

        # Bergerak menuju node sebelumnya
        current = current.prev

    print(garis)
    print(f"Total riwayat: {jumlah}")

    return jumlah