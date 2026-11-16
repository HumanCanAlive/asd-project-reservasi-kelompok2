# asd-project-reservasi-kelompok2
Project UTS Algoritma dan Struktur Data | 3C Kelompok 2 

============================================================

Nama Anggota Kelompok 
Kelompok 2 Algoritma
1. Panji Eka Saputra (25083000020) | @pnjiekaa
2. Yoses Tri Ananda Jodi (25083000024) | @sheesh-yo
3. Gemilang Jelang Lailattulqadr (25083000025) | @HumanCanAlive
4. Naurin Gita Nur Cahyani (25083000043) | @nanaagitaa
5. Rizka Mutiara Sandy (25083000102) | @rzkmdy

# SISTEM RESERVASI

## 1. Informasi Proyek

- Nama Proyek: Sistem Reservasi Hotel
- Mata Kuliah: Algoritma dan Struktur Data
- Program Studi: Sistem Informasi
- Fakultas: Teknologi Informasi
- Universitas: Universitas Merdeka Malang
- Bahasa Pemrograman: Python
- Antarmuka: Command Line Interface (CLI)
- Tahap Pengembangan: Tahap 1 — Array & Struct, Tahap 2 — Riwayat Booking dengan Linked List

## 2. Tugas Masing Masing

**Tahap 1 — Array & Struct (F1–F6)**

1. Gemilang : Ketua kelompok dan integrasi program
2. Yoses : Fitur tambah reservasi
3. Panji : Fitur tampilkan dan cari reservasi
4. Gita : Fitur update status reservasi
5. Rizka : Fitur filter, hapus reservasi, dan dokumentasi

**Tahap 2 — Riwayat Booking dengan Linked List (R1–R4)**

1. Gemilang : Core & integrasi (struktur dasar `riwayat.py` dan `main.py`, menu R2–R4)
2. Yoses : R1 — sistem pencatatan riwayat dan integrasi F1
3. Panji : R2 — menampilkan seluruh riwayat
4. Gita : R3 + R1 — riwayat per reservasi dan integrasi F4
5. Rizka : R4 + R1 — riwayat terbaru dan integrasi F6

## 3. Deskripsi Proyek

Sistem Reservasi merupakan aplikasi berbasis Command Line Interface (CLI) yang dibuat menggunakan bahasa pemrograman Python untuk membantu pengelolaan data reservasi Hotel.

Aplikasi ini dirancang agar pengguna dapat mengelola data reservasi melalui terminal, mulai dari menambahkan data baru, menampilkan seluruh data, mencari reservasi tertentu, memperbarui status, memfilter berdasarkan status, hingga menghapus data reservasi.

Pada Tahap 2, sistem ditambah modul riwayat booking. Setiap pembuatan, perubahan status, dan penghapusan reservasi dicatat sebagai satu catatan baru yang disusun berurutan menggunakan Linked List, sehingga admin dapat melihat kapan sebuah reservasi dibuat, diubah, atau dihapus.

Proyek ini dikembangkan sebagai penerapan konsep Algoritma dan Struktur Data, khususnya penggunaan struktur data list dan dictionary (Tahap 1) serta Singly dan Doubly Linked List (Tahap 2) dalam Python.

## 4. Tujuan Proyek

Tujuan pengembangan Sistem Reservasi adalah:

1. Menerapkan konsep algoritma dan struktur data dalam program sederhana.
2. Mempermudah pengelolaan data reservasi tiket atau ruangan.
3. Menerapkan validasi input untuk menjaga konsistensi data.
4. Melatih kerja sama tim dalam pengembangan perangkat lunak.
5. Menggunakan Git dan GitHub untuk mengelola kode sumber serta kontribusi setiap anggota.

## 5. Fitur Sistem

Sistem Reservasi memiliki enam fitur utama pada Tahap 1 (F1–F6) dan empat fitur riwayat pada Tahap 2 (R1–R4).

### Fitur Tahap 1

### F1. Tambah Reservasi

Digunakan untuk menambahkan data reservasi baru dengan atribut kode reservasi, nama pemesan, jenis reservasi, detail reservasi, dan tanggal. Setiap reservasi baru memiliki status awal `Aktif`.

### F2. Tampilkan Semua Reservasi

Digunakan untuk menampilkan seluruh data reservasi dalam bentuk tabel yang memuat informasi setiap reservasi.

### F3. Cari Reservasi

Digunakan untuk mencari data reservasi berdasarkan kode reservasi atau nama pemesan.

