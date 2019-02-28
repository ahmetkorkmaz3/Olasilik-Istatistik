n = int(input("Kaç adet sayı girmek istersiniz ?"))
list= []

for i in range(n):
    list.append(int(input("Sayı giriniz :")))

list.sort()

if (n % 2) == 1:
    orta = ((n + 1) / 2) - 1
    print("Medyan elemanı : ", list[int(orta)])
else:
    orta = int(n / 2) - 1
    orta = (list[orta] + list[orta + 1]) / 2
    print("Medyan elemanı :", orta)
