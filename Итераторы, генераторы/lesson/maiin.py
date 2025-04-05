# Итерируемый объект — это объект, который можно перебирать.
#
# За правило перебора отвечает итератор, а не сам объект.
#
# Итерируемый объект при попытке его перебрать должен уметь
# возвращать свой итератор, чтобы уже с ним продолжалась работа.
#
# Метод, который возвращает итератор, называется __iter__.
#
# Объект-итератор должен иметь метод __next__,
# который возвращает очередное значение.
#
# Цикл for будет вызывать функцию next от итератора до тех пор,
# пока не получит исключение StopIteration.
#
# Возникновение StopIteration — это ответственность итератора,
# а именно его метода __next__.
#
# Если StopIteration не возникнет никогда, то мы получим бесконечный цикл.
import time
from datetime import datetime
from pprint import pprint

from MyRange import MyRange
from Parrot import Parrot, NewParrot, ParrotWithLimit, my_parrot

# Как пишем мы
# words = [1, 2, 3, 4]
# for item in words:
#     print(item)


# Как пайтон это видит
# words = [1, 2, 3, 4]
# iter_ = iter(words) # iter_ = words.__iter__()
# while True:
#     try:
#         item = next(iter_) # next = iter_.__next__()
#         print(item)
#     except StopIteration:
#         break


words = ['Карамба!', 'Право руля!', 'На абордаж!']
# for word in words:
#     print(word)

# parrot = Parrot(words)
# for swear_word in Parrot(words):
#     print(swear_word)

# for swear_word in NewParrot(words):
#     print(swear_word)

# parrot = ParrotWithLimit(words, 5)
# for swear_word in parrot:
#     print(swear_word)
#
# parrot.learn('Пиастры!')
# print('-' * 20)
# for swear_word in parrot:
#     print(swear_word)


# for i in range(1, 15, 3):
#     print(i)

# for i in MyRange(1, 15, 3):
#     print(i)

from sys import getsizeof
# print(getsizeof(MyRange(1, 999999999, 14)))
#
# start = datetime.now()
# l_ = []
# for i in range(100_000_000):
#     l_.append(i)
# end = datetime.now()
#
# print(getsizeof(l_))
# print(end - start)



# def simple_generator():
#     i = 1
#     while True:
#         yield i
#         i += 1
#         time.sleep(0.5)
#         if i == 5:
#             break
#
# for i in simple_generator():
#     print(i)
#
# def non_simple_generator(num):
#     for i in simple_generator():
#         yield i * 1
#         yield i * 2
#         yield i * 3
#         yield i * 4
#
#
# for i in non_simple_generator(5):
#     print(i)


# for swear_word in my_parrot(words, 7):
#     print(swear_word)



# Итератор :
#     Используется, когда нужен полный контроль над процессом итерации.
#     Подходит для сложных структур данных, где требуется кастомная логика.
# Генератор :
#     Используется, когда нужно быстро создать итератор для обработки данных.
#     Подходит для простых случаев, таких как обход последовательностей,
#     генерация чисел или чтение больших файлов.

# пример для чтения больших файлов
def read_file(path):
    with open(path, 'r') as f:
        yield f.readline()



# list_1 = [i * i for i in range(100_000) if i * 10_000 == 0]
# start = datetime.now()
# list_1 = [i * i
#           for i in range(100_000_000)
#           if i * 10_000 == 0]
# end = datetime.now()
# print(end - start)

# start = datetime.now()
# generator_1 = (i * i for i in range(100_000_000) if i % 10_000 == 0)
# end = datetime.now()
# print(end - start)
# print(generator_1)
# print(type(generator_1))

# for i in generator_1:
#     print(i)
#
# start = datetime.now()
# list_2 = []
# for i in range(100_000_000):
#     if i * 10_000 == 0:
#         list_2.append(i * i)
# end = datetime.now()
# print(end - start)
#
# print(list(generator_1) == list_2)

# set_1 = {i * i for i in range(100_000) if i % 10_000 == 0}
# print(set_1)
#
# dict_1 = {str(i): i * i for i in range(100_000) if i % 10_000 == 0}
# pprint(dict_1)