def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

n = int(input("n sayısını giriniz:"))
r = int(input("r sayısını giriniz:"))

permutasyon = faktoriyel(n) / faktoriyel(n - r)

print("Permutasyon sonucu = {}".format(permutasyon))
