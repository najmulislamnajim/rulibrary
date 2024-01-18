from django.shortcuts import render
from book.models import *

# Create your views here.
def search(request):
    if request.method=='POST':
        if request.method == "POST":
            query_name = request.POST.get('name', None)
            if query_name:
                results = BookModel.objects.filter(name__contains=query_name)
                return render(request, 'product-search.html', {"results":results})