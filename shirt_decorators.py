"""Module for creating product object and adding features"""
from abc import ABC, abstractmethod


class Component(ABC):
    """Abstract class for features"""
    @property
    @abstractmethod
    def description(self):
        """Abstract class for obtaining description"""

    @property
    @abstractmethod
    def has_mark(self):
        """Flag to check if an object already has a mark"""

    @property
    @abstractmethod
    def has_text(self):
        """Flag to check if an object already has a text"""


class Shirt(Component):
    """Base product to which features are added"""
    @property
    def description(self):
        return 'Zwykła biała koszulka'

    @property
    def has_mark(self):
        return False

    @property
    def has_text(self):
        return False


class Feature(Component, ABC):
    """Abstract feature class"""
    def __init__(self, component: Component):
        self._wrapee = component


class ConcreteFeatureColor(Feature):
    """Class for objects adding color to the shirts"""
    def __init__(self, component: Component, color: str):
        super().__init__(component)
        self._color = color

    @property
    def description(self):
        return f'Wybrano {self._color} koszulkę.'

    @property
    def has_mark(self):
        return False

    @property
    def has_text(self):
        return False


class ConcreteFeatureMark(Feature):
    """Class for objects adding mark to the shirt"""
    def __init__(self, component: Component, mark: str):
        super().__init__(component)
        self._mark = mark

    @property
    def description(self):
        return self._wrapee.description[:-1] + f' z {self._mark}.'

    @property
    def has_mark(self):
        return True

    @property
    def has_text(self):
        return False


class ConcreteFeatureText(Feature):
    """Class for objects adding text to the shirt"""
    def __init__(self, component: Component, text: str):
        super().__init__(component)
        self._text = text

    @property
    def description(self):
        return self._wrapee.description[:-1] + f' i napisem {self._text}.' if \
            self._wrapee.has_mark else \
            self._wrapee.description[:-1] + f' z napisem {self._text}.'

    @property
    def has_text(self):
        return True

    @property
    def has_mark(self):
        return self._wrapee.has_mark
