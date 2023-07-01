from django.shortcuts import render
from .models import CarouselContent
from .models import HomeContent

def home(request):
   myCarousel  = CarouselContent.objects.all
   myHome = HomeContent.objects.all
   context = {
              'car_cont' :myCarousel,
              'mark_cont':myHome,
              'app_text':"Home",
              'app_name':"Home"
             }
   return render(request, 'home/home.html', context)


# Create your views here.
