import random
from Card import Card


class Game:
    def __init__(self):
        self._rand_collection = random.sample(range(1, 91), 90)
        self._card_human = Card()
        self._card_AI = Card()
        self._counter = 90
        self._number = 0

    def _get_random_number(self):
        result = random.choice(self._rand_collection)
        self._rand_collection.remove(result)
        return result

    def _print_card(self, card, info_str):
        print(info_str)
        card.print_card()

    def _game_process(self, card, ai_step):
        if ai_step == 0:
            self._print_card(card, "Карточка игрока:")
        else:
            self._print_card(card, "Карточка компьютера:")
        self._choose_action(card, ai_step)
        self._check_end_game(card, ai_step)

    def start(self):
        ai_step = 0
        while True:
            self._counter -= 1
            self._number = self._get_random_number()
            print("Новый бочонок: {0} (осталось {1})".format(self._number, self._counter))
            self._game_process(self._card_human, ai_step)
            ai_step = 1
            self._game_process(self._card_AI, ai_step)
            ai_step = 0

    def _choose_action(self, card, ai_step):
        while True:
            result, index = self._check_number(card)

            if ai_step == 0:  # ход человека
                answer = input("Зачеркнуть цифру? (y/n): ")
            else:  # ход компьютера
                if int(result) > 0:
                    answer = 'y'
                else:
                    answer = 'n'

            if answer == 'y':
                if int(result) < 0:
                    if ai_step == 0:
                        print("Вы проиграли! Конец игры!")
                    else:
                        print("Компьютер проиграл, поздравляю с победой!")
                    exit()
                else:
                    card[int(index)] = ''
                    if ai_step == 0:
                        print("Вы зачеркнули число {0} в своей карточке".format(result))
                    else:
                        print("Компьютер зачеркнул число {0} в своей карточке".format(result))
                        print("Компьютер зачеркнул существующее число, продолжаем!")
                break
            elif answer == 'n':
                if int(result) > 0:
                    if ai_step == 0:
                        print("Вы проиграли! Конец игры!")
                    else:
                        print("Компьютер проиграл, поздравляю с победой!")
                    exit()
                else:
                    print("Верно! Продолжаем!")
                break
            else:
                print("Неправильно введен ответ. Зачеркнуть цифру? (y/n): ")

    def _check_number(self, card):
        index = -1
        for num in card:
            index += 1
            if num == self._number:
                return num, index
            else:
                continue
        return "-1", "-1"

    def _check_end_game(self, card, ai_step):
        for element in card:
            if element != '':
                return 0
        if ai_step == 1:
            print("Победил компьютер. Конец игры!")
        else:
            print("Поздравляю, вы победили! Конец игры!")
        exit()
