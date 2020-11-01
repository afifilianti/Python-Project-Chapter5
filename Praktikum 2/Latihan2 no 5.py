#Latihan2 no 5

print("Hai...nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!")
tebak = int(input("Tebakan Anda : "))
while True:
    if(tebak < 10):
        print("Hehehe...Bilangan tebakan anda terlalu kecil")
        tebak = int(input("Tebakan Anda : "))
    elif(tebak > 10):
        print("Hehehe...Bilangan tebakan anda terlalu besar")
        tebak = int(input("Tebakan Anda : "))
    elif(tebak == 10):
        print("Yeeee...Bilangan tebakan anda benar")
        break
