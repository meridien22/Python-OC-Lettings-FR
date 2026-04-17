import pytest
from django.urls import reverse, resolve
from lettings.models import Letting, Address
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db    
def test_letting_infos_url():
    address = Address.objects.create(street="Libreville", zip_code=1000, number=12)
    letting = Letting.objects.create(title="Beau Rivage", address=address)
    path = reverse('lettings:letting', kwargs={'letting_id':address.id})
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"
