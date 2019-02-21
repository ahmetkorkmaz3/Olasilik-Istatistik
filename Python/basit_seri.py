n = int(input("Kaç adet sayı girmek istersiniz ?"))
list= []

for i in range(n):
    list.append(int(input("Sayı giriniz :")))

list.sort()

for i in range(0, len(list)):
    print(list[i])
