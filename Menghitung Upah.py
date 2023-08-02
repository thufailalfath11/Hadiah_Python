print ("## PROGRAM PYTHON MENGHITUNG GAJI KARYAWAN ##")
print ("=============================================")
nama = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan : ")

if golongan.lower() == "a":
    upah = 5000
elif golongan.lower() == "b":
    upah = 7000
elif golongan.lower() == "c":
    upah = 8000
elif golongan.lower() == "d":
    upah = 10000
else:
    print("Golongan yang dimasukkan tidak valid.")
    exit()
th
jam_kerja = float(input("Masukkan jam kerja per minggu: "))

if jam_kerja > 48:
    lembur = (jam_kerja - 48) * 4000
else:
    lembur = 0

gaji = (upah * 48) + lembur
print("------------------------")
print("## SLIP GAJI KARYAWAN ##")
print("------------------------")
print("Nama karyawan:", nama)
print("Upah Pokok Rp.", upah * 48)
print("Upah Lembur Rp.", lembur)
print("Upah Total Diterima: Rp.", gaji)
