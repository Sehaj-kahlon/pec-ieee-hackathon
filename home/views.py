from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("this is homepage")
    return render(request, 'challenge2.html')

# added


def contact(request):
    return render(request, 'contact.html')


def tutorial(request):
    return render(request, 'tutorial.html')
