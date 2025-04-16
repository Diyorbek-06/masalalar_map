# #1
# sonlar = [4, 19,111, 55]
#
# natija = []
#
# for i in sonlar:
#     raqamlar = len(str(abs(i)))
#     natija.append(i * raqamlar)
# print(natija)


##2
# sozlar = ["mEn", "WerrAs", "pOll"]
# kattalari = []
# kichiklari = []
#
# for soz in sozlar:
#     katta = 0
#     kichik = 0
#
#     for i in soz:
#         if i.islower():
#             kichik += 1
#         elif i.isupper():
#             katta += 1
#
#     kichiklari.append(kichik)
#     kattalari.append(katta)
#
# for i in range(len(sozlar)):
#     print(f"{sozlar[i]} so'zda: Kichik harflar: {kichiklari[i]}, Katta harflar: {kattalari[i]}")

##3
# sonlar = [3, 8, 15, 22, 7, 10, 6]
# berilgan_son = int(input("son kiriting: "))
#
# juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
#
# eng_yaqin_juft = min(juft_sonlar, key=lambda x: abs(x - berilgan_son))
#
# kvadrat = list(map(lambda x: x**2, [eng_yaqin_juft]))[0]
#
# print(f"Eng yaqin juft son: {eng_yaqin_juft}")
# print(f"Kvadrati: {kvadrat}")


## 4
# from collections import Counter
#
# matn = input("matn yoki so'z kiritin:")
# harf_soni = Counter(matn)
#
# yangi_soz = ''.join(map(lambda x: x if harf_soni[x] <= 2 else '', matn))
#
# print(f"Yangi so'z: {yangi_soz}")


# #5
# a = [10, 40, 50, 90]
# b = [20, 30, 40, 10]
# c = [60, 40, 20, 5]
#
# uchliklar = list(zip(a, b, c))
#
# natija = list(filter(lambda x: sum(x) > 100, uchliklar))
#
# print("qo'shsa yig'indisi 100 dan katta chiqadigan to'plamlar:", natija)


# #6
# import math
#
# sonlar = [145, 12, 34, 100]
#
# natija = list(map(lambda son: sum(math.factorial(int(r)) for r in str(son)), sonlar))
#
# print(natija)

#7
# import math
#
# sonlar = [3, 4, 8, 10, 16 , 81, 45]
#
# ildiz_olish = map(lambda x: math.sqrt(x), sonlar)
#
# ildiz_chiqadiganlari = list(filter(lambda x: x.is_integer(), ildiz_olish))
#
# print("ildiz chiqadiganlari:" , ildiz_chiqadiganlari)


# #8
# def tub(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# sozlar = ["qachon", "men", "diyorbek", "banana", "kitob", "bir", "dastur"]
#
# natija = list(filter(lambda x: tub(len(x)), sozlar))
# print(natija)


# #9
# sozlar = ["qasamki", "dasturxon", "Mevalar"]
#
# natija = list(map(lambda x: ''.join(sorted(x, reverse=True)).capitalize(), sozlar))
#
# print(natija)

# #10
# sonlar = [1, 2, 3, 4, 5, 6]
#
# juft_kvlar = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, sonlar)))
#
# print(juft_kvlar)

# #11
# sonlar = [34, 67, 21]
#
# natija = list(map(lambda x: sum(map(int, str(x))), sonlar))
#
# print("Raqamlar yig'indilari:", natija)


# #12
# sozlar = input("So‘zlarni kiriting: ").split()
#
# natija = list(filter(lambda s: all(harf == s[0] for harf in s), sozlar))
#
# print("Barcha harflari bir xil bo‘lgan so‘zlar:", natija)


# #13
# import math
#
# sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
# natija = list(map(lambda x: math.factorial(x), filter(lambda x: x % 3 == 0, sonlar)))
#
# print("3 ga karrali sonlarning faktoriallari:", natija)


# #14
# sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
#
# natija = list(map(lambda t: t[0] * t[1], enumerate(sonlar)))
#
# print("Indeksga ko‘paytirilgan natijalar:", natija)


# #15
# sozlar = input("So‘zlarni kiriting: ").split()
#
# natija = list(map(lambda s: s.capitalize(), filter(lambda s: s == s[::-1], sozlar)))
#
# print("Bosh harf bilan yozilgan palindrom so‘zlar:", natija)