### F4. Update Status Reservasi

Digunakan untuk memperbarui status reservasi sesuai aturan yang diterapkan oleh sistem, seperti `Selesai` atau `Dibatalkan`.

### F5. Filter Reservasi Berdasarkan Status

Digunakan untuk menampilkan data reservasi berdasarkan status tertentu, yaitu `Aktif`, `Selesai`, atau `Dibatalkan`.

### F6. Hapus Reservasi

Digunakan untuk menghapus data reservasi berdasarkan kode reservasi setelah pengguna memberikan konfirmasi penghapusan.

### Fitur Tahap 2 (Riwayat Booking)

### R1. Catat Riwayat Otomatis

Setiap aksi F1 (tambah), F4 (update status), dan F6 (hapus) dicatat otomatis sebagai node baru di akhir linked list melalui fungsi `catat_riwayat()`. Riwayat hanya dicatat jika aksi berhasil; penghapusan dicatat setelah pengguna mengonfirmasi `y`.

### R2. Tampilkan Seluruh Riwayat

Menampilkan semua catatan dari yang paling lama ke yang paling baru dalam bentuk tabel, disertai ringkasan jumlah catatan per aksi (`TAMBAH`, `UBAH_STATUS`, `HAPUS`).

### R3. Tampilkan Riwayat per Reservasi

Menampilkan seluruh jejak satu reservasi berdasarkan kode reservasi (exact match). Reservasi yang sudah dihapus tetap dapat dicari riwayatnya.

### R4. Riwayat Terbaru Lebih Dulu

Menampilkan N catatan terakhir dari yang paling baru ke yang lebih lama dengan Doubly Linked List (pointer `tail` dan `prev`). N harus berupa angka bulat lebih dari 0.

## 6. Struktur Data

Pada Tahap 1, sistem menggunakan struktur data berikut:

- **List:** Menyimpan kumpulan data reservasi.
- **Dictionary:** Menyimpan atribut dari setiap reservasi.

Setiap data reservasi memiliki enam atribut utama:

| Atribut          | Keterangan                                |
| `kode_reservasi` | Kode unik untuk setiap reservasi          |
| `nama_pemesan`   | Nama orang yang melakukan reservasi       |
| `jenis`          | Jenis reservasi, yaitu tiket atau ruangan |
| `detail`         | Informasi detail reservasi                |
| `tanggal`        | Tanggal pelaksanaan reservasi             |
| `status`         | Status reservasi                          |

Contoh representasi satu data reservasi dalam Python:

```python
reservasi = {
    "kode_reservasi": "RSV001",
    "nama_pemesan": "Budi",
    "jenis": "Ruangan",
    "detail": "Ruang Meeting A",
    "tanggal": "2026-10-25",
    "status": "Aktif"
}
```

Kumpulan reservasi disimpan dalam sebuah list:

```python
daftar_reservasi = [reservasi]
```

Pada Tahap 2, riwayat disimpan dalam **Doubly Linked List** buatan sendiri di `riwayat.py` (class `Node` dan `LinkedList` dengan pointer `head`, `tail`, `prev`, dan `next`). Satu catatan riwayat adalah satu dictionary yang disimpan sebagai data dalam satu node, dengan tujuh atribut wajib:

| Atribut          | Keterangan                                           |
| `no_urut`        | Nomor urut catatan, naik otomatis mulai dari 1       |
| `aksi`           | `TAMBAH`, `UBAH_STATUS`, atau `HAPUS`                |
| `kode_reservasi` | Kode reservasi yang terkait dengan aksi              |
| `nama_pemesan`   | Nama pemesan saat aksi terjadi                       |
| `nilai_lama`     | Nilai sebelum perubahan, `-` jika tidak ada          |
| `nilai_baru`     | Nilai sesudah perubahan, `-` jika tidak ada          |
| `waktu`          | Waktu aksi, format `YYYY-MM-DD HH:MM:SS` (otomatis)  |

## 7. Teknologi yang Digunakan

| Teknologi          | Kegunaan                                        |
| Python             | Bahasa pemrograman utama                        |
| Visual Studio Code | Editor untuk menulis dan mengelola kode         |
| Git                | Version control untuk mencatat perubahan kode   |
| GitHub             | Platform penyimpanan repository dan kolaborasi  |
| Terminal/CLI       | Antarmuka untuk menjalankan program             |

Proyek ini dirancang menggunakan library bawaan Python sehingga tidak memerlukan instalasi library eksternal.

