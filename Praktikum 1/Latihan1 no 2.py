#Latihan1 no 2

indo = int(input("Masukan nilai Bahasa Indonesia : "))
ipa = int(input("Masukan nilai IPA : "))
mtk = int(input("Masukan nilai Matematika : "))

print("===================================")

if(indo < 0 or indo > 100):
    print('Maaf input ada yang tidak valid')
elif(ipa < 0 or ipa > 100):
    print('Maaf input ada yang tidak valid')
elif (mtk < 0 or mtk > 100):
    print('Maaf input ada yang tidak valid')

    if (indo > 60 and ipa > 60 and mtk > 70):
        print("Status Kelulusan : LULUS")
    else:
        print("Status Kelulusan : TIDAK LULUS")
