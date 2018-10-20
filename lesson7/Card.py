import random


class Card:
    def __init__(self):
        self._loto_card = ['' for i in range(27)]
        self._random_collection = []
        self._fill_card()

    def __iter__(self):
        return iter(self._loto_card)

    def __setitem__(self, key, value):
        self._loto_card[key] = value

    def _generate_numbers(self):
        self._random_collection = sorted(random.sample(range(1, 91), 15))

    def _fill_card(self):
        self._generate_numbers()
        k = 0
        for i in random.sample(range(3), 3):
            random_indexes = sorted(random.sample(range(0 + i * 9, 9 + i * 9), 5))
            for element in random_indexes:
                self._loto_card[element] = self._random_collection[k]
                k += 1

    def print_card(self):
        k = 0
        for element in self._loto_card:
            print(element, end=' ')
            k += 1
            if k % 9 == 0:
                print('\n')