from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render()) 

def index_with_variables(request, num=1):
    if num == 1:
        number = "first"
    elif num == 2:
        number = "second"
    else:
        number = "nth"
    return render(request, 'indexWithVariables.html', {'number':number})

def tasks(request):
    ctx = {
        "tasks": [
            "task 1",
            "task 2",
            "task 3",
            "task 4"
        ]
    }
    return render(request, 'task_list_using_templates.html',ctx)