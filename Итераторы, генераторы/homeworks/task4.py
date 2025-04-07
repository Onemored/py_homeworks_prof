import types


def flat_generator(list_of_list):
    for sub_list in list_of_list: # Проходим по каждому списку в списке списков
        for item in sub_list: # Проходим по каждому элементу в текущем списке
            if isinstance(item, list):
                # Если элемент - список, рекурсивно вызываем flat_generator
                yield from flat_generator(item)
            else:
                # Если элемент не список, возвращаем его
                yield item

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()