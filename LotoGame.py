"""
делаем класс Игра
в нем принимаем 2х игроков и запускаем игру


делаем класс Игрок
в нем создаем карточку
в нем пишем механику игры для игрока

делаем класс Комп
в нем создаем карточку
в нем пишем механику игры для компа

делаем класс Карточка
в нем описываем метод создания карточки
делаем красивый вывод
"""

import random
from itertools import chain
class LotoCard():
    def __init__(self):
        self.card_creator()

    def __str__(self):
        border = '-' * 40 + '\n'
        card_print = '\r' + border
        for line in self.lotocard:
            for cell in line:
                card_print += str( cell ).ljust( 4 )
            card_print += '\n'
        card_print += border
        return card_print

    def card_creator(self):
        self.lotocard = []
        loto_numbers = []
        while len( loto_numbers ) != 15:
            num = random.randint( 1, 90 )
            if num not in loto_numbers:
                loto_numbers.append( num )
        lines = 3
        for line in range( lines ):
            line = sorted( random.sample( loto_numbers, 5 ) )
            for i in range( 4 ):
                line.insert( random.randint( 1, 9 ), ' ' )
            self.lotocard.append( line )
            loto_numbers = list( set( loto_numbers ) - set( line ) )
        return self.lotocard

class Player():
    def __init__(self, name):
        self.name = name
        self.my_card = LotoCard()
        self.lotocard = self.my_card.lotocard

    def player_play(self):
        print(f' lot is {LotoGame.lot}')
        print(self.my_card)
        print(self.name)
        counter = 0
        if input() == 'y':
            if LotoGame.lot not in list(chain(*self.lotocard)):
                print(f'it was {LotoGame.lot} you lost' )
            else:
                for line in self.lotocard:
                    if LotoGame.lot in line:
                        line[line.index(LotoGame.lot)] = '-'
                    if line.count( '-' ) == 5:
                        counter += 1
                        if counter == 1:
                            print( 'you won a line' )
                        elif counter == 2:
                            print( 'you won a 2nd line' )
                        else:
                            print( 'you won a card' )
        print(self.my_card)

class Computer():
    def __init__(self, name = 'computer'):
        self.name = name
        self.my_card = LotoCard()
        self.lotocard = self.my_card.lotocard

    def computer_play(self):
        print(f' lot is {LotoGame.lot}')
        print(self.my_card)
        print(self.name)
        counter = 0
        for line in self.lotocard:
            if LotoGame.lot in line:
                line[line.index(LotoGame.lot)] = '-'
            if line.count( '-' ) == 5:
                counter += 1
                if counter == 1:
                    print( 'computer won a line' )
                elif counter == 2:
                    print( 'computer won a 2nd line' )
                else:
                    print( 'computer won a card' )
        print(self.my_card)

class LotoGame():
    def __init__(self, Player, Computer):
        self.Player = Player
        self.Computer = Computer

    lots = [i for i in range( 1, 91 )]
    lot = 0
    def play(self):
        i = 2
        while True:
            LotoGame.lot = random.choice(LotoGame.lots)
            # print(f'lot is {LotoGame.lot}')
            if i%2 == 0:
                self.Player.player_play()
                i -= 1
            else:
                self.Computer.computer_play()
                i += 1
            LotoGame.lots.remove(LotoGame.lot)


me = Player('new_player')
comp = Computer()

new_game = LotoGame(me, comp)
new_game.play()