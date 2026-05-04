import pytest
from lettings.models import Letting, Address
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse

# View tests


@pytest.mark.django_db
def test_letting_index_view():
    client = Client()
    address = Address.objects.create(street="Libreville", zip_code=1000, number=12)
    Letting.objects.create(title="Beau Rivage", address=address)
    path = reverse('lettings:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Beau Rivage"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_detail_view():
    client = Client()
    address = Address.objects.create(street="Libreville", zip_code=1000, number=12)
    letting = Letting.objects.create(title="Beau Rivage", address=address)
    path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()

    expected_content = "Beau Rivage"
    assert expected_content in content

    expected_content = "Libreville"
    assert expected_content in content

    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
