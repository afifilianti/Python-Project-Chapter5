#Latihan2 no 6

print("Hai...nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!")
tebak = int(input("Tebakan Anda : "))
poin = 0
while True:
    if(tebak < 10):
        print("Hehehe...Bilangan tebakan anda terlalu kecil")
        tebak = int(input("Tebakan Anda : "))
        poin += 2
    elif(tebak > 10):
        print("Hehehe...Bilangan tebakan anda terlalu besar")
        tebak = int(input("Tebakan Anda : "))
        poin += 2
    elif(tebak == 10):
        print("Yeeee...Bilangan tebakan anda benar")
        score = 100 - poin
        print("Score Anda : " + str(score))
        break
