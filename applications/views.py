from django.shortcuts import render
from .models import ApplContent

def applications(request):
   myAppl = ApplContent.objects.all
   context = {
              'appl_cont':myAppl,
              'app_text':"Applications",
              'app_name':"Applications"
             }
   return render(request, 'applications/applications.html', context)
# Create your views here.
