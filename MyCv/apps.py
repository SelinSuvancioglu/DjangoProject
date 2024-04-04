from django.apps import AppConfig
from django.contrib import admin
from django.urls import path
from .views import index  # index view'ini ekledik

class MycvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyCv'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Boş bir URL, index view'ına yönlendiriliyor
]
