import pytest
from lettings.models import Letting, Address
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

User = get_user_model()

# model tests


@pytest.mark.django_db
def test_address_model():
    address = Address.objects.create(
        street="Libreville",
        zip_code=1000,
        number=12
    )
    expected_value = "12 Libreville"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_model():
    address = Address.objects.create(
        street="Libreville",
        zip_code=1000,
        number=12
    )
    letting = Letting.objects.create(
        title="Beau Rivage",
        address=address
    )
    expected_value = "Beau Rivage"
    assert str(letting) == expected_value

# URL tests


@pytest.mark.django_db
def test_letting_index_url():
    path = reverse('lettings:index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db
def test_letting_infos_url():
    address = Address.objects.create(street="Libreville", zip_code=1000, number=12)
    letting = Letting.objects.create(title="Beau Rivage", address=address)
    path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"
