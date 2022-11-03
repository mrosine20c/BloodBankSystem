from django.shortcuts import render


# Create your views here.

def indexall(request):
    return render(request, 'site/base.html')
