import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting, Address
from pytest_django.asserts import assertTemplateUsed
import html

@pytest.mark.django_db  
def test_letting_view():
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
