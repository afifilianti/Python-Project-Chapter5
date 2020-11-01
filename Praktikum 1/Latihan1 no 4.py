#Latihan1 no 4

kode = input("Masukkan kode karyawan : ")
nama = input("Masukkan nama karyawan : ")
golongan = input("Masukkan golongan : ")
print("====================================")

print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------")

print("Nama Karyawan :", nama + "(Kode : ", kode + ")")
print("Golongan :", golongan)
print("------------------------------------")

if(golongan == "A"):
    gajiPokok = 10000000
    potongan = 2.5
    jumlahPotongan = 2.5 / 100 * 10000000
    gajiBersih = 10000000 - jumlahPotongan
elif(golongan == "B"):
    gajiPokok = 8500000
    potongan = 2.0
    jumlahPotongan = 2.0 / 100 * 8500000
    gajiBersih = 8500000 - jumlahPotongan
elif(golongan == "C"):
    gajiPokok = 7000000
    potongan = 1.5
    jumlahPotongan = 1.5 / 100 * 7000000
    gajiBersih = 7000000 - jumlahPotongan
elif(golongan == "D"):
    gajiPokok = 5500000
    potongan = 1.0
    jumlahPotongan = 1.0 / 100 * 5500000
    gajiBersih = 5500000 - jumlahPotongan
print("Gaji Pokok : Rp", gajiPokok)
print("Potongan ("+ str(potongan) + "%) : Rp", str(jumlahPotongan))
print("------------------------------------")

print("Gaji Bersih : Rp", gajiBersih)
