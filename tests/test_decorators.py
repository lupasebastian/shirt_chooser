"""Class for testing decorators classes"""
from shirt_decorators import Shirt, ConcreteFeatureColor, ConcreteFeatureMark, ConcreteFeatureText


def test_can_create_shirt_instance(base_shirt_for_decorators: Shirt):
    """Tests if an instance of a case shirt to decorate can be created"""
    assert isinstance(base_shirt_for_decorators, Shirt)


def test_can_show_description(base_shirt_for_decorators: Shirt):
    """Tests if a description of a shirt can be obtained"""
    assert base_shirt_for_decorators.description == 'Zwykła biała koszulka'


def test_can_add_color(base_shirt_for_decorators):
    """Tests if a color can be added using decorator"""
    coloured_shirt = ConcreteFeatureColor(base_shirt_for_decorators, 'czarną')
    assert coloured_shirt.description == 'Wybrano czarną koszulkę.'


def test_can_add_and_mark(coloured_shirt_for_decorators):
    """Tests if a mark can be added using decorator"""
    coloured_shirt_with_mark = ConcreteFeatureMark(coloured_shirt_for_decorators, 'słońcem')
    assert coloured_shirt_with_mark.description == 'Wybrano czarną koszulkę z słońcem.'


def test_can_add_and_text(coloured_shirt_for_decorators):
    """Tests if a text can be added using decorator"""
    coloured_shirt_with_text = ConcreteFeatureText(coloured_shirt_for_decorators, 'YMCA')
    assert coloured_shirt_with_text.description == 'Wybrano czarną koszulkę z napisem YMCA.'


def test_can_add_mark_and_text(coloured_shirt_for_decorators):
    """Tests if a mark and a text can be added using decorator"""
    with_mark = ConcreteFeatureMark(coloured_shirt_for_decorators, 'słońcem')
    with_mark_and_text = ConcreteFeatureText(with_mark, 'YMCA')
    assert with_mark_and_text.description == 'Wybrano czarną koszulkę z słońcem i napisem YMCA.'


def test_can_check_if_has_mark(coloured_shirt_for_decorators):
    """Tests if a has_mark property can be obtained"""
    assert not coloured_shirt_for_decorators.has_mark


def test_can_check_if_has_text(coloured_shirt_for_decorators):
    """Tests if a has_text property can be obtained"""
    with_text = ConcreteFeatureText(coloured_shirt_for_decorators, 'some_text')
    assert with_text.has_text
