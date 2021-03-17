from random import randint
sayi1 = input("1 ile 90 arasında 1.sayıyı giriniz :")
sayi2 = input("1 ile 90 arasında 2.sayıyı giriniz :")
sayi3 = input("1 ile 90 arasında 3.sayıyı giriniz :")
sayi4 = input("1 ile 90 arasında 4.sayıyı giriniz :")
sayi5 = input("1 ile 90 arasında 5.sayıyı giriniz :")
sayi6 = input("1 ile 90 arasında 6.sayıyı giriniz :")

girilensayi = [sayi1,sayi2,sayi3,sayi4,sayi5,sayi6]
print(sorted(girilensayi))

i = 0
secilenler = [0,0,0,0,0,0]
for rastgele in secilenler:
    while i < len(secilenler):
        secilen = randint(1, 90)
        if secilen not in secilenler:
            secilenler[i] = secilen
            i+=1
    print(sorted(secilenler))
    i=0
if (girilensayi==secilenler):
    print("Tebrikler Sayısal Lotoyu Kazandınız")
else:
    print("Maalesef Kaybettiniz")