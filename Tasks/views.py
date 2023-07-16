from django.shortcuts import render,redirect
from .models import  Task
from .forms import TForm

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
        messages.error(request,'Ошибка пароля')
        return render(request,'kalendar/login.html',{'form': form})
    

def sign_out(request):
    logout(request)
    messages.success(request,'Вы вышли')
    return redirect('login')        
 
from .forms import RegisterForm
def sign_up(request):
    if request.method == 'GET':
        user_form = RegisterForm()
        context = {
            'form': user_form
        }
        return render(request, 'kalendar/register.html',context)
    if request.method == 'POST':
        user_form = RegisterForm(
            data=request.POST
        )
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Вы вошли')
            login(request, user)
            return redirect('tasks')
        else:
            context = {
                'form': user_form
            }
            messages.success(request, 'Ошибка входа')
            return render(request, 'kalendar/register.html', context)
        
#-----------------------------------------------
from django.shortcuts import get_object_or_404
import os
def edit_task(request, id):
    post = get_object_or_404(Task, id=id)
    if request.method == 'GET':
        context = {'form': TForm(instance=post), 'id': id}
        return render(request,'kalendar/task-edit.html',context)
    if request.method == 'POST':
        form = TForm(request.POST, instance=post)
        
        if form.is_valid():
            if (len(request.FILES)):
                form.img=request.FILES
            form.instance.author = request.user
            form.save()

            messages.success(request, 'Пост изменен')
            return redirect('tasks')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку в форме')
            return render(request,'kalendar/task-edit.html',{'form':form})

        
def tasks(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            tasks = Task.objects.filter(author=request.user)
            context = {'tasks': tasks, 'form': TForm()}
            return render(request, 'kalendar/tasks.html', context)
        else:
            return render(request, 'kalendar/tasks.html')
    if request.method == 'POST':
        form = TForm(request.POST, request.FILES)
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
