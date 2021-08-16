
from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from App_1.models import Trial 
from App_1.form import Task_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.mm
@login_required(login_url='/user/login')
def App_1(request):
    if request.method == 'POST':
        form = Task_form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        return redirect('App_1')
    else:
        all_tasks = Trial.objects.filter(manage=request.user)
        paginator =  Paginator(all_tasks, 3)
        page_number = request.GET.get('page')
        all_tasks = paginator.get_page(page_number)
        return render (request, 'app_1.html', {'all' : all_tasks})

def home(request):
    # return HttpResponse ('Welcome to App_1 page')
    contexto = {
        'tit':'Hello, Welcome to Home page',

    }
    return render (request, 'home.html' )

@login_required(login_url='/user/login')
def contact(request):
    # return HttpResponse ('Welcome to App_1 page')
    contexto = {
        'tit':'Hello, Welcome to Contact page',

    }
    return render (request, 'contact.html', contexto )

def link(request):
    # return HttpResponse ('Welcome to App_1 page')
    contexto = {
        'tit':'Hello, Welcome to Link page',

    }
    return render (request, 'link.html', contexto )

def done_task(request,task_id):
    task = Trial.objects.get(pk= task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    
    else:
        messages.error(request, ("Accesess denied !"))
    return redirect('App_1')

def delete_task(request,task_id):
    task = Trial.objects.get(pk= task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, ("Accesess denied !"))

    return redirect('App_1')

def edit_task(request,task_id):
    if request.method == 'POST':
        task = Trial.objects.get(pk= task_id)
        form = Task_form(request.POST or None, instance= task)
        if form.is_valid():
            form.save()

        messages.success(request,("Task edited"))
        return redirect('App_1')
    else:
        task_obj = Trial.objects.get(pk=task_id)
        return render (request, 'edit.html', {"task_obj" : task_obj})

    