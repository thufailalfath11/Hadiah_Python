print ("## PROGRAM PYTHON MENGHITUNG POTONGAN HARGA ##")
print ("==============================================")

total = int(input("Masukkan total belanja: Rp. "))

if total < 100000:
    diskon = 0.0
    print ("Anda Tidak Mendapatkan Diskon")
    
elif total <= 500000:
    diskon = 0.1
    print ("Anda Mendapatkan Diskon Sebesar 10%")

elif total <= 1000000:
    diskon = 0.2
    print ("Anda Mendapatkan Diskon Sebesar 20%")
else:
    diskon = 0.3
    print ("Anda Mendapatkan Diskon Sebesar 30%")

jumlah_diskon = total * diskon
print("----------------------------------------------")
print("Jumlah diskon yang didapat Rp.", jumlah_diskon)
harga_setelah_diskon = total - (total * diskon)
print("Total Dibayarkan Rp.", harga_setelah_diskon)