# 1.
# Дан список чисел. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке

# sp = input("Введите список").split()
# sp_1 = []
# for i in sp:
#     if sp.count(i) == 1:
#         sp_1.append(i)
#         print(sp_1)

# 2.
# Дан список . Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые 2 элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# sp = [int(s) for s in input(). split()]
# ch_count = 0
# for i in range(len(sp)):
#     for j in range(i + 1, len(sp)):
#         if sp[i] == sp[j]:
#             ch_count += 1
# print(ch_count)

# 3.
# Даны два кортежа: с_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231),
# с_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# Определить: 1. Сумма элементов какого из кортежей больше
# 2. Порядковые номера минимальных и максимальных элементов этих кортежей.
# c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# if sum(c_1) > sum(c_2):
#     print("Сумма больше в кортеже с_1")
# else:
#     print("Сумма больше в кортеже с_2")
# max_1 = max(c_1)
# max_2 = max(c_2)
# min_1 = min(c_1)
# min_2 = min(c_2)
# print(f'Порядковые номера минимальных элементов кортежей  с_1 - {c_1.index(min_1)}, c_2 - {c_2.index(min_2)}')
# print(f'Порядковые номера максимальных элементов кортежей с_1 - {c_1.index(max_1)}, c_2 - {c_2.index(max_2)}')

# 4.
# Дана строка 'An apple a day keeps the doctor away'
# Создайте из нее словарь: ключи - элементы строки,
# значения- количество вхождений данного элемета в строку.
# a = ' An apple a day keeps the doctor away'
# a_set = {i: a.count(i) for i in a}
# print(a_set)

# 2 способ:
# from collections import Counter
# a = ' An apple a day keeps the doctor away'
# counter = Counter(a)
# print(counter)

# 6
# Даны 2 списка чисел. В них могут быть одинаковые числа. Посчитать, сколько в списках одинаковых чисел
# a_1 = set(input().split())
# a_2 = set(input().split())
# b = list(a_1 & a_2)
# print(len(b))

# 7
# Напишите программу, демонстрирующую работу try/except/finally
# try:
#     a = int(input())
#     b = int(input())   # если пользователь введет не число будет ошибка
#     c = a/b   # если пользователь введет ноль возникнет ошибка
# except ValueError:
#     print("Вы ввели не число")
# except ZeroDivisionError:
#     print("Делить на 0 нельзя")
# except:
#     print("все остальные ошибки")

# ecть еще дополнительные:
# else:
#     print("Ошибок не было")
# finally:
#     print("Выполнится в любом случае")


# 5
# Клиент приходит в кондитерскую. Реализуйте кондитерскую:
# 1. Если клиент хочет посмотреть описание -название и состав
# 2. Цену -название и стоимость
# 3. Количество - название и сколько осталось.
# 4. Купить - стоимость покупки и остаток в кондитерской
# Словарь: ключи - название продукции, значения - описание, стоимость, количество
# sonset = {"Торт "Наполеон": [['сливки', 'мука', 'сахар', 'сметана', 'яйца'], 12, 5],
#             "Торт "Милашка": [['сливки', 'какао', 'яйца', 'мука', 'ванилин', 'сахар'], 10, 6],
#             "Торт "Киевский": [['масло сливочное','шоколад', 'мука', 'яйца', 'клубника'],12, 1]
#           }
# pr = input("Какой торт вы хотели бы приобрести? ")
# pr_1 = input("Чтобы вы хотели уточнить?")
# pr_2 = input("Торт "Наполеон?)
# pr_3 = input("Сколько торта вам положить?")


for k, v in sonset.items():
    if buy == k:
        bought = pr_3 * v[1] / 100
