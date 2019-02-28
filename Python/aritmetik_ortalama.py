n = int(input("Kaç adet sayı girmek istersiniz ?"))
list= []
toplam = 0

for i in range(n):
    sayi = int(input("Sayı giriniz :"))
    list.append(sayi)
    toplam += sayi

aritmetik_ortalama = toplam / n
print("Aritmetik ortalama = ", aritmetik_ortalama)
