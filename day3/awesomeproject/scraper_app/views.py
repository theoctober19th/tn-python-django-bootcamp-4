from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    d = {
        'names': ['sashank', 'bikalpa', 'kopila', 'nischal']
    }

    return render(request, 'scraper_app/index.html', d)