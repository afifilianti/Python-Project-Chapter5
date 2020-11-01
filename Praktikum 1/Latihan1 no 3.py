#Latihan1 no 3

indo = int(input("Masukan nilai Bahasa Indonesia : "))
ipa = int(input("Masukan nilai IPA : "))
mtk = int(input("Masukan nilai Matematika : "))

print("===================================")

if (indo > 60 and ipa > 60 and mtk > 70):
    print("Status Kelulusan : LULUS")
else:
    print("Status Kelulusan : TIDAK LULUS")
    print("Sebab :")

    if(indo < 60):
        print("- Nilai Bahasa Indonesia kurang dari 60")
    if(mtk < 70):
        print("- Nilai matematikanya kurang dari 70")
