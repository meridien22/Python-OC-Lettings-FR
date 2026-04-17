from django.shortcuts import render
from django.http import Http404


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis
# leo consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae
# erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    View that allows you to display the site's homepage.


        Parameters:
            request: A Python object (an instance of the HttpRequest class) that contains
            all the information sent by the user's browser to the server.

        Returns:
            render: A Django function that, based on a template and a context, returns
            an HttpResponse object to the browser.
        """
    return render(request, 'index.html')

def error_404(request):
    raise Http404()

def error_500(request):
    resultat = 1 / 0
    return render(request, 'index.html')

def error_404_custom(request, exception):
    """
    A view that allows a custom page to be displayed when a 404 error
    is returned by the server.


        Parameters:
            request: A Python object (an instance of the HttpRequest class) that contains
            all the information sent by the user's browser to the server.

        Returns:
            render: A Django function that, based on a template and a context, returns
            an HttpResponse object to the browser.
    """
    return render(request, '404.html', status=404)

def error_500_custom(request, *args, **kwargs):
    """
    A view that allows a custom page to be displayed when a 500 error
    is returned by the server.


        Parameters:
            request: A Python object (an instance of the HttpRequest class) that contains
            all the information sent by the user's browser to the server.

        Returns:
            render: A Django function that, based on a template and a context, returns
            an HttpResponse object to the browser.
    """
    return render(request, '500.html', status=500)