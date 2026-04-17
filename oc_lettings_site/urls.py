from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from . import views

handler404 = 'oc_lettings_site.views.error_404_custom'
handler500 = 'oc_lettings_site.views.error_500_custom'

urlpatterns = [
    path('', views.index, name='index'),
    path('error_404', views.error_404, name='error_404'),
    path('error_500', views.error_500, name='error_500'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
