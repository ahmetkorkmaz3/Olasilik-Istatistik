import random

min_deger = int(input("Minimum değeri giriniz :"))
max_deger = int(input("Maximum değer giriniz :"))
adet = int(input("Kaç adet sayi üretmek istiyorsunuz :"))

if min_deger >= max_deger:
    print("Hatalı giriş yaptınız. Minimum değer, maximum değerden büyük veya eşit olmaz")
else:
    list = []
    if (max_deger - min_deger) > adet:
        i = 0
        while(i < adet):
            deger = random.randint(min_deger, max_deger)
            if not(deger in list):
                list.append(deger)
                i += 1
    else:
        for i in range(0, adet):
            list.append(random.randint(min_deger, max_deger))

for i in range(len(list)):
    print(list[i])
