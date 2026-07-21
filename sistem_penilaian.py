
# # ==========================================================
# #                UJIAN PRAKTIK PYTHON
# #                  SISTEM NILAI SISWA
# # ==========================================================

# Buatlah program Python menggunakan:

# - def
# - global
# - return
# - while
# - if-elif-else
# - input()
# - int()
# - float()

# Program memiliki menu sebagai berikut:

# =========================
#     SISTEM NILAI SISWA
# =========================

# 1. Input Data Siswa
# 2. Lihat Hasil
# 3. Cek Kelulusan
# 4. Reset Data
# 5. Keluar

# Pilih :

# ==========================================================
# Jika memilih MENU 1 (Input Data Siswa)
# ==========================================================

# =========================
#    INPUT DATA SISWA
# =========================

# Nama Siswa   :
# NIS          :
# Nilai Tugas  :
# Nilai UTS    :
# Nilai UAS    :

# Data berhasil disimpan.

# ==========================================================
# Jika memilih MENU 2 (Lihat Hasil)
# ==========================================================

# =========================
#       HASIL SISWA
# =========================

# Nama          :
# NIS           :

# Nilai Tugas   :
# Nilai UTS     :
# Nilai UAS     :

# -------------------------

# Nilai Akhir   :

# Rumus Nilai Akhir :

# (Tugas × 20%)
# +
# (UTS × 30%)
# +
# (UAS × 50%)

# ==========================================================
# Jika memilih MENU 3 (Cek Kelulusan)
# ==========================================================

# =========================
#    HASIL KELULUSAN
# =========================

# Nama          :
# NIS           :
# Nilai Akhir   :

# Grade         :
# Status        :

# Ketentuan Grade :

# Nilai ≥ 85  = A
# Nilai ≥ 75  = B
# Nilai ≥ 65  = C
# Nilai ≥ 50  = D
# Nilai < 50  = E

# Status :

# Nilai ≥ 65  = Lulus
# Nilai < 65  = Tidak Lulus

# ==========================================================
# Jika memilih MENU 4 (Reset Data)
# ==========================================================

# =========================
#       RESET DATA
# =========================

# Data berhasil direset.

# Semua data kembali menjadi:

# nama_siswa = ""
# nis = 0
# nilai_tugas = 0
# nilai_uts = 0
# nilai_uas = 0
# nilai_akhir = 0

# ==========================================================
# Jika memilih MENU 5 (Keluar)
# ==========================================================

# =========================
#  PROGRAM SELESAI
# =========================

# Terima kasih telah menggunakan program.

# ==========================================================
# BONUS (+10)
# ==========================================================

# Apabila user memilih Menu 2 atau Menu 3 sebelum menginput data, tampilkan pesan:

# =========================
#       PERINGATAN
# =========================

# Data siswa belum diinput.
# Silakan pilih Menu 1 terlebih dahulu.

# ==========================================================
# Function yang WAJIB dibuat
# ==========================================================

# def menu()
# def input_data()
# def lihat_hasil()
# def cek_kelulusan()
# def reset_data()

# ==========================================================



nama_siswa = ""
nis = 0
nilai_tugas = 0
nilai_uts = 0
nilai_uas = 0
nilai_akhir = 0


def menu():
    print ("===========================")
    print ("      SISTEM NILAI SISWA   ")
    print ("===========================")
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

    print ("\n=========================")
    print ("        HASIL SISWA      ")
    print ("=========================\n")

    print ("Nama : ", nama_siswa)
    print ("NIS : ", nis)
    print ()
    print ("Nilai Tugas : ", nilai_tugas)
    print ("Nilai UTS : ", nilai_uts)
    print ("Nilai UAS : ", nilai_uas)
    print ()
    print ("-------------------------\n")
    print ("Nilai Akhir : ", nilai_akhir)
    
def cek_kelulusan():
    global nilai_akhir 

    if nilai_akhir >= 85:
        grade = "A"

    elif nilai_akhir >= 75:
        grade = "B"

    elif nilai_akhir >= 65:
        grade = "C"

    elif nilai_akhir >= 50:
        grade = "D"

    else:
        grade = "E"

    if nilai_akhir >= 65:
        status = "lulus"

    else:
        status = "tidak lulus"

    return grade, status

def reset_data():

    global nama_siswa
    global nis
    global nilai_tugas
    global nilai_uts
    global nilai_uas
    global nilai_akhir

    nama = ""
    nis = 0
    nilai_tugas = 0
    nilai_uts = 0
    nilai_uas = 0
    nilai_akhir = 0
    

    print("Data berhasil direset.")

jalan = True

while jalan:

    menu()

    pilihan = input("Masukan Pilihan : ")

    if pilihan == "1":
        input_data()

    elif pilihan == "2":
        lihat_hasil()
    
    elif pilihan == "3":
        grade, status = cek_kelulusan()
        print ("\n=========================")
        print ("      HASIL KELULUSAN    ")
        print ("=========================\n")
        print ("Nama : ", nama_siswa)
        print ("NIS : ", nis)
        print ("Nilai Akhir : ", nilai_akhir)
        print ("Grade : ", grade)
        print ("Status : ", status)
        print()

    elif pilihan == "4":
        reset_data()

    elif pilihan == "5":
        print ("PROGRAM SELESAI")

        jalan = False
    
    else:
        print ("MENU TIDAK TERSEDIA")