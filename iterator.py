class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.end = len(self.list_of_list)

    def __iter__(self):
        self.counter = 0
        self.inner_counter = 0
        return self

    def __next__(self):
        if self.counter >= self.end:
            raise StopIteration
        while self.inner_counter >= len(self.list_of_list[self.counter]):
            self.counter += 1
            self.inner_counter = 0
            if self.counter >= self.end:
                raise StopIteration
        item = self.list_of_list[self.counter][self.inner_counter]
        self.inner_counter += 1
        return item


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
