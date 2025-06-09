from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about_me(request):
    return HttpResponse("This would be the about page")
    return HttpResponse(
        request.method + " " + request.path + " " + str(request.META)
    )

# Create your views here.
