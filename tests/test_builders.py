"""
Tests for builders classes
"""
from shirt_builders import Shirt


def test_can_instantiate_shirt(base_shirt):
    """Tests if a product can be instantiated"""
    assert isinstance(base_shirt, Shirt)


def test_can_get_shirts_description(base_shirt):
    """Tests if description property of a product can be accessed"""
    assert base_shirt.description == 'Zwykła biała koszulka'


def test_can_change_description_by_building(coloured_shirt_builder,
                                            coloured_shirt_with_mark_builder,
                                            coloured_shirt_with_text_builder,
                                            coloured_shirt_with_mark_and_text_builder):
    """Tests if description property can be changed by builders and then accessed"""
    coloured_shirt_builder.add_elements()
    coloured_shirt_with_mark_builder.add_elements()
    coloured_shirt_with_text_builder.add_elements()
    coloured_shirt_with_mark_and_text_builder.add_elements()
    assert coloured_shirt_builder.result.description == \
           'Wybrano zieloną koszulkę.'
    assert coloured_shirt_with_mark_builder.result.description == \
           'Wybrano zieloną koszulkę z psem.'
    assert coloured_shirt_with_text_builder.result.description == \
           'Wybrano zieloną koszulkę z napisem SSID.'
    assert coloured_shirt_with_mark_and_text_builder.result.description == \
           'Wybrano zieloną koszulkę z psem i napisem SSID.'
