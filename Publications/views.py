from django.http import HttpResponse
from django.shortcuts import render
from .models import publication

all_publications = publication.objects.all()

# Create your views here.
def index(request):
    global all_publications
    all_publications = publication.objects.all()
    total = all_publications.count()
    context = {
        'all_publications': all_publications,
        'total': total,
    }
    return render(request, 'publications/index.html', context)


def bob(request):
    global all_publications
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        search_dept = request.GET.get('search_param1', None)
        search_year = request.GET.get('search_param2', None)
        search_type = request.GET.get('search_param3', None)
        search_nationality = request.GET.get('search_param4', None)

        if (search_year == ''):
            all_publications = publication.objects.filter(
                title__contains=search_query).__or__(publication.objects.filter(author__contains=search_query)).filter(
                dept__startswith=search_dept, type__contains=search_type,
                nationality__startswith=search_nationality)
        else:
            all_publications = publication.objects.filter(
                title__contains=search_query).__or__(publication.objects.filter(author__contains=search_query)).filter(
                dept__startswith=search_dept,
                year__year=int(search_year), type__contains=search_type,
                nationality__startswith=search_nationality)
            # Do whatever you need with the word the user looked for
            # Your code
    total = all_publications.count()
    context = {
        'all_publications': all_publications,
        'total': total,
    }
    return render(request, 'publications/index.html', context)


def print(request):
    context = {
        'all_publications': all_publications,
    }
    return render(request, 'publications/print.html', context)
