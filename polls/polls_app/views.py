from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Welcome to our new page lester')

def my_page(request):
    return HttpResponse('Just another page')
