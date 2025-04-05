# def foo(num1, num2, *args, **kwargs):
#     print(f'{num1=}')
#     print(f'{num2=}')
#     print(f'{args=}')
#     print(f'{kwargs=}')
#
# foo(1,2, 3, 4, 5, 6, a='7', b='8')
import random

from utils import time_check, attempts, attempts2


# some_list = [1, 2, 3, 4, 5]
# some_dict = {'f': 6, 'g': 7}
#
#
# def moo(a, b, c, d, e, f, g):
#     print(f'{a=}')
#     print(f'{b=}')
#     print(f'{c=}')
#     print(f'{d=}')
#     print(f'{e=}')
#     print(f'{f=}')
#     print(f'{g=}')
#
# moo(*some_list, **some_dict)


# from pprint import pprint as ppr
#
# ppr({'f': 6, 'g': 7})


# def foo():
#     print('foo')
#
# def boo():
#     print('boo')
#
# a = foo
# # a()
#
# funcs = a, foo, boo
#
# for f in funcs:
#     f()


# def foo():
#     def boo():
#         def moo():
#             print('moo')
#         return moo
#     return boo
#
#
# foo()           #  boo
# foo()()         #  boo()     ->  moo
# foo()()()       #  boo()()   ->  moo()  -> 'moo'



# def make_tax_calculator(rate):
#     def tax_calculator(amount):
#         return amount * rate / 100
#     return tax_calculator
#
# calculator_6 = make_tax_calculator(6)
# calculator_15 = make_tax_calculator(15)
#
# print(calculator_6(200))
# print(calculator_15(200))

#
# def wrapper(func, *args, **kwargs):
#     print(f'Вызвана функция {func} с аргументами {args}, {kwargs}')
#     result = func(*args, **kwargs)
#     print(f'{result=}')
#     return result
#
# # print(sum([1, 2, 3, 4]))
# # print(wrapper(sum, [1, 2, 3, 4]))
#
# wrapper(print, 1,2,3,4, sep='~~~', end='\n')



# def decorator(old_func):
#     def new_func(*args, **kwargs):
#         print(f'Вызвана функция {old_func} с аргументами {args}, {kwargs}')
#         result = old_func(*args, **kwargs)
#         print(f'{result=}')
#         return result
#
#     return new_func
#
#
# decorated_sum = decorator(sum)
# decorated_print = decorator(print)
#
# # print(decorated_sum([1,2,3,4]))
# decorated_print(1,2,3,4, sep='~~~', end='\n')


# @time_check     # generate_random_number = time_check(generate_random_number)
# def generate_random_number(iterations):
#     x = 0
#     for _ in range(iterations):
#         x = random.randint(1, 100)
#     return x

# print(generate_random_number(1_000_000))
# decorated_func = time_check(generate_random_number)
# print(decorated_func(20_000_000))

# print(generate_random_number(10_000_000))


# @attempts
# def read_file(path):
#     f = open(path)
#     return f.readline()
#
#
# print(read_file('test2.txt'))


# @time_check
# @attempts
# def read_file(path):    # read_file = time_check(attempts(read_file))
#     f = open(path)
#     return f.readline()
#
#
# print(read_file('test2.txt'))



# @attempts2(count=10, delay=2)
# def read_file(path):
#     f = open(path)
#     return f.readline()
#
#
# print(read_file('test2.txt'))
#
#
#
# class A:
#     @staticmethod
#     def a():
#         print('aaaaa')






def add_authorization(token):
    def wrapper(old_func):
        def new_func(*args, **kwargs):
            if 'headers' in kwargs:
                headers = kwargs['headers']
            else:
                headers = {}
                kwargs['headers'] = headers

            headers['Authorization'] = token

            return old_func(*args, **kwargs)
        return new_func
    return wrapper


@add_authorization(token='токен')
def make_folder(folder_name, headers=None):
    params = {'path': folder_name}
    response = requests.put(f'https://cloud-api.yandex.net/v1/disk/resources',
                            params=params,
                            headers=headers)
    return response.status_code == 201

print(make_folder('Image'))
print(make_folder('Image'))
print(make_folder('Music'))









