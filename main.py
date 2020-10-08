"""
Application designed to help undecided people choose what kind of shirt they can
wear.
If they don't have those kid of shirts they can always draw marks and texts :-)
Next releases will implement defining user's own wardrobe to choose from.
"""
from random import choice
from shirt_builders import ColouredShirtWithMarkAndTextBuilder, \
    ColouredShirtWithTextBuilder, ColouredShirtBuilder, \
    ColouredShirtWithMarkBuilder

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
    """
    Gets input from a user using other methods
    then formats it so appropriate builders can use it.
    """
    day = __get_day()
    final_mark = __get_mark()
    final_text = __get_text()
    final_color = __get_random_color(day)
    final_mark = __get_random_mark(day) if final_mark else None
    final_text = __get_random_text(day) if final_text else None
    return final_color, final_mark, final_text


def __get_day() -> str:
    """Gets the day of the week from a user."""
    while True:
        day = input('Jaki jest dzień tygodnia? ').casefold()
        if day in POLISH_DAYS:
            return day
        else:
            print('Nieprawidłowy wybór')


def __get_mark() -> bool:
    """Gets user's decision whether they want a mark on a shirt"""
    while True:
        mark = input('Czy chcesz koszulkę z nadrukiem? \n'
                     'Wpisz Tak lub Nie: ').casefold()
        if mark in ('tak', 'nie'):
            return True if mark == 'tak' else False
        else:
            print('Nieprawidłowy wybór')


def __get_text() -> bool:
    """Gets user's decision whether they want a text on their shirt"""
    while True:
        text = input('Czy chcesz koszulkę z napisem? \n'
                     'Wpisz Tak lub Nie: ').casefold()
        if text in ('tak', 'nie'):
            return True if text == 'tak' else False
        else:
            print('Nieprawidłowy wybór')


def __get_random_color(day: str) -> str:
    """Basing on a day chooses shirt's color from available ones"""
    if day == 'poniedziałek':
        result = choice(MONDAY_CHOICES[0])
    elif day == 'wtorek':
        result = choice(TUESDAY_CHOICES[0])
    elif day == 'środa':
        result = choice(WEDNESDAY_CHOICES[0])
    elif day == 'czwartek':
        result = choice(THURSDAY_CHOICES[0])
    elif day == 'piątek':
        result = choice(FRIDAY_CHOICES[0])
    elif day == 'sobota':
        result = choice(SATURDAY_CHOICES[0])
    else:
        result = choice(SUNDAY_CHOICES[0])
    return result


def __get_random_mark(day: str) -> str:
    """Basing on a day chooses mark from available ones"""
    if day == 'poniedziałek':
        result = choice(MONDAY_CHOICES[1])
    elif day == 'wtorek':
        result = choice(TUESDAY_CHOICES[1])
    elif day == 'środa':
        result = choice(WEDNESDAY_CHOICES[1])
    elif day == 'czwartek':
        result = choice(THURSDAY_CHOICES[1])
    elif day == 'piątek':
        result = choice(FRIDAY_CHOICES[1])
    elif day == 'sobota':
        result = choice(SATURDAY_CHOICES[1])
    else:
        result = choice(SUNDAY_CHOICES[1])
    return result


def __get_random_text(day: str) -> str:
    """Basing on a day chooses text from available ones"""
    if day == 'poniedziałek':
        result = choice(MONDAY_CHOICES[2])
    elif day == 'wtorek':
        result = choice(TUESDAY_CHOICES[2])
    elif day == 'środa':
        result = choice(WEDNESDAY_CHOICES[2])
    elif day == 'czwartek':
        result = choice(THURSDAY_CHOICES[2])
    elif day == 'piatek':
        result = choice(FRIDAY_CHOICES[2])
    elif day == 'sobota':
        result = choice(SATURDAY_CHOICES[2])
    else:
        result = choice(SUNDAY_CHOICES[2])
    return result


if __name__ == '__main__':
    while True:
        print('Witaj, na podstawie podanego dnia tygodnia '
              'wybierzemy dla Ciebie koszulkę: ')
        builder_color, builder_mark, builder_text = __get_final_input()
        if builder_color and builder_mark and builder_text:
            builder = ColouredShirtWithMarkAndTextBuilder(builder_color, builder_mark, builder_text)
            builder.add_elements()
            print(builder.result.description)
        elif builder_color and builder_mark:
            builder = ColouredShirtWithMarkBuilder(builder_color, builder_mark)
            builder.add_elements()
            print(builder.result.description)
        elif builder_color and builder_text:
            builder = ColouredShirtWithTextBuilder(builder_color, builder_text)
            builder.add_elements()
            print(builder.result.description)
        else:
            builder = ColouredShirtBuilder(builder_color)
            builder.add_elements()
            print(builder.result.description)
        choice = input('Jeśli chcesz zakończyć wybierz 0, '
              'jeśli chcesz wybrać jeszcze raz - '
              'wciśnij dowolny inny przycisk i zatwierdź wciskając ENTER: ')
        if choice == '0':
            break
