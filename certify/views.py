from django.shortcuts import render
from .models import CertifyContent
from .models import CertifyHeader
# Create your views here.
def certify(request):
   myCert = CertifyContent.objects.all()
   myHeader = CertifyHeader.objects.all()
   context = {
              'cert_head':myHeader,
              'cert_cont':myCert,
              'app_text':"Certifications",
              'app_name':"Certify"
             }
   return render(request, 'certify/certify.html', context)


