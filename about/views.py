from django.shortcuts import render
from .models import AboutContent

def about(request):
   myAbout = AboutContent.objects.all
   context = {
              'ab_cont':myAbout,
              'app_text':"About Us",
              'app_name':"About"
             }
   return render(request, 'about/about.html', context)
# Create your views here.
