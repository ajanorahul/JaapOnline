from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,SubCategory,Category
from .models import FeatureProduct
from math import ceil

# Create your views here.
def index(request):
    # prods = Product.objects.all()
    # print(prods)
    # subs  = SubCategory.objects.all()
    # n = len(prods)
    # nSlides = n//4 +ceil((n/4)-(n//4))
    #smiple way
    # context ={
    # 'no_of_slides':nSlides,
    # 'range':range(nSlides),
    # 'prods':prods,
    # }
    #meidum way
    # listprods = [[prods,range(1,len(prods)),nSlides],
    # [prods,range(1,len(prods)),nSlides]]
    feature = FeatureProduct.objects.all()
    listprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 +ceil((n/4)-(n//4))
        listprods.append([prod,range(1,nSlides),nSlides])







    context ={
    'listprods':listprods,
    'feature':feature,

    }
    return render(request, 'index.html',context)

def indextwo(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    context = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'indextwo.html',context)
