import pytest
import shirt_builders


@pytest.fixture
def base_shirt():
    return shirt_builders.Shirt()


@pytest.fixture
def coloured_shirt_builder():
    return shirt_builders.ColouredShirtBuilder('zieloną')


@pytest.fixture
def coloured_shirt_with_mark_builder():
    return shirt_builders.ColouredShirtWithMarkBuilder('zieloną', 'psem')


@pytest.fixture
def coloured_shirt_with_text_builder():
    return shirt_builders.ColouredShirtWithTextBuilder('zieloną', 'SSID')


@pytest.fixture
def coloured_shirt_with_mark_and_text_builder():
    return shirt_builders.ColouredShirtWithMarkAndTextBuilder('zieloną', 'psem', 'SSID')
