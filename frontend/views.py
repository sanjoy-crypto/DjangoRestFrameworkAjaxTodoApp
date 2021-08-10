from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def list(request):

    context = {}
    return render(request, 'frontend/list.html', context)
