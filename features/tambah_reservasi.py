from calendar import monthrange
from datetime import date

def tambah_reservasi(data_reservasi):
	# Validasi ID: memastikan tidak kosong dan belum digunakan.
	while True:
		kode = input("Masukkan ID/kode reservasi: ").strip()
		if not kode:
			print("Error: ID reservasi tidak boleh kosong.")
		elif any(item.get("kode") == kode for item in data_reservasi):
			print("Error: ID reservasi sudah digunakan. Silakan coba lagi.")
		else:
			break

	# Validasi nama: hanya huruf dan spasi, serta tidak boleh kosong.
	while True:
		nama = input("Masukkan nama pemesan: ").strip()
		if not nama:
			print("Error: Nama pemesan tidak boleh kosong.")
		elif nama.replace(" ", "").isalpha():
			break
		else:
			print("Error: Nama hanya boleh berisi huruf dan spasi, tanpa angka atau simbol.")

	# Validasi jenis reservasi: harus salah satu pilihan yang tersedia.
	jenis_valid = ("Standard", "Deluxe", "Suite")
	while True:
		jenis = input("Masukkan jenis reservasi (Standard/Deluxe/Suite): ").strip()
		if not jenis:
			print("Error: Jenis reservasi tidak boleh kosong.")
		elif jenis.casefold() in (pilihan.casefold() for pilihan in jenis_valid):
			jenis = next(
				pilihan for pilihan in jenis_valid
				if pilihan.casefold() == jenis.casefold()
			)
			break
		else:
			print("Error: Jenis reservasi harus Standard, Deluxe, atau Suite.")

	# Validasi format, tahun, bulan, dan hari secara terpisah.
	while True:
		tanggal = input("Masukkan tanggal reservasi (YYYY-MM-DD): ").strip()
		if not tanggal:
			print("Error: Tanggal reservasi tidak boleh kosong.")
			continue
		try:
			bagian_tanggal = tanggal.split("-")
			if len(bagian_tanggal) != 3 or any(
				len(bagian) != panjang or not bagian.isdigit()
				for bagian, panjang in zip(bagian_tanggal, (4, 2, 2))
			):
				print("Error: Format tanggal salah. Gunakan format YYYY-MM-DD.")
				continue

			tahun, bulan, hari = (int(bagian) for bagian in bagian_tanggal)
			if not 1 <= tahun <= 9999:
				print("Error: Tahun tidak valid. Masukkan tahun antara 0001 dan 9999.")
			elif not 1 <= bulan <= 12:
				print("Error: Bulan tidak valid. Masukkan bulan antara 01 dan 12.")
			elif not 1 <= hari <= monthrange(tahun, bulan)[1]:
				print("Error: Tanggal tidak valid untuk bulan dan tahun tersebut.")
			else:
				date(tahun, bulan, hari)
				break
		except ValueError:
			print("Error: Tanggal tidak valid. Periksa kembali nilai tanggal.")

	# Validasi nomor kamar: harus bilangan bulat positif.
	while True:
		try:
			nomor_kamar = int(input("Masukkan nomor kamar: ").strip())
		except ValueError:
			print("Error: Nomor kamar harus berupa angka bulat, misalnya 101.")
		else:
			if nomor_kamar <= 0:
				print("Error: Nomor kamar harus lebih besar dari 0.")
			else:
				break

	# Validasi lama menginap: harus bilangan bulat positif.
	while True:
		try:
			lama_menginap = int(input("Masukkan lama menginap (hari): ").strip())
		except ValueError:
			print("Error: Lama menginap harus berupa angka bulat, misalnya 2.")
		else:
			if lama_menginap <= 0:
				print("Error: Lama menginap harus lebih dari 0 hari.")
			else:
				break

	# Status ditetapkan otomatis, tanpa input dari pengguna.
	status = "Aktif"

	# Simpan data tervalidasi sebagai dictionary ke dalam list.
	reservasi_baru = {
		"kode": kode,
		"nama_pemesan": nama,
		"jenis_reservasi": jenis,
		"tanggal_reservasi": tanggal,
		"nomor_kamar": nomor_kamar,
		"lama_menginap": lama_menginap,
		"status": status,
	}
	data_reservasi.append(reservasi_baru)

	# Tampilkan pesan sukses.
	print(f"Data reservasi untuk {nama} berhasil ditambahkan!")


if __name__ == "__main__":
	# Contoh pemanggilan fungsi.
	data_reservasi = []
	tambah_reservasi(data_reservasi)
	print(data_reservasi)