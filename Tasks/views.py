from django.shortcuts import render,redirect
from .models import  Task
from .forms import TForm


# Create your views here.
def index(request):
    return render(request, 'kalendar/index.html')

def about(request):
    return render(request, 'kalendar/about.html')



from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .forms import LoginForm
def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('tasks')
        form = LoginForm()
        return render(request, 'kalendar/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('tasks')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'kalendar/login.html',{'form': form})
    

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')        

from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'kalendar/register.html', { 'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('tasks')
        else:
            return render(request, 'kalendar/register.html', {'form': form})
        
#-------------------------------------------------  

#-----------------------------------------------
from django.shortcuts import get_object_or_404
def edit_task(request, id):
    post = get_object_or_404(Task, id=id)
    if request.method == 'GET':
        context = {'form': TForm(instance=post), 'id': id}
        return render(request,'kalendar/task-edit.html',context)
    
    elif request.method == 'POST':
        form = TForm(request.POST, instance=post)
        
        if form.is_valid():
            form.instance.author = request.user
            form.save()

            messages.success(request, 'Пост изменен.')
            return redirect('tasks')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку в форме')
            return render(request,'kalendar/task-edit.html',{'form':form})
        
        
def tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(author=request.user)

        context = {'tasks': tasks}
        context = {'tasks': tasks, 'form': TForm()}
        return render(request, 'kalendar/tasks.html', context)
    if request.method == 'POST':
        task = Task(author=request.user)
        form = TForm(data=request.POST, instance=task)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Задача поставлена')
            return redirect('tasks')
        else:
            messages.success(request, 'Где-то проблема, поищи ошибку')
            return redirect('tasks')

def delete_post(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.success(request,  'Пост удален')
    return redirect('tasks')
