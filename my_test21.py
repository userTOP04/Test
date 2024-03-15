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
        'счет': 10,
        'сумма': 0
    }
    player_2 = {
        'человек': False,
        'имя': 'Ася',
        'карты': [],
        'счет': 10,
        'сумма': 0
    }
    return [player_1, player_2]


def deal_cards(num: int) -> None:
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop(-1))


def show_cards() -> None:
    for cart in player['карты']:
            print(cart['имя'], cart['масть'])


def get_total_cards_values(player: dict) -> int:
    total = 0
    for cart in player['карты']:
        total += cart['цена']
    return total


deck = get_dect()
shuffle(deck)
players = get_players()
deal_cards(2)
max_cards = len(deck) // len(players)

for player in players:
    while True:
        os.system('cls')
        print(player['имя']) 
        show_cards()
        player['сумма'] = get_total_cards_values(player)
        print('Сумма очков', player['сумма'])
        if player['человек']:
            player_option = input('Взять картe? y/n: ')
        else:
            if player['сумма'] < 16:
                player_option = 'y'
            else:
                player_option = 'n' 

        if player_option == 'y':
            if len(player['карты']) < max_cards:
                player['карты'].append(deck.pop(-1))
            else:
                print('Невозможно взять еще карту')
                input('Нажмите ENTER чтобы продолжить')
                break
        else:
            input('Нажмите ENTER чтобы продолжить')
            break
    print('Партия окончена')

players_values = []
max_value = 0
winner = []

def show_stat():
    for player in players:
        if player['сумма'] < 22:
            print(f"{player['имя']} - {player['сумма']}")
        else:
            print(f"{player['имя']} - {player['сумма']} - перебор")

def show_result() -> None:
    total_value = []
    for player in players:
        total_value.append(player['сумма'])

    if all(num > 21 for num in total_value):
        print('Ничья')

    elif all(num == total_value[0] for num in total_value):
        print('Ничья')

    for player in players:
        if player['сумма'] == max(total_value):
            print('Победил', winner['имя'])
            break



    

  
       



