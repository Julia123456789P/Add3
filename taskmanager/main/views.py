from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

#TODO отображение всех отзывов
def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница отзывов', 'tasks': tasks})

#TODO просто рендеринг страницы с контактами
def about(request):
    return render(request, 'main/about.html')

#TODO заполнение формы отзыва
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid(): #TODO проверка валицации
            form.save()
            return redirect("home")
        else:
            error = "Форма не верная"
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)