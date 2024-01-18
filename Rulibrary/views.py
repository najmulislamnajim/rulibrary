from django.shortcuts import render
from book.models import GenreModel,BookModel

def home(request):
    genres=GenreModel.objects.all()
    if request.method=='POST':
        search_field=request.POST.get('search_field')
        print('vai vai',search_field is None)
        results=BookModel.objects.filter(title__icontains=search_field)
        if results is not None:
            return render(request,'search_results.html',{'results':results})
        
        
    books=BookModel.objects.all()[:9]
    return render(request,'base.html',{'genres':genres,'books':books})
