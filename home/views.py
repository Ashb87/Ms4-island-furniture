from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def entry_not_found(request, exception, template_name='404.html'):
    """ displays 404 template """
    return render(request, '404.html')
