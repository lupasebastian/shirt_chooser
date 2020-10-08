"""File for creating fixtures to be used in tests"""
import pytest
import shirt_builders


@pytest.fixture
def base_shirt():
    """Creates an instance of a shirt"""
    return shirt_builders.Shirt()


@pytest.fixture
def coloured_shirt_builder():
    """Creates an instance of a coloured shirt"""
    return shirt_builders.ColouredShirtBuilder('zieloną')


@pytest.fixture
def coloured_shirt_with_mark_builder():
    """Creates an instance of a coloured shirt with a mark"""
    return shirt_builders.ColouredShirtWithMarkBuilder('zieloną', 'psem')


@pytest.fixture
def coloured_shirt_with_text_builder():
    """Creates an instance of a coloured shirt with a text"""
    return shirt_builders.ColouredShirtWithTextBuilder('zieloną', 'SSID')


@pytest.fixture
def coloured_shirt_with_mark_and_text_builder():
    """Creates an instance of a coloured shirt with a mark and a text"""
    return shirt_builders.ColouredShirtWithMarkAndTextBuilder('zieloną', 'psem', 'SSID')
