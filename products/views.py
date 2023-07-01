from django.shortcuts import render
from .models import ProductContent
from .models import UsesContent
from .models import CertContent
from .models import ProductButton

def products(request):
   myProducts = ProductContent.objects.all()
   myCerts    = CertContent.objects.all()
   myUses=[];
   myButtons=[];
   for counter in range(myProducts.count()):
      myUses.append(UsesContent.objects.filter(related_product = myProducts[counter]))
      myButtons.append(ProductButton.objects.filter(related_product = myProducts[counter]))
      counter = counter + 1

   context = {
              'prod_cont':myProducts,
              'use_cont':myUses,
              'butt_cont':myButtons,
              'cert_cont':myCerts,
              'app_text':"Products",
              'app_name':"Products"
             }
   return render(request, 'products/products.html', context)
# Create your views here.
