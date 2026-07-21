nama_siswa = ""
nis = 0
nilai_tugas = 0
nilai_uts = 0
nilai_uas = 0
niali_akhir = 0

def menu():
    print ("1. Input Data Siswa")
    print ("2. Lihat Hasil")
    print ("3. Cek Kelulusan")
    print ("4. Reset Data")
    print ("5. Keluar")

def input_data():
    global nama_siswa
    global nis
    global nilai_tugas
    global nilai_uts
    global nilai_uas

    nama_siswa = input("Masukan Nama Siswa : ")
    nis = int(input("Masukan NIS : "))
    nilai_tugas = float(input("Masukan Nilai Tugas : "))
    nilai_uts = float(input("Masukan Nilai UTS : "))
    nilai_uas = float(input("Masukan Nilai UAS : "))

def lihat_hasil():
    global nilai_akhir
    nilai_akhir = (nilai_tugas * 20 / 100) + (nilai_uts * 30 / 100) + (nilai_uas * 50 / 100)
    return nilai_akhir

    print ("\n=========================")
    print ("        HASIL SISWA      ")
    print ("=========================\n")

    print ("Nama : ", nama_siswa)
    print ("NIS : ", nis)
    print()
    print ("Nilai Tugas : ", nilai tugas)
    print ("Nilai UTS : ", nilai_uts)
    print ("Nilai UAS : ", niali_uas)

def cek_kelulusan()
    nilai_akhir = ...

