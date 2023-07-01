from django.urls import path
from . import views

urlpatterns = [
   path('', views.certify, name='Certifications'),
]
