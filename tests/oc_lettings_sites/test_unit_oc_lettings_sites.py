import pytest
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

User = get_user_model()

# URL tests


@pytest.mark.django_db
def test_index_url():
    path = reverse('index')
    assert path == "/"
    assert resolve(path).view_name == "index"


@pytest.mark.django_db
def test_admin_url():
    path = reverse('admin:index')
    assert path == "/admin/"


@pytest.mark.django_db
def test_error_404_url():
    path = reverse('error_404')
    assert path == "/error_404/"
    assert resolve(path).view_name == "error_404"


@pytest.mark.django_db
def test_error_500_url():
    path = reverse('error_500')
    assert path == "/error_500/"
    assert resolve(path).view_name == "error_500"

# View tests


@pytest.mark.django_db
def test_index_view():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Welcome to Holiday Homes"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


@pytest.mark.django_db
def test_error_404_custom_view():
    client = Client()
    path = reverse('profiles:profile', kwargs={'username': 'John'})
    response = client.get(path)
    content = response.content.decode()

    expected_content = "404"
    assert expected_content in content

    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


def test_error_505_custom_view():
    client = Client()
    url = reverse('error_500')
    with pytest.raises(ZeroDivisionError):
        response = client.get(url, raise_request_exception=False)
        assert response.status_code == 500
        assertTemplateUsed(response, "500.html")
