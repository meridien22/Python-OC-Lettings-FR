import pytest
from profiles.models import Profile
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

User = get_user_model()

# model_tests


@pytest.mark.django_db
def test_profile_model():
    user = User.objects.create_user(
        username="John",
        password="lechatmange9+"
    )
    expected_value = "John"
    assert str(user) == expected_value
    profile = Profile.objects.create(
        user=user,
        favorite_city="Franceville"
    )
    assert str(profile) == expected_value

# URL tests


@pytest.mark.django_db
def test_profile_index_url():
    path = reverse('profiles:index')
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile_infos_url():
    user = User.objects.create_user(
        username="John",
        password="lechatmange9+"
    )
    Profile.objects.create(
        user=user,
        favorite_city="Franceville"
    )
    path = reverse('profiles:profile', kwargs={'username': user.username})
    assert path == "/profiles/John/"
    assert resolve(path).view_name == "profiles:profile"
