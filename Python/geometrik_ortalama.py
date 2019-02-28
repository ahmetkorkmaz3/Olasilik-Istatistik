from math import sqrt

n = int(input("Kaç adet sayı girmek istersiniz ?"))
list= []
carpım = 1

for i in range(n):
    sayi = int(input("Sayı giriniz :"))
    list.append(sayi)
    carpım *= sayi

geometrik_ortalama = sqrt(carpım)
print("Geometrik Ortalama = ", round(geometrik_ortalama, 3))
