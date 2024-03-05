from random import shuffle
import os  
"""

Карта:
    вес
    цена
    масть

Колода: всего карт = вес * масть
    в 1 масти 6, 7, 8, 9, 10, валет, дама, король, туз

Игроки от 2 штук


Колода перемешивается


Каждому игроку выдаются по 2 карты игроку


Игрок видит только свои карты


Задача - вес всех карт игрока = 21


Ход игрока:
    оставить и больше не набирать
    или взять еще карту (сколько угодно раз)


Все игроки должны закончить ход


Если у игрока сумма васа карт > 21,он проиграл
если у всех игроков проирыш, то это ничья


Выигрывает тот у кого больше очков, и тот кто не проиграл


"""
def get_dect() -> list[dict]:
    suits = ['бубны', 'черви', 'пики', 'крести']
    names = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    deck = []

    for suit in suits:
        for name in names:
            if name in ('валет', 'дама', 'король'):
                value = 10
            elif name == 'туз':
                value = 11
            else:
                value = int(name)
            Cart = {
                'имя': name,
                'цена': value,
                'масть': suit
            }
            deck.append(Cart)

    return deck



def get_players() -> list[dict]:
    player_1 = {
        'человек': True,
        'имя': 'Вася',
        'карты': [],
        'счет': 10
    }
    player_2 = {
        'человек': True,
        'имя': 'Ася',
        'карты': [],
        'счет': 10
    }
    return [player_1, player_2]


def deal_cards(num: int) -> None:
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop(-1))


def show_cards() -> None:
    for cart in player['карты']:
            print(cart['имя'], cart['масть'])


deck = get_dect()
shuffle(deck)
players = get_players()
deal_cards(2)


for player in players:
    for i in range(1):
        player['карты'].append(deck.pop(-1))

for player in players:
    while True:
        os.system('cls') 
        show_cards()
        player_option = input('Взять картe? y/n: ')
        if player_option == 'y':
            player['карты'].append(deck.pop(-1))
        else:
            break

os.system('cls') 
for player in players: 
    show_cards()
    total = 0
    for cart in player['карты']:
        total += cart['цена']
    print(f'У {player["имя"]} {total} очков')
    print('-' * 20)

# У каждого игрока нужно хранить сумму очков

