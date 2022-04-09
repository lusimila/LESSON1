# def sum_namb(ls_namb):
#     return sum(ls_namb)
# print(sum_namb([5, 4, 7]))

# def muit_1(ls):
#     res = 1
#     for i in ls:
#         res *= i
#     return res
# print(muit_1([2,4,6]))

# Создайте функцию count_letters,
# которая принимает на вход фразу и
# подсчитывает, какое количество в ней
# строчных(down) и заглавных (up) букв.
# Функция должна вывести на

# def count_letter(st_1):
#     a = 0
#     b = 0
#     for i in st_1:
#         if i isalpa() and i.islolower():
#             down += 1
#         eiif i.isalpa() and i.isupper():

# Напишите программу ввода двух слов  через  пробел.Сформируйте новую строку,
# продублировав первое слово дважды, а второе - трижды (все слова  в  результирующей
# строке должны идти через пробел).Результат выведите на экран. Программу следует
# реализовать без использования F - строк, а с применением оператора дублирования строк.
# hello python    hello hello python python python
s1, s2 = map(str.strip, input().split())
print((s1+" ")*2, (s2+" ")*3, sep= "")










