from django.shortcuts import render
from django.http import Http404


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis
# leo consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae
# erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    return render(request, 'index.html')

def error_404(request):
    raise Http404()

def error_500(request):
    resultat = 1 / 0
    return render(request, 'index.html')

def error_404_custom(request, exception):
    return render(request, '404.html', status=404)

def error_500_custom(request, *args, **kwargs):
    return render(request, '500.html', status=500)