## 8. Cara Menjalankan Program

### Persyaratan

- Python versi 3.8 atau lebih baru.
- Git, jika ingin mengunduh repository menggunakan Git.
- Terminal atau Visual Studio Code.

### Langkah 1. Clone Repository

Jalankan perintah berikut pada terminal:

```bash
git clone URL_REPOSITORY_KALIAN
```

Ganti `URL_REPOSITORY_KALIAN` dengan alamat repository GitHub kelompok.

### Langkah 2. Masuk ke Folder Proyek

```bash
cd NAMA_FOLDER_PROYEK
```

Ganti `NAMA_FOLDER_PROYEK` sesuai nama folder proyek.

### Langkah 3. Jalankan Program

```bash
python main.py
```

Jika sistem menggunakan perintah `python3`, jalankan:

```bash
python3 main.py
```

### Langkah 4. Gunakan Menu

Setelah program berjalan, pilih menu sesuai fitur yang ingin digunakan dan masukkan data berdasarkan instruksi yang ditampilkan pada terminal.

| Menu | Fitur                              |
| 1–6  | F1–F6 (Tahap 1)                    |
| 7    | R2 — Tampilkan seluruh riwayat     |
| 8    | R3 — Riwayat per reservasi         |
| 9    | R4 — Riwayat terbaru (N terakhir)  |
| 0    | Keluar                             |

R1 tidak memiliki menu karena riwayat dicatat otomatis saat F1, F4, dan F6 berhasil dijalankan.

## 9. Pembagian Tugas

### Tahap 1 — Array & Struct (F1–F6)

#### Gemilang — Ketua dan Integrasi Program

- Membuat menu utama pada `main.py`.
- Mengintegrasikan fungsi yang dikembangkan anggota kelompok.
- Memastikan seluruh fitur dapat diakses melalui menu.
- Menguji jalannya program secara keseluruhan.

#### Yoses — Fitur F1: Tambah Reservasi

- Mengembangkan fungsi untuk menambahkan reservasi.
- Memvalidasi kelengkapan input dan keunikan kode reservasi.
- Memvalidasi jenis dan format tanggal sesuai ketentuan proyek.
- Menetapkan status awal reservasi menjadi `Aktif`.

#### Panji — Fitur F2 dan F3: Tampilkan dan Cari Reservasi

- Mengembangkan fungsi untuk menampilkan seluruh data reservasi.
- Menyusun tampilan data dalam bentuk tabel.
- Mengembangkan pencarian berdasarkan kode reservasi atau nama pemesan.
- Menguji hasil pencarian dan tampilan data.

#### Gita — Fitur F4: Update Status Reservasi

- Mengembangkan fungsi untuk memperbarui status reservasi.
- Memvalidasi kode reservasi sebelum perubahan dilakukan.
- Menerapkan aturan perubahan status sesuai ketentuan proyek.
- Menguji berbagai kondisi perubahan status.

#### Rizka — Fitur F5 dan F6: Filter dan Hapus Reservasi

- Mengembangkan fungsi filter berdasarkan status.
- Mengembangkan fungsi penghapusan reservasi berdasarkan kode.
- Menambahkan konfirmasi sebelum penghapusan.
- Menyusun dan memperbarui dokumentasi `README.md`.
- Membantu pengujian fitur filter dan hapus.

### Tahap 2 — Riwayat Booking dengan Linked List (R1–R4)

#### Gemilang — Core & Integrasi

Tugas: struktur dasar `riwayat.py` dan `main.py`.

- Membuat class `Node`.
- Membuat class `LinkedList`.
- Membuat atribut `head` dan method `insert_akhir()`.
- Mengatur fondasi yang nantinya bisa dikembangkan menjadi Doubly Linked List.
- Menambahkan menu R2, R3, dan R4 di `main.py`.
- Mengintegrasikan pemanggilan fitur riwayat ke menu utama.

#### Yoses — R1: Sistem Pencatatan Riwayat dan Integrasi F1

- Membuat fungsi `catat_riwayat()`.
- Mengatur tujuh atribut wajib riwayat.
- Membuat nomor urut otomatis.
- Mengatur waktu pencatatan menggunakan `datetime`.
- Mengintegrasikan pencatatan ke `tambah_reservasi.py`.
- Memastikan riwayat tercatat hanya ketika F1 berhasil.

#### Panji — R2: Menampilkan Seluruh Riwayat

