"""
Classes of product and builders to be used by app
"""
# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod


class Shirt:
    """Class for creating instances of product (shirt)"""
    def __init__(self):
        self._description = 'Zwykła biała koszulka'

    @property
    def description(self):
        """Property description of object shirt"""
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description


class ShirtBuilder(ABC):
    """Abstract class for builders with methods to implement"""
    @abstractmethod
    def reset(self):
        """Abstract method"""

    @abstractmethod
    def add_elements(self):
        """Abstract method"""


class ColouredShirtBuilder(ShirtBuilder):
    """Class for creating coloured shirts builders"""
    def __init__(self, color: str):
        self._color = color
        self._result = Shirt()

    def reset(self):
        self._result = Shirt()

    def add_elements(self):
        self._result.description = f'Wybrano {self._color} koszulkę.'

    @property
    def result(self):
        """Property result of coloured shirts builders"""
        return self._result


class ColouredShirtWithMarkBuilder(ShirtBuilder):
    """Class for creating coloured shirts with mark builders"""
    def __init__(self, color: str, mark: str):
        self._result = Shirt()
        self._color = color
        self._mark = mark

    def reset(self):
        self._result = Shirt()

    def add_elements(self):
        self._result.description = f'Wybrano {self._color} ' \
                                   f'koszulkę z {self._mark}.'

    @property
    def result(self):
        """Property result of coloured shirts with mark builders"""
        return self._result


class ColouredShirtWithTextBuilder(ShirtBuilder):
    """Class for creating coloured shirts with text builders"""
    def __init__(self, color: str, text: str):
        self._result = Shirt()
        self._color = color
        self._text = text

    def reset(self):
        self._result = Shirt()

    def add_elements(self):
        self._result.description = f'Wybrano {self._color} ' \
                                   f'koszulkę z napisem {self._text}.'

    @property
    def result(self):
        """Property result of coloured shirts with text builders"""
        return self._result


class ColouredShirtWithMarkAndTextBuilder(ShirtBuilder):
    """Class for creating coloured shirts with mark and text builders"""
    def __init__(self, color: str, mark: str, text: str):
        self._result = Shirt()
        self._color = color
        self._mark = mark
        self._text = text

    def reset(self):
        self._result = Shirt()

    def add_elements(self):
        self._result.description = f'Wybrano {self._color} ' \
                                   f'koszulkę z {self._mark} ' \
                                   f'i napisem {self._text}.'

    @property
    def result(self):
        """Property result of coloured shirts with mark and text builders"""
        return self._result


class Director:
    """
    Class for managing builders, but it's not necessary.
    Builders can be called directly by the client.
    """
    def __init__(self, builder: ShirtBuilder):
        self._builder = builder

    def change_builder(self, builder: ShirtBuilder):
        """Resets product to a default state"""
        self._builder = builder

    def make(self):
        """Resets product to a default state then adds changes appropriate for
        a particular builder"""
        self._builder.reset()
        self._builder.add_elements()
