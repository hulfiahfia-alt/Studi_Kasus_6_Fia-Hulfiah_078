# Studi_Kasus_6_Fia-Hulfiah_078


# Sistem Manajemen Inventaris Barang
Program Python ini digunakan untuk mencatat dan melihat stok barang di sebuah toko kelontong. Data disimpan di file CSV sehingga tidak hilang walaupun program ditutup dan dijalankan lagi.

# Penjelasan Kode

Import dan variabel awal

<img width="1070" height="203" alt="Screenshot 2026-10-08 213209" src="https://github.com/user-attachments/assets/aa43b099-a470-4a84-8bdd-d88bd848ef07" />


import csv : modul untuk membaca dan menulis file CSV.

import os : modul untuk mengecek apakah file sudah ada.

Nama_File : nama file tempat data disimpan. Ditaruh di variabel supaya mudah diganti.

Kolom : daftar judul kolom di baris pertama CSV. Juga dipakai sebagai kunci dictionary.

# siapkan_file()

<img width="1174" height="171" alt="Screenshot 2026-10-08 213836" src="https://github.com/user-attachments/assets/322d20b9-6cd0-41a8-a38e-ad489558af52" />

Mengecek apakah inventaris.csv sudah ada dengan os.path.exists(). Kalau belum ada, file dibuat (mode "w") dan judul kolom ditulis dengan DictWriter.writeheader(). Jika file sudah ada, fungsi ini tidak melakukan apa-apa sehingga data lama aman.

# baca_data()

<img width="978" height="168" alt="Screenshot 2026-10-08 214741" src="https://github.com/user-attachments/assets/22cfab72-32e6-4ff2-98e9-4d14e9f19956" />

Membuka file dalam mode baca ("r") dan membacanya dengan csv.DictReader. Setiap baris menjadi dictionary (kunci = nama kolom), lalu dikumpulkan ke dalam list dengan append dan dikembalikan lewat return.


# tampilkan_data()

<img width="1383" height="257" alt="Screenshot 2026-10-08 215357" src="https://github.com/user-attachments/assets/3d57f378-7af0-4829-94fc-bad1d3be065c" />

Memanggil baca_data(). Jika list kosong, tampil pesan bahwa belum ada data. Jika ada, setiap barang ditampilkan memakai perulangan for.

# tambah_data()

<img width="1123" height="509" alt="Screenshot 2026-10-08 215946" src="https://github.com/user-attachments/assets/afdba774-1116-48a7-bdc1-79752f75d097" />

Meminta input nama, jumlah, harga, dan kode barang lewat input(). Lalu file dibuka dengan mode "a" (append) dan satu baris baru ditulis dengan DictWriter.writerow(). Mode "a" inilah yang membuat data lama tidak terhapus dan data baru tersimpan permanen.

# Menu utama (while True)

<img width="1047" height="523" alt="Screenshot 2026-10-08 220938" src="https://github.com/user-attachments/assets/8195175d-a644-4811-9136-eefc5d13faca" />

Menu ditampilkan di dalam perulangan while True sehingga program berjalan terus-menerus. Pilihan user diproses dengan if / elif / else, dan break dipakai untuk keluar dari perulangan saat user memilih keluar.


# 1. Program berhasil dijalankan

<img width="1584" height="762" alt="Screenshot 2026-10-08 221447" src="https://github.com/user-attachments/assets/c34fc22d-10f8-4624-94aa-463c700773e1" />

<img width="1596" height="554" alt="Screenshot 2026-10-08 221502" src="https://github.com/user-attachments/assets/ec49ed4d-10e6-48da-8001-12720b740c1f" />

# 2. Data baru tetap tersimpan setelah program dijalankan kembali

<img width="1571" height="602" alt="Screenshot 2026-10-08 222057" src="https://github.com/user-attachments/assets/1a777e69-e281-40b1-a09f-fba1fb4d9ab4" />



