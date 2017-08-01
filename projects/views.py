from django.shortcuts import render
from .models import Project

all_projects = Project.objects.all()


# Create your views here.

def index(request):
    global all_projects
    all_projects = Project.objects.all()
    total = all_projects.count()
    context = {
        'all_projects': all_projects,
        'total': total,
    }
    return render(request, 'projects/index.html', context)


def bob(request):
    global all_projects
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        search_dept = request.GET.get('search_param1', None)
        search_year = request.GET.get('search_param2', None)

        if (search_year == ''):
            all_projects = Project.objects.filter(
                funding_agency__contains=search_query, dept__contains=search_dept)
        else:
            all_projects = Project.objects.filter(
                funding_agency__contains=search_query, dept__contains=search_dept, start_date__year=search_year)
        # Do whatever you need with the word the user looked for
        # Your code
        total = all_projects.count()
        context = {
            'all_projects': all_projects,
            'total': total,
        }
    return render(request, 'projects/index.html', context)