- Membuat fungsi R2 di `riwayat.py`.
- Melakukan traversal dari `head` sampai akhir.
- Membuat tabel seluruh riwayat.
- Membuat ringkasan jumlah aksi `TAMBAH`, `UBAH_STATUS`, dan `HAPUS`.
- Menangani kondisi riwayat kosong.

#### Gita — R3 + R1: Riwayat per Reservasi dan Integrasi F4

- Membuat fungsi R3 di `riwayat.py`.
- Membuat pencarian berdasarkan kode reservasi.
- Menerapkan exact match dan validasi input.
- Menampilkan riwayat sesuai kode yang dicari.
- Mengintegrasikan pencatatan `UBAH_STATUS` ke `update_reservasi.py`.
- Memastikan status lama dan baru tercatat benar.

#### Rizka — R4 + R1: Riwayat Terbaru dan Integrasi F6

- Mengembangkan Doubly Linked List dengan `tail`, `prev`, dan `next`.
- Membuat fungsi R4.
- Membuat validasi input N.
- Menampilkan riwayat terbaru dari belakang.
- Mengintegrasikan pencatatan `HAPUS` ke `hapus_reservasi.py`.
- Memastikan penghapusan baru dicatat setelah konfirmasi `y`.

Seluruh anggota bertanggung jawab menguji fitur masing-masing, memberikan kontribusi melalui commit GitHub, dan memahami kode yang dikembangkan.

## 10. Pengujian Program

Pengujian dilakukan untuk memastikan setiap fitur berjalan sesuai kebutuhan.

Skenario pengujian yang direncanakan meliputi:

1. Menambahkan reservasi dengan data valid.
2. Memasukkan kode reservasi yang sudah digunakan.
3. Menampilkan seluruh data reservasi.
4. Mencari reservasi menggunakan kode dan nama pemesan.
5. Memperbarui status reservasi dengan kode yang valid dan tidak valid.
6. Memfilter reservasi berdasarkan status.
7. Menghapus reservasi dengan konfirmasi dan membatalkan penghapusan.
8. Memastikan program menangani input yang tidak sesuai.
9. Memastikan riwayat tercatat setelah F1, F4, dan F6 berhasil, dan tidak tercatat saat aksi gagal atau dibatalkan.
10. Menampilkan seluruh riwayat (R2), riwayat per reservasi (R3), dan N riwayat terbaru (R4), termasuk kondisi riwayat kosong dan input N tidak valid.

Hasil pengujian dapat dilengkapi setelah implementasi dan pengujian seluruh fitur selesai dilakukan.

## 11. Kolaborasi Git dan GitHub

Pengembangan proyek dilakukan secara berkelompok dengan menggunakan Git dan GitHub untuk mengelola kode sumber.

Setiap anggota diharapkan melakukan commit terhadap perubahan yang dikerjakan masing-masing. Pesan commit ditulis secara jelas sesuai perubahan yang dilakukan.

Contoh perintah Git:

```bash
git add README.md
git commit -m "Menambahkan dokumentasi README sistem reservasi"
git push
```

Sebelum melakukan integrasi, perubahan kode perlu diperiksa agar tidak menimbulkan konflik dan seluruh fitur dapat bekerja dengan baik.

## 12. Batasan Sistem

Pada Tahap 1 dan Tahap 2, sistem memiliki batasan berikut:

- Program dijalankan melalui terminal atau CLI.
- Data reservasi disimpan dalam memori menggunakan list dan dictionary.
- Data riwayat disimpan dalam memori menggunakan Doubly Linked List.
- Data tidak tersimpan secara permanen setelah program ditutup.
- Riwayat hanya bertambah; catatan lama tidak diubah atau dihapus.
- Pengelolaan data dilakukan melalui menu yang tersedia.
- Fitur yang dikembangkan berfokus pada kebutuhan reservasi tiket atau ruangan sesuai ruang lingkup proyek.

## 13. Penutup

Sistem Reservasi diharapkan dapat menjadi aplikasi sederhana yang membantu pengelolaan data reservasi sekaligus menjadi sarana penerapan konsep Algoritma dan Struktur Data.

Melalui proyek ini, setiap anggota kelompok memperoleh pengalaman dalam mengembangkan program Python, membagi tanggung jawab, menguji fitur, mendokumentasikan perangkat lunak, serta berkolaborasi menggunakan Git dan GitHub.

---

**Program Studi Sistem Informasi**  
**Fakultas Teknologi Informasi**  
**Universitas Merdeka Malang**