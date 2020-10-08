from random import choice
from shirt_builders import *

MONDAY_CHOICES = [['zieloną', 'niebieską', 'żółtą'],
                  ['słońcem', 'koniem', 'psem'],
                  ['NY 1934', 'LA 56', 'KOCHAM PSY']]
TUESDAY_CHOICES = [['białą', 'czarną', 'czerwoną'],
                   ['kotem', 'budzikiem', 'rośliną'],
                   ['BULLSEYE', 'CHEROKEE', 'STREET']]
WEDNESDAY_CHOICES = [['czerwoną', 'brązową', 'liliową'],
                     ['baranem', 'wielbłądem', 'parówką'],
                     ['01-93', 'SWAG', 'THIS']]
THURSDAY_CHOICES = [['granatową', 'błękitną', 'oliwkową'],
                    ['folią', 'guzem', 'gołębiem'],
                    ['THREE', 'FORTY-TWO', 'ALL DOGS GO TO HEAVEN']]
FRIDAY_CHOICES = [['bordową', 'fioletową', 'brunatną'],
                  ['orzechem', 'budynkiem', 'procesorem'],
                  ['OUCH', 'HAVE MERCY', 'TRAINSPOTTING']]
SATURDAY_CHOICES = [['szkarłatną', 'morską', 'pomarańczową'],
                    ['falangą', 'morzem', 'słownikiem'],
                    ['SSID', 'HERE GOES', 'DOORS OPEN']]
SUNDAY_CHOICES = [['malinową', 'ciemnozieloną', 'beżową'],
                  ['klawiaturą', 'kapslem', 'rurą'],
                  ['SUMMER OF \'69', 'PNEUMA', 'DARK TOWER']]
POLISH_DAYS = ('poniedziałek', 'wtorek', 'środa',
               'czwartek', 'piątek', 'sobota', 'niedziela')


def __get_final_input():
    day = __get_day()
    mark = __get_mark()
    text = __get_text()
    color = __get_random_color(day)
    mark = __get_random_mark(day) if mark else None
    text = __get_random_text(day) if text else None
    return color, mark, text


def __get_day() -> str:
    while True:
        day = input('Jaki jest dzień tygodnia? ').casefold()
        if day in POLISH_DAYS:
            return day
        else:
            print('Nieprawidłowy wybór')


def __get_mark() -> bool:
    while True:
        mark = input('Czy chcesz koszulkę z nadrukiem? \n'
                     'Wpisz Tak lub Nie: ').casefold()
        if mark in ('tak', 'nie'):
            return True if mark == 'tak' else False
        else:
            print('Nieprawidłowy wybór')


def __get_text() -> bool:
    while True:
        text = input('Czy chcesz koszulkę z napisem? \n'
                     'Wpisz Tak lub Nie: ').casefold()
        if text in ('tak', 'nie'):
            return True if text == 'tak' else False
        else:
            print('Nieprawidłowy wybór')


def __get_random_color(day: str) -> str:
    if day == 'monday':
        return choice(MONDAY_CHOICES[0])
    elif day == 'tuesday':
        return choice(TUESDAY_CHOICES[0])
    elif day == 'wednesday':
        return choice(WEDNESDAY_CHOICES[0])
    elif day == 'thursday':
        return choice(THURSDAY_CHOICES[0])
    elif day == 'friday':
        return choice(FRIDAY_CHOICES[0])
    elif day == 'saturday':
        return choice(SATURDAY_CHOICES[0])
    else:
        return choice(SUNDAY_CHOICES[0])


def __get_random_mark(day: str) -> str:
    if day == 'monday':
        return choice(MONDAY_CHOICES[1])
    elif day == 'tuesday':
        return choice(TUESDAY_CHOICES[1])
    elif day == 'wednesday':
        return choice(WEDNESDAY_CHOICES[1])
    elif day == 'thursday':
        return choice(THURSDAY_CHOICES[1])
    elif day == 'friday':
        return choice(FRIDAY_CHOICES[1])
    elif day == 'saturday':
        return choice(SATURDAY_CHOICES[1])
    else:
        return choice(SUNDAY_CHOICES[1])


def __get_random_text(day: str) -> str:
    if day == 'monday':
        return choice(MONDAY_CHOICES[2])
    elif day == 'tuesday':
        return choice(TUESDAY_CHOICES[2])
    elif day == 'wednesday':
        return choice(WEDNESDAY_CHOICES[2])
    elif day == 'thursday':
        return choice(THURSDAY_CHOICES[2])
    elif day == 'friday':
        return choice(FRIDAY_CHOICES[2])
    elif day == 'saturday':
        return choice(SATURDAY_CHOICES[2])
    else:
        return choice(SUNDAY_CHOICES[2])


if __name__ == '__main__':
    while True:
        print('Witaj, na podstawie podanego dnia tygodnia '
              'wybierzemy dla Ciebie koszulkę: ')
        color, mark, text = __get_final_input()
        if color and mark and text:
            builder = ColouredShirtWithMarkAndTextBuilder(color, mark, text)
            builder.add_elements()
            print(builder.result.description)
        elif color and mark:
            builder = ColouredShirtWithMarkBuilder(color, mark)
            builder.add_elements()
            print(builder.result.description)
        elif color and text:
            builder = ColouredShirtWithTextBuilder(color, text)
            builder.add_elements()
            print(builder.result.description)
        else:
            builder = ColouredShirtBuilder(color)
            builder.add_elements()
            print(builder.result.description)
        choice = input('Jeśli chcesz zakończyć wybierz 0, '
              'jeśli chcesz wybrać jeszcze raz - '
              'wciśnij dowolny inny przycisk i zatwierdź wciskając ENTER: ')
        if choice == '0':
            break