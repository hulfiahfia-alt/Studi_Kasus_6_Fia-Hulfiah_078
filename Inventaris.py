import csv
import os

Nama_File = "inventaris.csv"
Kolom = ["Nama Barang", "Jumlah Barang", "Harga Barang", "kode Barang"]

def siapkan_file():
    if not os.path.exists(Nama_File):
        with open(Nama_File, mode = "w", newline = "", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = Kolom)
            writer.writeheader()

def baca_data():
    with open(Nama_File, "r", newline = "", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    return data

def tampilkan_data():
    data = baca_data()

    if data == []:
        print("\nbelum ada data barang di gudang.")
    else:
        for row in data:
            print(row["Nama Barang"], row["Jumlah Barang"], row["Harga Barang"], row["kode Barang"])


def tambah_data():
    print("--- Tambah Barang Baru ---")
    nama_barang = input("Nama Barang: ")
    jumlah_barang = input("Jumlah Barang: ")
    harga_barang = input("Harga Barang: ")
    kode_barang = input("Kode Barang: ")

    with open(Nama_File, mode = "a", newline = "", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = Kolom)
        writer.writerow({
            "Nama Barang": nama_barang,
            "Jumlah Barang": jumlah_barang,
            "Harga Barang": harga_barang,
            "kode Barang": kode_barang
        })

    print("barang berhasil ditambahkan")

siapkan_file()

while True:
    print("\n=== Sistem Inventaris Toko ===")
    print("1. Tampilkan Data Barang")
    print("2. Tambah Data Barang")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem inventaris.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")