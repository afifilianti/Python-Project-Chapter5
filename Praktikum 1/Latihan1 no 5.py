#Latihan1 no 5

kode = input("Masukkan kode karyawan : ")
nama = input("Masukkan nama karyawan : ")
golongan = input("Masukkan golongan : ")
status = input("Masukkan status (1: menikah, 2: blm) : ")
if(status == "1"):
    jumlahAnak = int(input("Masukkan Jumlah Anak : "))
    tunjanganSuamiIstri = 10 / 100
    tunjanganAnak = 5 / 100 * jumlahAnak
    statusMenikah = "Sudah Menikah"
else:
    jumlahAnak = 0
    tunjanganSuamiIstri = 0
    tunjanganAnak = 0
    statusMenikah = "Belum Menikah"
print("====================================")

print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------")

print("Nama Karyawan :", nama + "(Kode : ", kode + ")")
print("Golongan :", golongan)
print("Status Menikah : ", status)
print("Jumlah Anak : ", str(jumlahAnak))
print("------------------------------------")

if(golongan == "A"):
    gajiPokok = 10000000
    potongan = 2.5
    jumlahTunjanganSuamiIstri = 10000000 * tunjanganSuamiIstri
    jumlahTunjanganAnak = 10000000 * tunjanganAnak
    gajiKotor = 10000000 + jumlahTunjanganSuamiIstri + jumlahTunjanganAnak
    jumlahPotongan = 2.5 / 100 * gajiKotor
    gajiBersih = gajiKotor - jumlahPotongan
elif(golongan == "B"):
    gajiPokok = 8500000
    potongan = 2.0
    jumlahTunjanganSuamiIstri = 8500000 * tunjanganMenikah
    jumlahTunjanganAnak = 8500000 * tunjanganAnak
    gajiKotor = 8500000 + jumlahTunjanganSuamiIstri + jumlahTunjanganAnak
    jumlahPotongan = 2.0 / 100 * gajiKotor
    gajiBersih = gajiKotor - jumlahPotongan
elif(golongan == "C"):
    gajiPokok = 7000000
    potongan = 1.5
    jumlahTunjanganSuamiIstri = 7000000 * tunjanganMenikah
    jumlahTunjanganAnak = 7000000 * tunjanganAnak
    gajiKotor = 7000000 + jumlahTunjanganSuamiIstri + jumlahTunjanganAnak
    jumlahPotongan = 1.5 / 100 * gajiKotor
    gajiBersih = gajiKotor - jumlahPotongan
elif(golongan == "D"):
    gajiPokok = 5500000
    potongan = 1.0
    jumlahTunjanganSuamiIstri = 5500000 * tunjanganMenikah
    jumlahTunjanganAnak = 5500000 * tunjanganAnak
    gajiKotor = 5500000 + jumlahTunjanganSuamiIstri + jumlahTunjanganAnak
    jumlahPotongan = 1.0 / 100 * gajiKotor
    gajiBersih = gajiKotor - jumlahPotongan
print("Gaji Pokok : Rp", gajiPokok)
print("Tunjangan Istri/Suami : Rp", jumlahTunjanganSuamiIstri)
print("Tunjangan Anak : Rp", jumlahTunjanganAnak)
print("------------------------------------ +")

print("Gaji Kotor : Rp", gajiKotor)
print("Potongan ("+ str(potongan) + "%) : Rp", str(jumlahPotongan))
print("------------------------------------ -")

print("Gaji Bersih : Rp", gajiBersih)
