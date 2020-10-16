"""
Application designed to help undecided people choose what kind of shirt they can
wear.
If they don't have those kind of shirts they can always draw marks and texts :-)
Next releases will implement defining user's own wardrobe to choose from.
"""
from random import choice, randint
from shirt_builders import ColouredShirtWithMarkAndTextBuilder, \
    ColouredShirtWithTextBuilder, ColouredShirtBuilder, \
    ColouredShirtWithMarkBuilder
from shirt_decorators import Shirt, ConcreteFeatureColor, ConcreteFeatureMark, ConcreteFeatureText

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
    final_color = get_random_color(day)
    final_mark = __get_random_mark(day) if final_mark else None
    final_text = __get_random_text(day) if final_text else None
    return final_color, final_mark, final_text


def __get_day() -> str:
    """Gets the day of the week from a user."""
    while True:
        day = input('Jaki jest dzień tygodnia? ').casefold()
        if day in POLISH_DAYS:
            return day
        print('Nieprawidłowy wybór')


def __get_mark() -> bool:
    """Gets user's decision whether they want a mark on a shirt"""
    while True:
        mark = input('Czy chcesz koszulkę z nadrukiem? \n'
                     'Wpisz Tak lub Nie: ').casefold()
        if mark in ('tak', 'nie'):
            return mark == 'tak'
        print('Nieprawidłowy wybór')


def __get_text() -> bool:
    """Gets user's decision whether they want a text on their shirt"""
    while True:
        text = input('Czy chcesz koszulkę z napisem? \n'
                     'Wpisz Tak lub Nie: ').casefold()
        if text in ('tak', 'nie'):
            return text == 'tak'
        print('Nieprawidłowy wybór')


def get_random_color(day: str) -> str:
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


def prompt_for_exit():
    """Asks user if they want to quit program"""
    choice_exit = input('Jeśli chcesz zakończyć wybierz 0, '
                        'jeśli chcesz wybrać jeszcze raz - '
                        'wciśnij dowolny inny przycisk i '
                        'zatwierdź wciskając ENTER: ')
    return choice_exit == '0'


def print_greeting():
    """Greets user in application"""
    print('Witaj, na podstawie podanego dnia tygodnia '
          'wybierzemy dla Ciebie koszulkę: ')


if __name__ == '__main__':
    print_greeting()
    final_color_main, final_mark_main, final_text_main = __get_final_input()
    pattern_random_selection = randint(1, 2)
    if pattern_random_selection == 1:
        print('Używamy wzorca Builder :-)')
        while True:
            if final_color_main and final_mark_main and final_text_main:
                builder = ColouredShirtWithMarkAndTextBuilder(final_color_main,
                                                              final_mark_main,
                                                              final_text_main)
                builder.add_elements()
                print(builder.result.description)
            elif final_color_main and final_mark_main:
                builder = ColouredShirtWithMarkBuilder(final_color_main,
                                                       final_mark_main)
                builder.add_elements()
                print(builder.result.description)
            elif final_color_main and final_text_main:
                builder = ColouredShirtWithTextBuilder(final_color_main,
                                                       final_text_main)
                builder.add_elements()
                print(builder.result.description)
            else:
                builder = ColouredShirtBuilder(final_color_main)
                builder.add_elements()
                print(builder.result.description)
            if prompt_for_exit():
                break
            else:
                print_greeting()
                final_color_main, final_mark_main, final_text_main = __get_final_input()

    else:
        print('Używamy wzorca Decorator :-)')
        while True:
            final_shirt = Shirt()
            coloured_shirt = ConcreteFeatureColor(final_shirt, final_color_main)
            if not final_mark_main and not final_text_main:
                print(coloured_shirt.description)
            elif not final_mark_main and final_text_main:
                final_shirt_with_text = \
                    ConcreteFeatureText(coloured_shirt, final_text_main)
                print(final_shirt_with_text.description)
            elif final_mark_main:
                final_shirt_with_mark = \
                    ConcreteFeatureMark(coloured_shirt, final_mark_main)
                if final_text_main:
                    final_shirt_with_mark_and_text = \
                        ConcreteFeatureText(final_shirt_with_mark,
                                            final_text_main)
                    print(final_shirt_with_mark_and_text.description)
                else:
                    print(final_shirt_with_mark.description)
            if prompt_for_exit():
                break
            else:
                print_greeting()
                final_color_main, final_mark_main, final_text_main = __get_final_input()
