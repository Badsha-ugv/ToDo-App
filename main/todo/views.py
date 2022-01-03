from django.shortcuts import render
from django.utils import timezone
from .models import ToDo
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    items = ToDo.objects.all().order_by("-added_date")
    return render(request, 'todo/index.html', {'items': items})

def create_todo(request):
    current_date = timezone.now()
    content = request.POST["contains"]
    create_obj = ToDo.objects.create(added_date = current_date,text = content)
    todo_len = ToDo.objects.all().count()
    return HttpResponseRedirect('/')

def clear_todo(request,todo_id):
    ToDo.objects.get(id = todo_id).delete()
    return HttpResponseRedirect('/')