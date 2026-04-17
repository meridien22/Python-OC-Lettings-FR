import pytest
from lettings.models import Letting, Address

@pytest.mark.django_db
def test_address_model():
    address = Address.objects.create(street="Libreville", zip_code=1000, number=12)
    expected_value = "12 Libreville"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_model():
    address = Address.objects.create(street="Libreville", zip_code=1000, number=12)
    letting = Letting.objects.create(title="Beau Rivage", address=address)
    expected_value = "Beau Rivage"
    assert str(letting) == expected_value