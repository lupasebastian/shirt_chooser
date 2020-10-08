from abc import ABC, abstractmethod


class Shirt:
    def __init__(self):
        self._description = 'Zwykła biała koszulka'

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description


class ShirtBuilder(ABC):
    @abstractmethod
    def reset(self):
        """

        :return:
        """

    @abstractmethod
    def add_elements(self):
        """

        :return:
        """


class ColouredShirtBuilder(ShirtBuilder):
    def __init__(self, color: str):
        self._color = color
        self._result = Shirt()

    def reset(self):
        self._result = Shirt()

    def add_elements(self):
        self._result.description = f'Wybrano {self._color} koszulkę.'

    @property
    def result(self):
        return self._result


class ColouredShirtWithMarkBuilder(ShirtBuilder):
    def __init__(self, color: str, mark: str):
        self._result = Shirt()
        self._color = color
        self._mark = mark

    def reset(self):
        self._result = Shirt()

    def add_elements(self):
        self._result.description = f'Wybrano {self._color} koszulkę z {self._mark}.'

    @property
    def result(self):
        return self._result


class ColouredShirtWithTextBuilder(ShirtBuilder):
    def __init__(self, color: str, text: str):
        self._result = Shirt()
        self._color = color
        self._text = text

    def reset(self):
        self._result = Shirt()

    def add_elements(self):
        self._result.description = f'Wybrano {self._color} koszulkę z napisem {self._text}.'

    @property
    def result(self):
        return self._result


class ColouredShirtWithMarkAndTextBuilder(ShirtBuilder):
    def __init__(self, color: str, mark: str, text: str):
        self._result = Shirt()
        self._color = color
        self._mark = mark
        self._text = text

    def reset(self):
        self._result = Shirt()

    def add_elements(self):
        self._result.description = f'Wybrano {self._color} koszulkę z {self._mark} i napisem {self._text}.'

    @property
    def result(self):
        return self._result


class Director:
    """
    class for managing builders, but not necessary
    builders can be called directly by the client
    """
    def __init__(self, builder: ShirtBuilder):
        self._builder = builder

    def change_builder(self, builder: ShirtBuilder):
        self._builder = builder

    def make(self):
        self._builder.reset()
        self._builder.add_elements()
