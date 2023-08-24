from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo


# Create your views here.
def index(request):
    return render(request, "todo/index.html")


@csrf_exempt
def create(request):
    Todo.objects.create(content=request.POST["content"])
    return HttpResponse("create!!")
