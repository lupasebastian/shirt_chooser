from shirt_builders import *
import pytest


def test_can_instantiate_shirt(base_shirt):
    assert type(base_shirt) is Shirt


def test_can_get_shirts_description(base_shirt):
    assert base_shirt.description == 'Zwykła biała koszulka'


def test_can_change_description_by_building(base_shirt, coloured_shirt_builder,
                                            coloured_shirt_with_mark_builder,
                                            coloured_shirt_with_text_builder,
                                            coloured_shirt_with_mark_and_text_builder):
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
