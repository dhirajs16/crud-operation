from django.shortcuts import render, redirect,  get_object_or_404

from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    items = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            
            Todo.objects.create(title = title, description = description)
            
    else:
        form = TodoForm()
    return render(request, 'myapp/index.html', {'form': form, 'items':items})


def update(request, id):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            
            Todo.objects.filter(id = id).update(title = title, description = description)
    else:
        item = get_object_or_404(Todo, id=id)
    return render(request, 'myapp/update.html', { 'item' : item })

def delete(request, id):
    Todo.objects.filter(id = id).delete()
    return redirect('/')