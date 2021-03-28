from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Query

from math import ceil
# Create your views here.


def index(request):
    #p = Product.objects.all()
    #N = len(p)
    #n = N//4 + ceil(N/4 - N//4)    # number of slides required
    #allp = [[p,range(1,n),n], [p,range(1,n),n]]
    #params={'allp':allp}
    #params = {'products':p, 'range':range(1,n), 'nSlides':n}

    allp=[]
    x = Product.objects.values('category', 'id')
    cats = {item['category'] for item in x}
    for cat in cats:
        p = Product.objects.filter(category=cat)
        N=len(p)
        n = N // 4 + ceil(N / 4 - N // 4)  # number of slides required
        allp.append([p, range(1,n), n])
    params = {'allp': allp}
    return render(request, 'shop/index3.html', params)    # index3.html is the file made by me solely
    # return HttpResponse("Index Shop")


def about(request):
    # return HttpResponse("About Us")
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name','')    # 'name' in get method is the name of the form element with name='name'
        email = request.POST.get('email','')   # 'email' in get method is the name of the form element with name='email'
        phone = request.POST.get('phone','')
        query = request.POST.get('query','')
        print(name,email,phone,query)
        q = Query(name=name, email=email, phone=phone, query=query)
        q.save()
    return render(request, 'shop/contact.html')


def track(request):
    return render(request, 'shop/track.html')


def search(request):
    return render(request, 'shop/search.html')


def prodView(request,myid):
    p=Product.objects.filter(id=myid)
    #print(p)
    return render(request, 'shop/prodView.html',{'prod':p[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')

