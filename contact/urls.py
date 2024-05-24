#from django.urls import path, include
#from .views import contact_form, contact


#urlpatterns = [
#    path('contact_form', contact_form, name='contact_form'),
#    path('contact/', contact, name='contact'),
#]

from django.urls import path
from .views import contact, contact_form

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('contact_form', contact_form, name='contact_form'),  # Updated URL pattern
]

