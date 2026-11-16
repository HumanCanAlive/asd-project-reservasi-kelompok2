
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_akhir(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node_baru

    def is_empty(self):
        return self.head is None
    
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

