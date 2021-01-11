from view.input_nilai import *
#Rizkyy Coderr
#Jangan Record Masss
data = {}

def tambah_data():
    print("====Tambah Data Dulu Boskuu====")
    global data
    nama = input_nama()
    nim = input_nim()
    nilaiTugas = input_nilaiTugas()
    nilaiUts = input_nilaiUas()
    nilaiUas = input_nilaiUas()
    nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
    data[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
    print("\nData Berhasil Ditambahkan!")
    return data

def ubah_data():
    print("====Ubah Data Dulu Boskuu====")
    nama = input("Masukkan Nama: ")
    if nama in data.keys():
        nim           = input_nim()
        nilaiTugas    = input_nilaiTugas()
        nilaiUts      = input_nilaiUts()
        nilaiUas      = input_nilaiUas()
        nilaiAkhir    = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        data[nama]  = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData Berhasil Di Update!")
    else:
        print("Data tidak ditemukan !!!")

def hapus_data():
    print("====Hapus Data====")
    nama = input("Masukkan Nama:  ")
    if nama in data.keys():
        del data[nama]
        print("Data",nama,"Telah dihapus!")
    else:
        print("Data Mahasiswa Tidak Ada Coba Harap Periksa Kembali".format(nama))
