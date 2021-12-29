from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from store.models import Product


def say_hello(request):
    # return HttpResponse()
    try:
        query_set = Product.objects.get(pk=1)
        for product in query_set:
            print(product)
    except:

    return render(request, 'hello.html', {'name': 'Hussein'})
