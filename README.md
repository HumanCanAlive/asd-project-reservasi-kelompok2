# asd-project-reservasi-kelompok2
Project UTS Algoritma dan Struktur Data | 3C Kelompok 2 

=============================================================
Nama Anggota Kelompok 
Kelompok 2
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
- Tahap Pengembangan: Tahap 1 — Array & Struct

## 2. Tugas Masing Masing

1. Gemilang : Ketua kelompok dan integrasi program 
2. Yoses : Fitur tambah reservasi 
3. Panji : Fitur tampilkan dan cari reservasi 
4. Gita : Fitur update status reservasi
5. Rizka : Fitur filter, hapus reservasi, dan dokumentasi

## 3. Deskripsi Proyek

Sistem Reservasi merupakan aplikasi berbasis Command Line Interface (CLI) yang dibuat menggunakan bahasa pemrograman Python untuk membantu pengelolaan data reservasi Hotel.

Aplikasi ini dirancang agar pengguna dapat mengelola data reservasi melalui terminal, mulai dari menambahkan data baru, menampilkan seluruh data, mencari reservasi tertentu, memperbarui status, memfilter berdasarkan status, hingga menghapus data reservasi.

Proyek ini dikembangkan sebagai penerapan konsep Algoritma dan Struktur Data, khususnya penggunaan struktur data list dan dictionary dalam Python.

## 4. Tujuan Proyek

Tujuan pengembangan Sistem Reservasi adalah:

1. Menerapkan konsep algoritma dan struktur data dalam program sederhana.
2. Mempermudah pengelolaan data reservasi tiket atau ruangan.
3. Menerapkan validasi input untuk menjaga konsistensi data.
4. Melatih kerja sama tim dalam pengembangan perangkat lunak.
5. Menggunakan Git dan GitHub untuk mengelola kode sumber serta kontribusi setiap anggota.

## 5. Fitur Sistem

Sistem Reservasi dirancang memiliki enam fitur utama.

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

## 9. Pembagian Tugas

### Gemilang — Ketua dan Integrasi Program

- Membuat menu utama pada `main.py`.
- Mengintegrasikan fungsi yang dikembangkan anggota kelompok.
- Memastikan seluruh fitur dapat diakses melalui menu.
- Menguji jalannya program secara keseluruhan.

### Yoses — Fitur F1: Tambah Reservasi

- Mengembangkan fungsi untuk menambahkan reservasi.
- Memvalidasi kelengkapan input dan keunikan kode reservasi.
- Memvalidasi jenis dan format tanggal sesuai ketentuan proyek.
- Menetapkan status awal reservasi menjadi `Aktif`.

### Panji — Fitur F2 dan F3: Tampilkan dan Cari Reservasi

- Mengembangkan fungsi untuk menampilkan seluruh data reservasi.
- Menyusun tampilan data dalam bentuk tabel.
- Mengembangkan pencarian berdasarkan kode reservasi atau nama pemesan.
- Menguji hasil pencarian dan tampilan data.

### Gita — Fitur F4: Update Status Reservasi

- Mengembangkan fungsi untuk memperbarui status reservasi.
- Memvalidasi kode reservasi sebelum perubahan dilakukan.
- Menerapkan aturan perubahan status sesuai ketentuan proyek.
- Menguji berbagai kondisi perubahan status.

### Rizka — Fitur F5 dan F6: Filter dan Hapus Reservasi

- Mengembangkan fungsi filter berdasarkan status.
- Mengembangkan fungsi penghapusan reservasi berdasarkan kode.
- Menambahkan konfirmasi sebelum penghapusan.
- Menyusun dan memperbarui dokumentasi `README.md`.
- Membantu pengujian fitur filter dan hapus.

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

Pada Tahap 1, sistem memiliki batasan berikut:

- Program dijalankan melalui terminal atau CLI.
- Data reservasi disimpan dalam memori menggunakan list dan dictionary.
- Data tidak tersimpan secara permanen setelah program ditutup.
- Pengelolaan data dilakukan melalui menu yang tersedia.
- Fitur yang dikembangkan berfokus pada kebutuhan reservasi tiket atau ruangan sesuai ruang lingkup proyek.

## 13. Penutup

Sistem Reservasi diharapkan dapat menjadi aplikasi sederhana yang membantu pengelolaan data reservasi sekaligus menjadi sarana penerapan konsep Algoritma dan Struktur Data.

Melalui proyek ini, setiap anggota kelompok memperoleh pengalaman dalam mengembangkan program Python, membagi tanggung jawab, menguji fitur, mendokumentasikan perangkat lunak, serta berkolaborasi menggunakan Git dan GitHub.

---

**Program Studi Sistem Informasi**  
**Fakultas Teknologi Informasi**  
**Universitas Merdeka Malang**