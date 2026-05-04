import pytest
from profiles.models import Profile
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

User = get_user_model()

# View tests


@pytest.mark.django_db
def test_profile_index_view():
    client = Client()
    user = User.objects.create_user(
        username="John",
        password="lechatmange9+"
    )
    Profile.objects.create(
        user=user,
        favorite_city="Franceville"
    )
    path = reverse('profiles:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "John"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_detail_view():
    client = Client()
    user = User.objects.create_user(
        username="John",
        password="lechatmange9+"
    )
    Profile.objects.create(
        user=user,
        favorite_city="Franceville"
    )
    path = reverse('profiles:profile', kwargs={'username': user.username})
    response = client.get(path)
    content = response.content.decode()

    expected_content = "John"
    assert expected_content in content

    expected_content = "Franceville"
    assert expected_content in content

    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
