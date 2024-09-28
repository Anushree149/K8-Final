from django.shortcuts import render,redirect
from .models import Todo,Feedback
from . forms import *
from .filters import TodoFilter
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import Employee
from django.contrib.auth import authenticate
# Create your views here.

@login_required(login_url='all_login')
def my_todos(request):
    if request.user.is_admin == True:
        todos = Todo.objects.order_by("deadline").filter(company_name=request.user.company_name)
        # todos = Todo.objects.filter(company_name=request.user.company_name)
    else:
        todos = Todo.objects.filter(search=request.user.first_name+ " "+request.user.last_name)
    my_filter = TodoFilter(request.GET,queryset=todos)
    todos = my_filter.qs
    context = {
        'todos':todos,
        'my_filter':my_filter,      
    }
    return render (request,'home.html',context)


@login_required(login_url='all_login')
def add_todo(request):
    if request.method =='POST':
        form = TodoForm(request.user, data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.company_name = request.user.company_name
            task.search = form.cleaned_data['assign_to']
            task.save()
            messages.success(request,f'To-do assigned to {task.assign_to}   Successfully!!!')
            return redirect('home')
    else:
        form = TodoForm(request.user)
    context = {
        'form':form,
    }
    return render (request,'todo.html',context)


@login_required(login_url='all_login')
def todo_details(request,id):
    if request.user.is_authenticated:
        todo_details = Todo.objects.get(id=id)
        context ={
            'todo_details':todo_details,
        }
        return render(request,'details.html',context)
    else:
        messages.error(request,'You must be logged in to see the record ')
        return redirect('home')
    
@login_required(login_url='all_login')
def todo_delete(request,id):
    if request.user.is_authenticated:
        record = Todo.objects.get(id=id)
        record.delete()
        messages.success(request,f'Record {record.assign_to} Deleted Successfully!!!')
        return redirect('home')
    else:
        messages.error(request,'You must be logged in to delete a record ')
        return redirect('home')


def update_todo(request,pk):
    if request.user.is_authenticated:
        instance = Todo.objects.get(id=pk)
        if request.user.is_admin == True:
            if request.method == 'POST':
                form = AllFieldUpdateForm(request.user,data=request.POST, instance=instance)
                if form.is_valid():
                    form.save()
                    return redirect('home')  # Redirect to a success page or any other desired URL
            else:
                form = AllFieldUpdateForm(request.user,instance=instance)
        else:
            if request.method == 'POST':
                form = SpecificFieldUpdateForm(request.POST, instance=instance)
                if form.is_valid():
                    form.save()
                    return redirect('home')  # Redirect to a success page or any other desired URL
            else:
                form = SpecificFieldUpdateForm(instance=instance)

        context = {
            'form': form,
            'instance': instance,
        }
    return render(request, 'update_todo.html', context)





@login_required(login_url='all_login')
def feedback(request):
    if request.method =='POST':
        fm = FeedbackForm(request.POST)
        if fm.is_valid():
            feedback=fm.save(commit=False)
            feedback.user = request.user.first_name + " " + request.user.last_name
            feedback.save()
            messages.success(request,'Thanks for your Feedback.... ')
            return redirect('home')
    else:
        fm = FeedbackForm()
    context = {
        'form':fm
    }
    return render(request,'feedback.html',context)