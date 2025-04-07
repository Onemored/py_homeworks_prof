class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list  # Сохраняем список списков
        self.outer_index = 0  # Индекс для отслеживания текущего списка
        self.inner_index = 0  # Индекс для отслеживания текущего элемента в списке

    def __iter__(self):
        return self

    def __next__(self):
        # Проверяем, не достигли ли мы конца внешнего списка
        while self.outer_index < len(self.list_of_list):
            # Получаем текущий список
            current_list = self.list_of_list[self.outer_index]

            # Проверяем, не достигли ли мы конца текущего списка
            if self.inner_index < len(current_list):
                # Если нет, то возвращаем текущий элемент и увеличиваем индекс
                item = current_list[self.inner_index]
                self.inner_index += 1
                return item
            else:
                # Если текущий список закончился, переходим к следующему
                self.outer_index += 1
                self.inner_index = 0

        # Если все списки пройдены, поднимаем исключение StopIteration
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()