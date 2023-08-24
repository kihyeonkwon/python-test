from urllib import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo


# Create your views here.
def index(request):
    return render(request, "todo/index.html")
