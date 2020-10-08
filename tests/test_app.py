from random import choice
from unittest.mock import MagicMock
from main import MONDAY_CHOICES, POLISH_DAYS, __get_random_color,\
    __get_random_mark, __get_random_text


def test_can_generate_choices():
    color = choice(MONDAY_CHOICES[0])
    mark = choice(MONDAY_CHOICES[1])
    text = choice(MONDAY_CHOICES[2])
    assert color is not None and mark is not None and text is not None


def test_can_get_day():
    __get_day = MagicMock(return_value='wtorek')
    assert __get_day() in POLISH_DAYS


def test_can_get_mark():
    __get_mark = MagicMock(return_value=False)
    assert __get_mark() is False


def test_can_get_text():
    __get_text = MagicMock(return_value=True)
    assert __get_text() is True


def test_can_generate_random_color():
    day = 'środa'
    assert __get_random_color(day) is not None


def test_can_generate_random_mark():
    day = 'środa'
    assert __get_random_mark(day) is not None


def test_can_generate_random_text():
    day = 'środa'
    assert __get_random_text(day) is not None


def test_can_get_final_input():
    __get_final_input = MagicMock(return_value=('zieloną', 'słońcem', None))
    result = __get_final_input()
    assert result[0] in MONDAY_CHOICES[0]
    assert result[1] in MONDAY_CHOICES[1]
    assert result[2] is None

