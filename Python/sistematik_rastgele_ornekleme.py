import random

buyuk_n = int(input("N :"))
kucuk_n = int(input("n :"))

k = int(buyuk_n / kucuk_n)
rastgele_sayi = random.randint(1, k)

print("k = {} a = {}".format(k, rastgele_sayi))

list = []

for i in range(0, kucuk_n):
    list.append(rastgele_sayi + i * k)

print(list)
