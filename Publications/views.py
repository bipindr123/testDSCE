from django.http import HttpResponse
from django.shortcuts import render
from .models import publication


# Create your views here.
def index(request):
    all_publications = publication.objects.all()
    context = {
        'all_publications': all_publications,
    }
    return render(request, 'publications/index.html', context)


def bob(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        search_dept = request.GET.get('search_param1', None)
        search_year = request.GET.get('search_param2', None)
        if(search_year==''):
            all_publications = publication.objects.filter(title__startswith=search_query, dept__startswith=search_dept)
        else:
            all_publications = publication.objects.filter(title__startswith=search_query, dept__startswith=search_dept,year__year=int(search_year))
        # Do whatever you need with the word the user looked for
        # Your code
    context = {
        'all_publications': all_publications,
    }
    return render(request, 'publications/index.html', context)
