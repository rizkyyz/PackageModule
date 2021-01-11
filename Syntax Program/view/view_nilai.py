from model.daftar_nilai import *
#Rizkyyz Ganss parah
#Jangan Di Record Ya masszz
def cetak_daftar_nilai():
    print("====Lihat Data====")
    if data.items():
        print("\n Daftar Nilai Mahasiswa ")
        print("==================================================================")
        print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        i = 0
        for x in data.items():
            i += 1
            print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2],
                                                                                        x[1][3], x[1][4], i))
        print("==================================================================")
    else:
        print("\n Daftar Nilai Mahasiswa ")
        print("==================================================================")
        print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        print("|                          DATA GADA BOSS KU                      |")
        print("==================================================================")

def cetak_hasil_pencarian():
    print("====Cari Data====")
    nama = input("Masukkan Nama        : ")
    if nama in data.keys():
        print("\n Daftar Nilai Mahasiswa ")
        print("==============================================================")
        print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
        print("==============================================================")
        print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6}  |"
              .format(nama, data[nama][0], data[nama][1],data[nama][2], data[nama][3],data[nama][4]))
        print("==============================================================")
    else:
        print("Data {0} Tidak Ada ".format(nama))