import random
def sifre_olusturucu(karakter):
    crts1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    parola = ""
    a=0
    while a<karakter:
         b = random.choice(crts1)
         parola=parola+b
         a+=1
    print(parola)
    secim=input("Şifre Kayıt edilsin mi (e/h) :")
    if secim=="e":
        with open("Sifreler.txt","a",encoding="utf-8") as file:
            sifre=parola+"\n"
            file.write(sifre)
        print("Şifre Kaydedildi.")
        return sifre
    else:
        print("Şifre kaydedilmedi.")


def sifre_oku():
    with open("Sifreler.txt","r",encoding="utf-8") as file:
        for i in file:
            print(i,end="")


while True:
    islem=int(input("1-Yeni şifre oluştur\n2-Şifreleri göster\n3-Çıkış\n"))
    if islem==1:
        karakter=int(input("Kaç karakterli:"))
        sifre_olusturucu(karakter)
    elif islem==2:
        sifre_oku()
    else:
        break

