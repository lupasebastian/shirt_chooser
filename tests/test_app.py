"""
Module for testing the application's main file
"""
from random import choice
from unittest.mock import MagicMock
from main import MONDAY_CHOICES, POLISH_DAYS, get_random_color, \
    __get_random_mark, __get_random_text, WEDNESDAY_CHOICES


def test_can_generate_choices():
    """Tests if choices can be generated from lists of data"""
    color = choice(MONDAY_CHOICES[0])
    mark = choice(MONDAY_CHOICES[1])
    text = choice(MONDAY_CHOICES[2])
    assert color is not None and mark is not None and text is not None


def test_can_get_day():
    """Tests if app can get day from user using MagicMock"""
    __get_day = MagicMock(return_value='wtorek')
    assert __get_day() in POLISH_DAYS


def test_can_get_mark():
    """Tests if app can get mark decision from user using MagicMock"""
    __get_mark = MagicMock(return_value=False)
    assert __get_mark() is False


def test_can_get_text():
    """Tests if app can get text decision from user using MagicMock"""
    __get_text = MagicMock(return_value=True)
    assert __get_text() is True


def test_can_generate_random_color():
    """Tests if app can get a random color choice from appropriate list"""
    day = 'środa'
    assert get_random_color(day) in WEDNESDAY_CHOICES[0]


def test_can_generate_random_mark():
    """Tests if app can get a random mark choice from appropriate list"""
    day = 'środa'
    assert __get_random_mark(day) in WEDNESDAY_CHOICES[1]


def test_can_generate_random_text():
    """Tests if app can get a random text choice from appropriate list"""
    day = 'środa'
    assert __get_random_text(day) in WEDNESDAY_CHOICES[2]


def test_can_get_final_input():
    """Tests if an app can get final result with three values from user"""
    __get_final_input = MagicMock(return_value=('zieloną', 'słońcem', None))
    result = __get_final_input()
    assert result[0] in MONDAY_CHOICES[0]
    assert result[1] in MONDAY_CHOICES[1]
    assert result[2] is None
