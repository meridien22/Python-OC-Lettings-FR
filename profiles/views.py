from django.shortcuts import render
from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis
# dictum lacus d
def index(request):
    """
    View that allows you to display the home page of user profiles.


        Parameters:
            request: A Python object (an instance of the HttpRequest class) that contains
            all the information sent by the user's browser to the server.

        Returns:
            render: A Django function that, based on a template and a context, returns
            an HttpResponse object to the browser.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis
# fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    View that allows you to display a user's profile page.


        Parameters:
            request: A Python object (an instance of the HttpRequest class) that contains
            all the information sent by the user's browser to the server.
            username (string): User name.

        Returns:
            render: A Django function that, based on a template and a context, returns
            an HttpResponse object to the browser.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
