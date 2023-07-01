from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
   path('', views.contact, name='Contact Us'),
   path('mail', views.mail, name='mail'),
]
