from django.shortcuts import render, redirect,  get_object_or_404

from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    items = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')            
    else:
        form = TodoForm()
    return render(request, 'myapp/index.html', {'form': form, 'items':items})


def update(request, pk):
    item = get_object_or_404(Todo, pk = pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = TodoForm(instance=item)
        print(form)
    return render(request, 'myapp/update.html', {'form': form})
   
def delete(request, pk):
    Todo.objects.filter(pk = pk).delete()
    return redirect('index')