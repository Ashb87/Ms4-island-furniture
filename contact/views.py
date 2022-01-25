from django.shortcuts import render


def contact(request):
    """ A view to return our contact page"""

    return render(request, 'contact/contact.html')