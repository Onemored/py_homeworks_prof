import os
from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        # Записываем время вызова функции
        call_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Получаем имя функции
        function_name = old_function.__name__
        # Преобразуем аргументы в строки
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{key}={repr(value)}" for key, value in kwargs.items()]
        all_args = ", ".join(args_repr + kwargs_repr)

        # Вызываем оригинальную функцию
        result = old_function(*args, **kwargs)

        # Формируем строку для записи в лог
        log_entry = (
            f"{call_time} - {function_name}({all_args}) -> {repr(result)}\n"
        )

        # Записываем в файл
        with open('main.log', 'a', encoding='utf-8') as log_file:
            log_file.write(log_entry)

        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path, encoding='utf-8') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()